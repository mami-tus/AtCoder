import itertools


n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]

count = 0
for x, y in itertools.combinations(range(n), 2):
    is_solved = True
    for i in range(m):
        if s[x][i] != "o" and s[y][i] != "o":
            is_solved = False
            break
    if is_solved:
        count += 1
print(count)
