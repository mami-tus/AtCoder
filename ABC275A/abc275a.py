N = int(input())
H = list(map(int, input().split()))
i = 1
max = 0
max_i = 0
for h in H:
    if max < h:
        max = h
        max_i = i
    i += 1
print(max_i)
