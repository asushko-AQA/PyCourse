import fs from "node:fs";
import path from "node:path";
import { getRepoRoot } from "./repo-root.js";

export interface ToolLogEntry {
  timestamp: string;
  tool: string;
  args: Record<string, unknown>;
  status: "success" | "error";
  durationMs: number;
  summary: string;
  error?: string;
}

const LOG_DIR = path.join(getRepoRoot(), "documents", "agent-runs");
const LOG_FILE = path.join(LOG_DIR, "mcp-tools.jsonl");

function ensureLogDir(): void {
  fs.mkdirSync(LOG_DIR, { recursive: true });
}

export function getLogFilePath(): string {
  return LOG_FILE;
}

export function logToolCall(entry: ToolLogEntry): void {
  ensureLogDir();
  fs.appendFileSync(LOG_FILE, `${JSON.stringify(entry)}\n`, "utf-8");
}

export async function withToolLogging<T>(
  tool: string,
  args: Record<string, unknown>,
  run: () => Promise<{ summary: string; result: T }>,
): Promise<T> {
  const started = Date.now();
  try {
    const { summary, result } = await run();
    logToolCall({
      timestamp: new Date().toISOString(),
      tool,
      args,
      status: "success",
      durationMs: Date.now() - started,
      summary,
    });
    return result;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    logToolCall({
      timestamp: new Date().toISOString(),
      tool,
      args,
      status: "error",
      durationMs: Date.now() - started,
      summary: message,
      error: message,
    });
    throw error;
  }
}
