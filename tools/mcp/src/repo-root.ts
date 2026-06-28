import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));

/** Repo root containing course-* folders (two levels up from tools/mcp/src). */
export function getRepoRoot(): string {
  return path.resolve(__dirname, "../../..");
}

export function assertRepoRoot(root: string): void {
  const hasCourses = fs
    .readdirSync(root)
    .some((entry) => /^course-\d+-/.test(entry));
  if (!hasCourses) {
    throw new Error(`PyCourse repo root not found at ${root}`);
  }
}
