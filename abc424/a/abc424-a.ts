/*
CONTEST
  ID: abc424
  TITLE: AtCoder Beginner Contest 424
  URL: https://atcoder.jp/contests/abc424

TASK
  ID: abc424_a
  LABEL: A
  TITLE: Isosceles
  URL: https://atcoder.jp/contests/abc424/tasks/abc424_a

To test, run the following command:
  bun run test -c "bun abc424/a/abc424-a.ts" -d abc424/a/tests

To submit, run the following command:
  bun run submit abc424/a/abc424-a.ts -t abc424_a -c abc424 -- -l 5058
*/

import { readFileSync } from 'node:fs';

const inputs = readFileSync('/dev/stdin', 'utf-8').trimEnd().split(' ');
const a = Number(inputs[0]);
const b = Number(inputs[1]);
const c = Number(inputs[2]);
const ans = a === b || a === c || b === c ? 'Yes' : 'No';
console.log(ans);
