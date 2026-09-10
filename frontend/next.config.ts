import path from "node:path";
import type { NextConfig } from "next";

const repoRoot = path.join(__dirname, "..");

const nextConfig: NextConfig = {
  // Required for the production Docker image (frontend/Dockerfile).
  output: "standalone",
  // Course markdown lives beside frontend/ in the monorepo; trace from repo root
  // so standalone output can read lesson files at runtime when needed.
  outputFileTracingRoot: repoRoot,
  outputFileTracingIncludes: {
    "/*": ["../course-*/*/**"],
  },
  // frontend/ lives inside the course repo; pin the workspace root so Next
  // doesn't pick up unrelated lockfiles further up the tree.
  turbopack: {
    root: path.join(__dirname),
  },
};

export default nextConfig;
