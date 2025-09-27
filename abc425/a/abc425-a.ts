/*
CONTEST
  ID: abc425
  TITLE: UNIQUE VISION Programming Contest 2024 Autumn (AtCoder Beginner Contest 425)
  URL: https://atcoder.jp/contests/abc425

TASK
  ID: abc425_a
  LABEL: A
  TITLE: Sigma Cubes
  URL: https://atcoder.jp/contests/abc425/tasks/abc425_a

To test, run the following command:
  bun run test -c "bun abc425/a/abc425-a.ts" -d abc425/a/tests

To submit, run the following command:
  bun run submit abc425/a/abc425-a.ts -t abc425_a -c abc425 -- -l 5058
*/

import { readFileSync } from 'node:fs';

const n = Number(readFileSync('/dev/stdin', 'utf-8').trimEnd());
let ans = 0;
for (let i = 1; i < n + 1; i++) {
  ans += (-1) ** i * i ** 3;
}
console.log(String(ans));
