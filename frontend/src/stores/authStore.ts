"use client";

import { create } from "zustand";

import {
  AuthApiError,
  fetchSession,
  signIn as apiSignIn,
  signOut as apiSignOut,
  type SessionUser,
} from "@/lib/authClient";
import { useProgressStore } from "@/stores/progressStore";

interface AuthState {
  user: SessionUser | null;
  status: "unknown" | "signed_in" | "signed_out";
  bootstrap: () => Promise<void>;
  signIn: (email: string, password: string) => Promise<SessionUser>;
  signOut: () => Promise<void>;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  status: "unknown",

  bootstrap: async () => {
    try {
      const user = await fetchSession();
      set({ user, status: "signed_in" });
    } catch (err) {
      if (err instanceof AuthApiError && err.code === "unauthorized") {
        set({ user: null, status: "signed_out" });
        return;
      }
      set({ user: null, status: "signed_out" });
    }
  },

  signIn: async (email, password) => {
    const user = await apiSignIn(email, password);
    set({ user, status: "signed_in" });
    return user;
  },

  signOut: async () => {
    await apiSignOut();
    useProgressStore.getState().reset();
    set({ user: null, status: "signed_out" });
  },
}));
