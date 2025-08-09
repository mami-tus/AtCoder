/*
CONTEST
  ID: abc418
  TITLE: AtCoder Beginner Contest 418
  URL: https://atcoder.jp/contests/abc418

TASK
  ID: abc418_a
  LABEL: A
  TITLE: I'm a teapot
  URL: https://atcoder.jp/contests/abc418/tasks/abc418_a

To test, run the following command:
  bun run test -c "bun abc418/a/abc418-a.ts" -d abc418/a/tests

To submit, run the following command:
  bun run submit abc418/a/abc418-a.ts -t abc418_a -c abc418 -- -l 5058
*/

import { readFileSync } from 'node:fs';

const inputs = readFileSync('/dev/stdin', 'utf-8').trimEnd().split('\n');
const s = inputs[1];
console.log(s?.endsWith('tea') ? 'Yes' : 'No');
