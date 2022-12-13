h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
print(sum(map(lambda x: x.count("#"), s)))
