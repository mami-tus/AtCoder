n = int(input())
p = list(map(int, input().split()))


# 単調増加でない要素を探す
i = n - 2
while p[i] < p[i + 1]:
    i -= 1

# p[i]より小さい要素を後ろから探す
j = n - 1
while p[i] < p[j]:
    j -= 1

p[i], p[j] = p[j], p[i]
x = p[: i + 1]
y = p[i + 1 :]
y.sort(reverse=True)
print(*x, *y)
