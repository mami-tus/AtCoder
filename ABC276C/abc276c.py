import itertools


n = int(input())
p = list(map(int, input().split()))
permutations = list(itertools.permutations(range(1, n + 1), n))
index = 0
for i in permutations:
    if p == list(i):
        break
    index += 1
print(*list(permutations)[index - 1])
