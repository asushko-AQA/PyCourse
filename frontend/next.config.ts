import path from "node:path";
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  // frontend/ lives inside the course repo; pin the workspace root so Next
  // doesn't pick up unrelated lockfiles further up the tree.
  turbopack: {
    root: path.join(__dirname),
  },
};

export default nextConfig;
