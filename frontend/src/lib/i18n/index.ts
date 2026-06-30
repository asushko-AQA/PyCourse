import type { Lang } from "../types";
import { en } from "./en";
import { ru } from "./ru";

/** All UI chrome strings. Course content itself comes from the markdown. */
export interface Dict {
  appName: string;
  tagline: string;
  home: {
    welcome: string;
    subtitle: string;
    lessons: string;
    completed: string;
    start: string;
    continue: string;
  };
  nav: {
    level: string;
    xp: string;
  };
  map: {
    backHome: string;
    locked: string;
    lockedHint: string; // "{lesson}" placeholder = prerequisite title
    yourProgress: string;
  };
  tabs: {
    theory: string;
    assignments: string;
    quiz: string;
  };
  lesson: {
    lockedTitle: string;
    lockedBody: string; // "{lesson}" placeholder = prerequisite title
    backToMap: string;
    goToPrereq: string;
    markDone: string;
    markedDone: string;
    nextLesson: string;
    noQuiz: string;
  };
  quiz: {
    questionOf: string; // "{current}" and "{total}" placeholders
    correct: string[];
    wrong: string[];
    hint: string;
    next: string;
    finish: string;
    resultsTitle: string;
    resultsBody: string; // "{score}" and "{total}" placeholders
    xpEarned: string; // "{xp}" placeholder
    alreadyEarned: string;
    replay: string;
    backToMap: string;
    nextLesson: string;
  };
  auth: {
    registerTitle: string;
    registerSubtitle: string;
    emailLabel: string;
    passwordLabel: string;
    passwordHint: string;
    minorLabel: string;
    guardianEmailLabel: string;
    consentLabel: string;
    submit: string;
    submitting: string;
    checkEmailTitle: string;
    checkEmailBody: string; // "{email}" placeholder
    checkEmailGuardianBody: string; // "{email}" placeholder (guardian)
    registerAnother: string;
    verifyTitle: string;
    verifying: string;
    verifiedTitle: string;
    verifiedBody: string;
    verifyFailedTitle: string;
    backHome: string;
    errors: {
      generic: string;
      email_already_registered: string;
      weak_password: string;
      parental_consent_required: string;
      invalid_token: string;
      token_expired: string;
      token_used: string;
      missing_token: string;
    };
  };
  courses: Record<string, { title: string; description: string; emoji: string }>;
  /** Keyed by "{courseId}/{blockId}" since block ids repeat across courses. */
  blocks: Record<string, { title: string; emoji: string }>;
}

const dicts: Record<Lang, Dict> = { en, ru };

export function getDict(lang: Lang): Dict {
  return dicts[lang];
}

/** Tiny template helper: fill("{a} + {b}", {a: "1", b: "2"}) → "1 + 2". */
export function fill(
  template: string,
  values: Record<string, string | number>,
): string {
  return template.replace(/\{(\w+)\}/g, (_, k) => String(values[k] ?? ""));
}
