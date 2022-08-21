x, y, n = map(int, input().split())

prices = []
for i in range(n + 1):
    for j in range(n + 1):
        if (i * 1) + (j * 3) == n:
            price = (x * i) + (y * j)
            prices.append(price)
print(min(prices))
