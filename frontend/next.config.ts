import path from "node:path";
import type { NextConfig } from "next";

const repoRoot = path.join(__dirname, "..");

const nextConfig: NextConfig = {
  // Required for the production Docker image (frontend/Dockerfile).
  output: "standalone",
  // Course markdown lives beside frontend/. Trace from the repo root so the
  // standalone image still nests as standalone/frontend and can read those
  // files. turbopack.root must be that same directory: Next warns when the
  // two differ, and the mismatch makes next/font/google resolution flaky
  // when `next build` is started from the repo root (Playwright UI job)
  // instead of from frontend/. Pinning the root here also stops lockfile
  // detection from walking above the repo.
  outputFileTracingRoot: repoRoot,
  outputFileTracingIncludes: {
    "/*": ["../course-*/*/**"],
  },
  turbopack: {
    root: repoRoot,
  },
};

export default nextConfig;
