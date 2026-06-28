"use client";

/**
 * Confetti helpers wrapping canvas-confetti.
 * Call from client event handlers only (no-op on the server).
 */

import confetti from "canvas-confetti";

/** Short celebratory burst — for a correct quiz answer. */
export function fireConfettiBurst(): void {
  if (typeof window === "undefined") return;
  confetti({
    particleCount: 60,
    spread: 70,
    startVelocity: 35,
    origin: { y: 0.7 },
    scalar: 0.9,
  });
}

/** Big celebration — for finishing a quiz or lesson. */
export function fireConfettiCelebration(): void {
  if (typeof window === "undefined") return;
  const defaults = { startVelocity: 40, spread: 360, ticks: 80, zIndex: 50 };
  confetti({ ...defaults, particleCount: 120, origin: { x: 0.3, y: 0.5 } });
  window.setTimeout(() => {
    confetti({ ...defaults, particleCount: 120, origin: { x: 0.7, y: 0.4 } });
  }, 250);
  window.setTimeout(() => {
    confetti({ ...defaults, particleCount: 80, origin: { x: 0.5, y: 0.6 } });
  }, 500);
}
