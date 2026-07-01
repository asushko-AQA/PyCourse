/**
 * Thin client for the FastAPI auth endpoints (plan 06).
 *
 * The typed, generated client arrives in plan 11; until then this hand-written
 * wrapper covers register/verify/sign-in/sign-out/session bootstrap.
 */

const BACKEND_URL = (
  process.env.NEXT_PUBLIC_BACKEND_URL ?? "http://localhost:8000"
).replace(/\/$/, "");

/** Error codes the backend returns in `detail.code`; mapped to i18n strings. */
export type AuthErrorCode =
  | "generic"
  | "email_already_registered"
  | "weak_password"
  | "parental_consent_required"
  | "invalid_credentials"
  | "email_not_verified"
  | "too_many_attempts"
  | "unauthorized"
  | "invalid_token"
  | "token_expired"
  | "token_used"
  | "missing_token";

export class AuthApiError extends Error {
  code: AuthErrorCode;
  constructor(code: AuthErrorCode, message?: string) {
    super(message ?? code);
    this.code = code;
  }
}

export interface RegisterInput {
  email: string;
  password: string;
  isMinor: boolean;
  guardianEmail?: string;
  parentalConsent: boolean;
}

export interface RegisterResult {
  userId: string;
  email: string;
  verificationRequired: boolean;
  isMinor: boolean;
}

export interface SessionUser {
  id: string;
  email: string;
  emailVerifiedAt: string;
}

async function parseErrorCode(res: Response): Promise<AuthErrorCode> {
  try {
    const data = await res.json();
    const code = data?.detail?.code;
    if (typeof code === "string") return code as AuthErrorCode;
  } catch {
    // fall through
  }
  return "generic";
}

export async function register(input: RegisterInput): Promise<RegisterResult> {
  let res: Response;
  try {
    res = await fetch(`${BACKEND_URL}/auth/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({
        email: input.email,
        password: input.password,
        is_minor: input.isMinor,
        guardian_email: input.guardianEmail || null,
        parental_consent: input.parentalConsent,
      }),
    });
  } catch {
    throw new AuthApiError("generic", "network error");
  }

  if (!res.ok) throw new AuthApiError(await parseErrorCode(res));

  const data = await res.json();
  return {
    userId: data.user_id,
    email: data.email,
    verificationRequired: data.verification_required,
    isMinor: data.is_minor,
  };
}

export async function verifyEmail(token: string): Promise<void> {
  let res: Response;
  try {
    res = await fetch(`${BACKEND_URL}/auth/verify`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ token }),
    });
  } catch {
    throw new AuthApiError("generic", "network error");
  }

  if (!res.ok) throw new AuthApiError(await parseErrorCode(res));
}

export async function signIn(email: string, password: string): Promise<SessionUser> {
  let res: Response;
  try {
    res = await fetch(`${BACKEND_URL}/auth/sign-in`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify({ email, password }),
    });
  } catch {
    throw new AuthApiError("generic", "network error");
  }

  if (!res.ok) throw new AuthApiError(await parseErrorCode(res));
  const data = await res.json();
  return {
    id: data.user.id,
    email: data.user.email,
    emailVerifiedAt: data.user.email_verified_at,
  };
}

export async function fetchSession(): Promise<SessionUser> {
  let res: Response;
  try {
    res = await fetch(`${BACKEND_URL}/auth/session`, {
      method: "GET",
      credentials: "include",
    });
  } catch {
    throw new AuthApiError("generic", "network error");
  }

  if (!res.ok) throw new AuthApiError(await parseErrorCode(res));
  const data = await res.json();
  return {
    id: data.user.id,
    email: data.user.email,
    emailVerifiedAt: data.user.email_verified_at,
  };
}

export async function signOut(): Promise<void> {
  let res: Response;
  try {
    res = await fetch(`${BACKEND_URL}/auth/sign-out`, {
      method: "POST",
      credentials: "include",
    });
  } catch {
    throw new AuthApiError("generic", "network error");
  }

  if (!res.ok) throw new AuthApiError(await parseErrorCode(res));
}
