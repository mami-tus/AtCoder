/*
CONTEST
  ID: abc415
  TITLE: Japan Registry Services (JPRS) Programming Contest 2025#2 (AtCoder Beginner Contest 415)
  URL: https://atcoder.jp/contests/abc415

TASK
  ID: abc415_a
  LABEL: A
  TITLE: Unsupported Type
  URL: https://atcoder.jp/contests/abc415/tasks/abc415_a

To test, run the following command:
  bun run test -c "bun abc415/a/abc415-a.ts" -d abc415/a/tests

To submit, run the following command:
  bun run submit abc415/a/abc415-a.ts -t abc415_a -c abc415 -- -l 5058
*/

import { readFileSync } from 'node:fs';

const inputs = readFileSync('/dev/stdin', 'utf-8').trimEnd().split('\n');

const supportedNums = inputs[1]?.split(' ').map(Number);
const x = Number(inputs[2]);
const ans = supportedNums?.includes(x) ? 'Yes' : 'No';
console.log(ans);
