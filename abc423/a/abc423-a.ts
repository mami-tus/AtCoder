/*
CONTEST
  ID: abc423
  TITLE: AtCoder Beginner Contest 423
  URL: https://atcoder.jp/contests/abc423

TASK
  ID: abc423_a
  LABEL: A
  TITLE: Scary Fee
  URL: https://atcoder.jp/contests/abc423/tasks/abc423_a

To test, run the following command:
  bun run test -c "bun abc423/a/abc423-a.ts" -d abc423/a/tests

To submit, run the following command:
  bun run submit abc423/a/abc423-a.ts -t abc423_a -c abc423 -- -l 5058
*/

import { readFileSync } from 'node:fs';

const inputs = readFileSync('/dev/stdin', 'utf-8').trimEnd().split(' ');
// 残高
const balance = Number(inputs[0]);
const c = Number(inputs[1]);
// 引き出し可能額
let withdrawalLimit = balance;
// 手数料
let fee = (withdrawalLimit / 1000) * c;
while (withdrawalLimit + fee > balance) {
  withdrawalLimit = withdrawalLimit - 1000;
  if (withdrawalLimit < 1000) {
    withdrawalLimit = 0;
    break;
  }
  fee = (withdrawalLimit / 1000) * c;
}
console.log(String(withdrawalLimit));
