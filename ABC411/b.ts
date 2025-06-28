// https://atcoder.jp/contests/abc411/tasks/abc411_b

import { readFileSync } from 'fs';

const input: string[] = readFileSync('/dev/stdin', 'utf8').split('\n');

const distances = (input[1]?.split(' ') || []).map(Number);

for (let i = 0; i < distances.length; i++) {
  const distanceSums: number[] = [];
  let distanceSum = 0;
  for (const d of distances.slice(i)) {
    distanceSums.push((distanceSum += d));
  }
  console.log(distanceSums.join(' '));
}
