"use client";

/**
 * Styled markdown renderer for lesson content.
 * react-markdown + remark-gfm (tables, strikethrough) + rehype-raw
 * (lessons occasionally contain inline HTML like <details> or <kbd>).
 */

import ReactMarkdown, { type Components } from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";
import { LESSON_FILE_HREF } from "@/lib/types";

interface MarkdownViewProps {
  markdown: string;
  /** Called with a lesson file path when a `#lesson-file:` link is clicked. */
  onFileLink?: (path: string) => void;
}

export default function MarkdownView({ markdown, onFileLink }: MarkdownViewProps) {
  const components: Components = {
    a({ href, children, node, ...rest }) {
      void node;
      if (href?.startsWith(LESSON_FILE_HREF)) {
        const filePath = href.slice(LESSON_FILE_HREF.length);
        return (
          <a
            {...rest}
            href={href}
            data-lesson-file={filePath}
            onClick={(e) => {
              if (!onFileLink) return;
              e.preventDefault();
              onFileLink(filePath);
            }}
          >
            {children}
          </a>
        );
      }
      return (
        <a {...rest} href={href}>
          {children}
        </a>
      );
    },
  };

  return (
    <div className="md-content">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeRaw]}
        components={components}
      >
        {markdown}
      </ReactMarkdown>
    </div>
  );
}
