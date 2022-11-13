H, W = map(int, input().split())
C = (list(input()) for _ in range(H))
count = [0] * W
for i in C:
    for j in range(W):
        if i[j] == "#":
            count[j] += 1
print(*count)
