N, M = map(int, input().split())
sides = [list(map(int, input().split())) for _ in range(M)]

# 頂点 i,j を結ぶ辺があるかどうかを表す配列adj
adj = [[False] * N for _ in range(N)]
for u, v in sides:
    u -= 1
    v -= 1
    adj[u][v] = True
    adj[v][u] = True

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if adj[i][j] and adj[j][k] and adj[k][i]:
                ans += 1
print(ans)
