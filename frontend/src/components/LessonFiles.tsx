"use client";

/**
 * Files tab: the lesson folder's starter files, exercise prompts and (collapsed)
 * solution, so learners using only the web app can still get every file the
 * lesson text refers to.
 */

import { useState } from "react";
import type { Dict } from "@/lib/i18n";
import type { LessonFile } from "@/lib/types";
import MarkdownView from "./MarkdownView";

export function lessonFileAnchorId(filePath: string): string {
  return `lesson-file-${filePath.replace(/[^a-zA-Z0-9]+/g, "-")}`;
}

function fenced(file: LessonFile): string {
  return `\`\`\`\`${file.language}\n${file.content.replace(/\n$/, "")}\n\`\`\`\``;
}

function CopyButton({ text, dict }: { text: string; dict: Dict }) {
  const [copied, setCopied] = useState(false);
  return (
    <button
      type="button"
      onClick={() => {
        void navigator.clipboard?.writeText(text).then(() => {
          setCopied(true);
          setTimeout(() => setCopied(false), 1500);
        });
      }}
      className="rounded-full bg-slate-100 px-3 py-1 text-xs font-extrabold text-slate-600 hover:bg-slate-200"
    >
      {copied ? dict.files.copied : dict.files.copy}
    </button>
  );
}

function FileCard({
  file,
  dict,
  onFileLink,
}: {
  file: LessonFile;
  dict: Dict;
  onFileLink: (path: string) => void;
}) {
  return (
    <div
      id={lessonFileAnchorId(file.path)}
      data-automation-id="lesson-file"
      data-file-path={file.path}
      className="scroll-mt-24 rounded-2xl ring-1 ring-slate-200"
    >
      <div className="flex items-center justify-between gap-3 rounded-t-2xl bg-slate-50 px-4 py-2">
        <code className="text-sm font-bold text-slate-700">{file.path}</code>
        {file.language !== "markdown" && <CopyButton text={file.content} dict={dict} />}
      </div>
      <div className="px-4 py-3">
        <MarkdownView
          markdown={file.language === "markdown" ? file.content : fenced(file)}
          onFileLink={onFileLink}
        />
      </div>
    </div>
  );
}

export default function LessonFiles({
  files,
  dict,
  onFileLink,
}: {
  files: LessonFile[];
  dict: Dict;
  onFileLink: (path: string) => void;
}) {
  const groups: { kind: LessonFile["kind"]; title: string }[] = [
    { kind: "starter", title: dict.files.starter },
    { kind: "exercises", title: dict.files.exercises },
    { kind: "solution", title: dict.files.solution },
  ];

  return (
    <div className="flex flex-col gap-6">
      <p className="font-semibold text-slate-600">{dict.files.intro}</p>
      {groups.map(({ kind, title }) => {
        const group = files.filter((f) => f.kind === kind);
        if (group.length === 0) return null;
        const cards = group.map((file) => (
          <FileCard key={file.path} file={file} dict={dict} onFileLink={onFileLink} />
        ));
        return (
          <section
            key={kind}
            id={lessonFileAnchorId(`${kind}/`)}
            className="flex scroll-mt-24 flex-col gap-3"
          >
            <h2 className="text-xl font-extrabold text-slate-800">{title}</h2>
            {kind === "solution" ? (
              <details data-automation-id="lesson-solution" className="flex flex-col gap-3">
                <summary className="cursor-pointer font-bold text-violet-600">
                  {dict.files.showSolution}
                </summary>
                <div className="mt-3 flex flex-col gap-3">{cards}</div>
              </details>
            ) : (
              cards
            )}
          </section>
        );
      })}
    </div>
  );
}
