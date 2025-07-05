/*
CONTEST
  ID: abc413
  TITLE: Denso Create Programming Contest 2025（AtCoder Beginner Contest 413）
  URL: https://atcoder.jp/contests/abc413

TASK
  ID: abc413_b
  LABEL: B
  TITLE: cat 2
  URL: https://atcoder.jp/contests/abc413/tasks/abc413_b

To test, run the following command:
  bun run test -c "bun abc413/b/abc413-b.ts" -d abc413/b/tests

To submit, run the following command:
  bun run submit abc413/b/abc413-b.ts -t abc413_b -c abc413 -- -l 5058
*/

import { readFileSync } from 'node:fs';

const [_, ...strings] = readFileSync('/dev/stdin', 'utf-8').trim().split('\n');
const concatenatedStrings: string[] = [];

for (const s of strings) {
  for (const t of strings) {
    if (s !== t) {
      concatenatedStrings.push(s.concat(t));
    }
  }
}
console.log(String(new Set(concatenatedStrings).size));
