import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import { inspectLesson } from "./lib/inspect-lesson.js";
import { formatQuizHashResult, quizHash } from "./lib/quiz-hash.js";
import { validateContent } from "./lib/validate-content.js";
import { getLogFilePath, withToolLogging } from "./logger.js";
import { assertRepoRoot, getRepoRoot } from "./repo-root.js";

function textResult(payload: unknown) {
  return {
    content: [
      {
        type: "text" as const,
        text: typeof payload === "string" ? payload : JSON.stringify(payload, null, 2),
      },
    ],
  };
}

async function main(): Promise<void> {
  const root = getRepoRoot();
  process.chdir(root);
  assertRepoRoot(root);

  const server = new McpServer({
    name: "pycourse",
    version: "0.1.0",
  });

  server.tool(
    "validate_content",
    "Validate lesson markdown across the repo (or filter by course/block/lesson slug substring). Mirrors frontend/scripts/validate-content.ts.",
    {
      course: z
        .string()
        .optional()
        .describe("Optional course slug filter, e.g. course-1-python-basics"),
      block: z
        .string()
        .optional()
        .describe("Optional block slug filter, e.g. block-1-meeting-your-computer"),
      lesson: z
        .string()
        .optional()
        .describe("Optional lesson slug filter, e.g. lesson-1-1-installing-python"),
    },
    async (args) =>
      withToolLogging("validate_content", args, async () => {
        const result = validateContent(args);
        const summary = result.ok
          ? `Validated ${result.lessonsChecked} lesson(s); no fatal problems`
          : `Validated ${result.lessonsChecked} lesson(s); ${result.problems.length} problem(s)`;
        return { summary, result: textResult(result) };
      }).then((payload) => payload),
  );

  server.tool(
    "quiz_hash",
    "Print canonical quiz hashes for lesson en.md/ru.md files (wraps tools/apply_lesson_quizzes.py --hash).",
    {
      lesson: z
        .string()
        .optional()
        .describe(
          "Optional lesson path or slug filter, e.g. lesson-1-1-installing-python",
        ),
    },
    async (args) =>
      withToolLogging("quiz_hash", args, async () => {
        const result = await quizHash(args.lesson);
        const summary = `Hashed ${result.hashed} quiz file(s), ${result.missing} missing`;
        return {
          summary,
          result: textResult({
            ...result,
            formatted: formatQuizHashResult(result),
          }),
        };
      }).then((payload) => payload),
  );

  server.tool(
    "inspect_lesson",
    "Inspect one lesson folder for section completeness, quiz parity, and starter/solution files.",
    {
      lesson_path: z
        .string()
        .describe(
          "Lesson folder path or slug, e.g. course-1-python-basics/block-1-meeting-your-computer/lesson-1-1-installing-python",
        ),
    },
    async (args) =>
      withToolLogging("inspect_lesson", args, async () => {
        const result = inspectLesson({ lessonPath: args.lesson_path });
        const issueCount =
          Object.values(result.languages).reduce(
            (count, lang) => count + lang.issues.length,
            0,
          ) + result.parityIssues.length;
        const summary =
          issueCount === 0
            ? `Lesson ${result.lessonId} looks complete`
            : `Lesson ${result.lessonId} has ${issueCount} issue(s)`;
        return { summary, result: textResult(result) };
      }).then((payload) => payload),
  );

  server.tool(
    "agent_run_logs",
    "Read recent MCP tool invocation logs written for agent observability.",
    {
      limit: z
        .number()
        .int()
        .min(1)
        .max(200)
        .optional()
        .describe("Number of most recent log lines to return (default 20)"),
    },
    async (args) =>
      withToolLogging("agent_run_logs", args, async () => {
        const fs = await import("node:fs");
        const logPath = getLogFilePath();
        if (!fs.existsSync(logPath)) {
          return {
            summary: "No MCP logs yet",
            result: textResult({ logFile: logPath, entries: [] }),
          };
        }

        const lines = fs
          .readFileSync(logPath, "utf-8")
          .split(/\r?\n/)
          .filter(Boolean);
        const limit = args.limit ?? 20;
        const entries = lines.slice(-limit).map((line) => JSON.parse(line));
        return {
          summary: `Returned ${entries.length} log entr${entries.length === 1 ? "y" : "ies"}`,
          result: textResult({ logFile: logPath, entries }),
        };
      }).then((payload) => payload),
  );

  const transport = new StdioServerTransport();
  await server.connect(transport);
}

main().catch((error) => {
  console.error("PyCourse MCP server failed to start:", error);
  process.exit(1);
});
