// https://atcoder.jp/contests/abc411/tasks/abc411_b

import { readFileSync } from 'fs';

function main(): void {
  const [nLine = '', dLine = ''] = readFileSync('/dev/stdin', 'utf8')
    .trim()
    .split('\n');

  const N = parseInt(nLine, 10);
  const adjacent: number[] = dLine.split(' ').map((x) => parseInt(x, 10));

  // 1要素多い累積和配列を作る
  // prefix[i] = 駅1から駅(i)までの距離（prefix[0] = 0）
  const prefix: number[] = new Array(N).fill(0);
  for (let i = 1; i < N; i++) {
    prefix[i] = prefix[i - 1]! + adjacent[i - 1]!;
  }

  // 各 i について、i→j (j > i) の距離を prefix[j] - prefix[i] で取得
  for (let i = 0; i < N - 1; i++) {
    const line: number[] = [];
    for (let j = i + 1; j < N; j++) {
      line.push(prefix[j]! - prefix[i]!);
    }
    console.log(line.join(' '));
  }
}

main();
