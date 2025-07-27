/*
CONTEST
  ID: abc416
  TITLE: AtCoder Beginner Contest 416
  URL: https://atcoder.jp/contests/abc416

TASK
  ID: abc416_a
  LABEL: A
  TITLE: Vacation Validation
  URL: https://atcoder.jp/contests/abc416/tasks/abc416_a

To test, run the following command:
  bun run test -c "bun abc416/a/abc416-a.ts" -d abc416/a/tests

To submit, run the following command:
  bun run submit abc416/a/abc416-a.ts -t abc416_a -c abc416 -- -l 5058
*/

import { readFileSync } from 'node:fs';

const inputs = readFileSync('/dev/stdin', 'utf-8').trimEnd().split('\n');
const [_, l, r] = inputs[0]?.split(' ').map(Number) as [number, number, number];
const s = inputs[1];
if (s?.slice(l - 1, r) === 'o'.repeat(r - l + 1)) {
  console.log('Yes');
} else console.log('No');
