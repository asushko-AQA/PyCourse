"use client";

/**
 * Tiny Web Audio chime util. Gracefully no-ops when audio is unavailable
 * (older browsers, autoplay restrictions, SSR).
 */

type ChimeKind = "correct" | "wrong" | "finish";

let ctx: AudioContext | null = null;

function getContext(): AudioContext | null {
  if (typeof window === "undefined") return null;
  try {
    if (!ctx) {
      const Ctor =
        window.AudioContext ??
        (window as unknown as { webkitAudioContext?: typeof AudioContext })
          .webkitAudioContext;
      if (!Ctor) return null;
      ctx = new Ctor();
    }
    if (ctx.state === "suspended") void ctx.resume();
    return ctx;
  } catch {
    return null;
  }
}

function tone(
  audio: AudioContext,
  freq: number,
  startAt: number,
  duration: number,
  volume = 0.18,
): void {
  const osc = audio.createOscillator();
  const gain = audio.createGain();
  osc.type = "sine";
  osc.frequency.value = freq;
  gain.gain.setValueAtTime(volume, startAt);
  gain.gain.exponentialRampToValueAtTime(0.0001, startAt + duration);
  osc.connect(gain);
  gain.connect(audio.destination);
  osc.start(startAt);
  osc.stop(startAt + duration);
}

/** Play a short feedback sound. Safe to call anywhere on the client. */
export function playChime(kind: ChimeKind): void {
  const audio = getContext();
  if (!audio) return;
  const now = audio.currentTime;

  if (kind === "correct") {
    // Cheerful two-note up
    tone(audio, 660, now, 0.15);
    tone(audio, 880, now + 0.12, 0.2);
  } else if (kind === "wrong") {
    // Gentle low blip (not scary)
    tone(audio, 220, now, 0.18, 0.1);
  } else {
    // Finish fanfare: C-E-G-C arpeggio
    tone(audio, 523, now, 0.18);
    tone(audio, 659, now + 0.14, 0.18);
    tone(audio, 784, now + 0.28, 0.18);
    tone(audio, 1047, now + 0.42, 0.35);
  }
}
