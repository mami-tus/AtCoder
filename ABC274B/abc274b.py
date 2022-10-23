import collections


H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
for j in range(W):
    column = [i[j] for i in C]
    count = collections.Counter(column)
    print(count["#"])
