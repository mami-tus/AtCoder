def func(k: int) -> int:
    if k == 0:
        return 1
    else:
        return func(k // 2) + func(k // 3)


N = int(input())
print(func(N))
