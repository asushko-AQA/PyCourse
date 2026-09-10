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

function onSignedIn(userId: string) {
  useProgressStore.getState().setSignedIn(true, userId);
}

function onSignedOut() {
  useProgressStore.getState().setSignedIn(false);
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  status: "unknown",

  bootstrap: async () => {
    try {
      const user = await fetchSession();
      set({ user, status: "signed_in" });
      onSignedIn(user.id);
    } catch (err) {
      if (err instanceof AuthApiError && err.code === "unauthorized") {
        set({ user: null, status: "signed_out" });
        onSignedOut();
        return;
      }
      set({ user: null, status: "signed_out" });
      onSignedOut();
    }
  },

  signIn: async (email, password) => {
    const user = await apiSignIn(email, password);
    set({ user, status: "signed_in" });
    onSignedIn(user.id);
    return user;
  },

  signOut: async () => {
    await apiSignOut();
    onSignedOut();
    set({ user: null, status: "signed_out" });
  },
}));
