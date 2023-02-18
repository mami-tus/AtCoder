s = input()
n = len(s) - 1  # 間に入る"+"の数
ans = 0
for bit in range(1 << n):
    formula = s[0]
    for i in range(n):
        if bit & (1 << i):
            formula += "+"
        formula += s[i + 1]
    ans += sum(map(int, formula.split("+")))
print(ans)
