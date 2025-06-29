// https://atcoder.jp/contests/abc412/tasks/abc412_a

import { readFileSync } from 'fs';

function main(): void {
  const lines = readFileSync('/dev/stdin', 'utf8').trim().split('\n');

  const N = Number(lines[0]);
  const tasks = lines
    .slice(1, 1 + N) // 必要行だけ取り出す
    .map((line) => line.split(' ').map(Number) as [number, number]); // ["a","b"] → [a, b]

  const count = tasks.filter(([a, b]) => a < b).length;

  console.log(count);
}

main();
