from decimal import Decimal, ROUND_HALF_UP

X, K = map(int, input().split())
result = X
for i in range(K):
    result = int(Decimal(result).quantize(Decimal(f"1E{i+1}"), rounding=ROUND_HALF_UP))
print(result)
