n, m = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(m)]
box = [[] for _ in range(n)]

for a, b in roads:
    box[a - 1].append(b)
    box[b - 1].append(a)
for i in box:
    new_i = sorted(i)
    new_i.insert(0, len(i))
    print(*new_i)
