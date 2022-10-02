n, q = map(int, input().split())
sequence = [list(map(int, input().split())) for _ in range(n)]
queries = [list(map(int, input().split())) for _ in range(q)]
for i in queries:
    print(sequence[i[0] - 1][i[1]])
