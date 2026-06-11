"use client";

/**
 * Navbar XP / level badge with an animated count-up and a mini progress bar
 * toward the next level. Hydration-safe: shows 0 XP until the persisted
 * store is available on the client.
 */

import { useEffect, useRef, useState } from "react";
import {
  getLevel,
  getLevelProgress,
  useHydrated,
  useProgressStore,
} from "@/stores/progressStore";

interface XPBadgeProps {
  levelLabel: string;
  xpLabel: string;
}

/** Animate a number toward `target` with a short ease-out count-up. */
function useCountUp(target: number): number {
  const [value, setValue] = useState(target);
  const fromRef = useRef(target);

  useEffect(() => {
    const from = fromRef.current;
    if (from === target) return;
    const duration = 600;
    const start = performance.now();
    let raf = 0;
    const tick = (now: number) => {
      const t = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - t, 3);
      setValue(Math.round(from + (target - from) * eased));
      if (t < 1) raf = requestAnimationFrame(tick);
      else fromRef.current = target;
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [target]);

  return value;
}

export default function XPBadge({ levelLabel, xpLabel }: XPBadgeProps) {
  const hydrated = useHydrated();
  const xp = useProgressStore((s) => s.xp);
  const shownXp = useCountUp(hydrated ? xp : 0);
  const level = getLevel(hydrated ? xp : 0);
  const progress = getLevelProgress(hydrated ? xp : 0);

  return (
    <div className="flex items-center gap-3 rounded-full bg-white/80 px-4 py-1.5 shadow-sm ring-1 ring-amber-200">
      <span className="flex items-center gap-1 text-sm font-bold text-amber-600">
        <span aria-hidden>⭐</span>
        {shownXp} {xpLabel}
      </span>
      <div className="flex items-center gap-2">
        <span className="rounded-full bg-violet-100 px-2 py-0.5 text-xs font-extrabold text-violet-700">
          {levelLabel} {level}
        </span>
        <div className="h-2 w-16 overflow-hidden rounded-full bg-violet-100">
          <div
            className="h-full rounded-full bg-gradient-to-r from-violet-400 to-fuchsia-400 transition-all duration-500"
            style={{ width: `${Math.round(progress * 100)}%` }}
          />
        </div>
      </div>
    </div>
  );
}
