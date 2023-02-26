from __future__ import annotations
import sys

sys.setrecursionlimit(pow(10, 5) * 2)  # 再起回数の設定


def dfs(v: int, visited: list[bool], graph: list[int]) -> None:
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(v=neighbor, visited=visited, graph=graph)


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

visited = [False] * n
dfs(v=0, visited=visited, graph=graph)

for v in range(n):
    if not visited[v]:
        print("The graph is not connected.")
        exit()
print("The graph is connected.")
