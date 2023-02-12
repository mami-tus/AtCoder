h, w = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
queries = [list(map(int, input().split())) for _ in range(q)]

# 縦方向の累積和
accm = [[0] * (w + 1) for _ in range(h + 1)]  # 0の行と列を追加して初期化
for i in range(1, h + 1):
    for j in range(1, w + 1):
        accm[i][j] = accm[i - 1][j] + x[i - 1][j - 1]

# 横方向の累積和
for i in range(1, h + 1):
    for j in range(1, w + 1):
        accm[i][j] += accm[i][j - 1]
for a, b, c, d in queries:
    print(accm[c][d] - accm[a - 1][d] - accm[c][b - 1] + accm[a - 1][b - 1])
