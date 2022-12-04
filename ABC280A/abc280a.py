h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
count = 0
for i in s:
    for j in i:
        if j == "#":
            count += 1
print(count)
