/*
CONTEST
  ID: abc413
  TITLE: Denso Create Programming Contest 2025（AtCoder Beginner Contest 413）
  URL: https://atcoder.jp/contests/abc413

TASK
  ID: abc413_a
  LABEL: A
  TITLE: Content Too Large
  URL: https://atcoder.jp/contests/abc413/tasks/abc413_a

To test, run the following command:
  bun run test -c "bun abc413/a/abc413-a.ts" -d abc413/a/tests

To submit, run the following command:
  bun run submit abc413/a/abc413-a.ts -t abc413_a -c abc413 -- -l 5058
*/

import { readFileSync } from 'node:fs';

const inputs = readFileSync('/dev/stdin', 'utf-8').trimEnd().split('\n');
const capacity = Number((inputs[0]?.split(' ') || [])[1]);
const totalSize =
  inputs[1]
    ?.split(' ')
    .map(Number)
    ?.reduce((a, c) => a + c, 0) || 0;

const ans = capacity >= totalSize ? 'Yes' : 'No';
console.log(ans);
