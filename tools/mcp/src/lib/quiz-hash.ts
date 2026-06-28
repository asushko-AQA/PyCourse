import { spawn } from "node:child_process";
import path from "node:path";
import { getRepoRoot } from "../repo-root.js";

export interface QuizHashEntry {
  hash?: string;
  path: string;
  status: "ok" | "missing";
}

export interface QuizHashResult {
  entries: QuizHashEntry[];
  hashed: number;
  missing: number;
}

function runQuizHashScript(): Promise<string> {
  const root = getRepoRoot();
  return new Promise((resolve, reject) => {
    const child = spawn("python", ["tools/apply_lesson_quizzes.py", "--hash"], {
      cwd: root,
      env: process.env,
    });

    let stdout = "";
    let stderr = "";

    child.stdout.on("data", (chunk: Buffer) => {
      stdout += chunk.toString();
    });
    child.stderr.on("data", (chunk: Buffer) => {
      stderr += chunk.toString();
    });

    child.on("error", reject);
    child.on("close", (code) => {
      if (code !== 0) {
        reject(
          new Error(
            stderr.trim() ||
              `quiz_hash script exited with code ${code ?? "unknown"}`,
          ),
        );
        return;
      }
      resolve(stdout);
    });
  });
}

function parseQuizHashOutput(stdout: string): QuizHashResult {
  const entries: QuizHashEntry[] = [];
  let hashed = 0;
  let missing = 0;

  for (const line of stdout.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith("Hashed ")) continue;

    if (trimmed.startsWith("NO QUIZ:")) {
      const rel = trimmed.slice("NO QUIZ:".length).trim();
      entries.push({ path: rel.replace(/\\/g, "/"), status: "missing" });
      missing++;
      continue;
    }

    const match = trimmed.match(/^([0-9a-f]{12})\s+(.+)$/i);
    if (!match) continue;

    entries.push({
      hash: match[1],
      path: match[2].replace(/\\/g, "/"),
      status: "ok",
    });
    hashed++;
  }

  return { entries, hashed, missing };
}

export async function quizHash(lessonFilter?: string): Promise<QuizHashResult> {
  const stdout = await runQuizHashScript();
  const parsed = parseQuizHashOutput(stdout);

  if (!lessonFilter) {
    return parsed;
  }

  const needle = lessonFilter.replace(/\\/g, "/");
  const entries = parsed.entries.filter((entry) => entry.path.includes(needle));
  const hashed = entries.filter((entry) => entry.status === "ok").length;
  const missing = entries.filter((entry) => entry.status === "missing").length;

  return { entries, hashed, missing };
}

export function formatQuizHashResult(result: QuizHashResult): string {
  const lines = result.entries.map((entry) => {
    if (entry.status === "missing") {
      return `NO QUIZ: ${entry.path}`;
    }
    return `${entry.hash}  ${entry.path}`;
  });

  lines.push(`\nHashed ${result.hashed} quizzes, ${result.missing} without quiz.`);
  return lines.join("\n");
}
