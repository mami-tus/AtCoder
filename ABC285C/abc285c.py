s = list(input())
ans = 0
for i, t in enumerate(reversed(s)):
    ans += ((ord(t) - ord("A")) + 1) * pow(26, i)
print(ans)
