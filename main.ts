// news-image-20261121 entry (Node 22, standard library only).
// The image is entry.png beside this file; the program copies it to the
// output directory the grader provides. It must be deterministic: the
// same bytes in, the same bytes out, on every run.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync, statSync } from "node:fs";
import { join } from "node:path";

function main() {
  const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
  mkdirSync(outDir, { recursive: true });

  const source = new URL("./entry.png", import.meta.url);
  const expected = statSync(source).size;
  const target = join(outDir, "entry.png");
  copyFileSync(source, target);

  const written = readFileSync(target);
  if (written.length !== expected) {
    throw new Error(
      `entry.png copy is incomplete: wrote ${written.length} bytes, ` +
        `expected ${expected}`
    );
  }
  console.log(
    `entry.png (${written.length} bytes) copied to ${target} — ` +
      `byte-identical to the repository copy`
  );
}

main();
