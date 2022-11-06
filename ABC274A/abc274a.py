from decimal import ROUND_HALF_UP, Decimal


A, B = map(int, input().split())
result = B / A
result = Decimal(str(result)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP)
print(result)
