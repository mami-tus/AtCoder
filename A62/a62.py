from __future__ import annotations
import sys

sys.setrecursionlimit(pow(10, 5) * 2)  # 再起回数の設定


def dfs(v: int, visited: list[bool], graph: list[int]) -> None:
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(v=neighbor, visited=visited, graph=graph)


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
dfs(v=1, visited=visited, graph=graph)

for v in range(1, n + 1):
    if not visited[v]:
        print("The graph is not connected.")
        exit()
print("The graph is connected.")
