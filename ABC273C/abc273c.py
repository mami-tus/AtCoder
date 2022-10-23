import collections


N = int(input())
A = list(map(int, input().split()))
K = []  # 条件を満たす種類のリスト

for i in A:
    kind = len(set([j for j in A if j > i]))
    K.append(kind)
for i in range(N):
    c = collections.Counter(K)
    print(c[i])
