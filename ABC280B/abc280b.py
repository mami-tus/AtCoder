n = int(input())
s = list(map(int, input().split()))
a = []
for i in range(n):
    if i != (n - 1):
        a.insert(0, (s[-1] - s[-2]))
        del s[-1]
    else:
        a.insert(0, s[-1])
print(*a)
