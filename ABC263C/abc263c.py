import itertools


N, M = map(int, input().split())
sequences = list(itertools.combinations(range(1, M+1), N))
for i in sequences:
    print(*i)
