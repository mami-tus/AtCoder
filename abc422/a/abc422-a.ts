/*
CONTEST
  ID: abc422
  TITLE: AtCoder Beginner Contest 422
  URL: https://atcoder.jp/contests/abc422

TASK
  ID: abc422_a
  LABEL: A
  TITLE: Stage Clear
  URL: https://atcoder.jp/contests/abc422/tasks/abc422_a

To test, run the following command:
  bun run test -c "bun abc422/a/abc422-a.ts" -d abc422/a/tests

To submit, run the following command:
  bun run submit abc422/a/abc422-a.ts -t abc422_a -c abc422 -- -l 5058
*/

import { readFileSync } from 'node:fs';

const inputs = readFileSync('/dev/stdin', 'utf-8').trimEnd().split('-');
const i = Number(inputs[0]);
const j = Number(inputs[1]);
let nextStage = '';
if (j < 8) {
  nextStage = `${i}-${j + 1}`;
} else if (i < 8) {
  nextStage = `${i + 1}-1`;
}
console.log(nextStage);
