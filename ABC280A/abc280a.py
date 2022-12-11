h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
count = 0
for i in s:
    count += i.count("#")
print(count)
