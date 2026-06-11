"use client";

/**
 * Styled markdown renderer for lesson content.
 * react-markdown + remark-gfm (tables, strikethrough) + rehype-raw
 * (lessons occasionally contain inline HTML like <details> or <kbd>).
 */

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";

export default function MarkdownView({ markdown }: { markdown: string }) {
  return (
    <div className="md-content">
      <ReactMarkdown remarkPlugins={[remarkGfm]} rehypePlugins={[rehypeRaw]}>
        {markdown}
      </ReactMarkdown>
    </div>
  );
}
