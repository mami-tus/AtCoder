/*
CONTEST
  ID: abc415
  TITLE: Japan Registry Services (JPRS) Programming Contest 2025#2 (AtCoder Beginner Contest 415)
  URL: https://atcoder.jp/contests/abc415

TASK
  ID: abc415_b
  LABEL: B
  TITLE: Pick Two
  URL: https://atcoder.jp/contests/abc415/tasks/abc415_b

To test, run the following command:
  bun run test -c "bun abc415/b/abc415-b.ts" -d abc415/b/tests


To submit, run the following command:
  bun run submit abc415/b/abc415-b.ts -t abc415_b -c abc415 -- -l 5058
*/

import { readFileSync } from 'node:fs';

const sections = readFileSync('/dev/stdin', 'utf-8').trimEnd();
let pickedSection: number[] = [];
for (const [index, section] of Object.entries(sections)) {
  if (section === '#') {
    pickedSection.push(Number(index) + 1);
  }
  if (pickedSection.length === 2) {
    console.log(pickedSection.join(','));
    pickedSection = [];
    continue;
  }
}
