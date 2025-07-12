/*
CONTEST
  ID: abc414
  TITLE: Mirrativ Programming Contest 2025 (AtCoder Beginner Contest 414)
  URL: https://atcoder.jp/contests/abc414

TASK
  ID: abc414_b
  LABEL: B
  TITLE: String Too Long
  URL: https://atcoder.jp/contests/abc414/tasks/abc414_b

To test, run the following command:
  bun run test -c "bun abc414/b/abc414-b.ts" -d abc414/b/tests

To submit, run the following command:
  bun run submit abc414/b/abc414-b.ts -t abc414_b -c abc414 -- -l 5058
*/

import { readFileSync } from 'node:fs';

function main(): void {
  const inputs = readFileSync('/dev/stdin', 'utf-8').trimEnd().split('\n');
  const N = Number(inputs[0]);
  const lines = inputs.slice(1, N + 1).map((i) => i.split(' '));

  let ans = '';
  for (const l of lines) {
    const string = l[0];
    const repeatCount = Number(l[1]);
    if (repeatCount > 100) {
      console.log('Too Long');
      return;
    }
    ans += string?.repeat(repeatCount);
    if (ans.length > 100) {
      console.log('Too Long');
      return;
    }
  }
  console.log(ans);
}

main();
