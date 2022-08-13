r, c = map(int, input().split())
dist = max(abs(8 - r), abs(8 - c))
if dist % 2 != 0:
    print("black")
else:
    print("white")
