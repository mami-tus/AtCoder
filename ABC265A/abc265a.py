x, y, n = map(int, input().split())


# りんご1個の値段がx円の方が安い時(x*n)円が答え
if x <= (y / 3):
    print(x * n)
# y円の方が安い時 (n%3)*x + (n//3)*y
else:
    print((n % 3) * x + (n // 3) * y)
