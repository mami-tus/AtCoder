import sys

sys.setrecursionlimit(10**6)
N, M = map(int, input().split())
rode = [[] for _ in range(N)]  # 辺の情報を保存するリスト

for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    rode[u].append(v)
    rode[v].append(u)

# グラフが連結かどうか
visited = [False for _ in range(N)]


def dfs(now):
    visited[now] = True
    for i in rode[now]:
        if not visited[i]:
            dfs(i)


dfs(0)
if not all(visited):
    print("No")
    exit()

# 頂点の次数が2以下、1が2個
c = 0
for i in rode:
    if len(i) == 1:
        c += 1
    elif len(i) != 2:
        print("No")
        exit()

if c == 2:
    print("Yes")
else:
    print("No")
