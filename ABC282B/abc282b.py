import itertools


n, m = map(int, input().split())
s_list = [list(input()) for _ in range(n)]
new_s = []
for s in s_list:
    for i in range(m):
        s[i] = "1" if s[i] == "o" else "0"
    bin_s = "".join(s)
    new_s.append(int(bin_s, 2))
count = 0
for x, y in itertools.combinations(range(n), 2):
    if (new_s[x] | new_s[y]) == int("1" * m, 2):
        count += 1
print(count)
