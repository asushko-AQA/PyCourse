/** DOM id for a lesson file shown on the Files tab. Safe to import from client components. */
export function lessonFileAnchor(filePath: string): string {
  return "lesson-file-" + filePath.replace(/[^a-zA-Z0-9]+/g, "-").replace(/^-|-$/g, "");
}
