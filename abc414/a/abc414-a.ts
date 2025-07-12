/*
CONTEST
  ID: abc414
  TITLE: Mirrativ Programming Contest 2025 (AtCoder Beginner Contest 414)
  URL: https://atcoder.jp/contests/abc414

TASK
  ID: abc414_a
  LABEL: A
  TITLE: Streamer Takahashi
  URL: https://atcoder.jp/contests/abc414/tasks/abc414_a

To test, run the following command:
  bun run test -c "bun abc414/a/abc414-a.ts" -d abc414/a/tests

To submit, run the following command:
  bun run submit abc414/a/abc414-a.ts -t abc414_a -c abc414 -- -l 5058
*/

import { readFileSync } from 'node:fs';

const inputs = readFileSync('/dev/stdin', 'utf-8').trimEnd().split('\n');
const [N, streamStartTime, streamEndTime] = inputs[0]
  ?.split(' ')
  .map(Number) as [number, number, number];

const listenersInfo = inputs
  .slice(1, 1 + N)
  .map((i) => i.split(' ').map(Number));
let listenerCount = 0;
for (const l of listenersInfo) {
  const viewingStartTime = l[0] || 0;
  const viewingEndTime = l[1] || 0;
  if (viewingStartTime <= streamStartTime && streamEndTime <= viewingEndTime) {
    listenerCount += 1;
  }
}
console.log(String(listenerCount));
