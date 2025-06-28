// index.ts
import { readFileSync } from 'fs';

const input: string[] = readFileSync('/dev/stdin', 'utf8').split('\n');

const p = input[0] || '';
const l = Number(input[1]);
const ans = p.length >= l ? 'Yes' : 'No';
console.log(ans);
