N = int(input())


def func(N: int) -> int:
    if N == 0:
        return 1
    else:
        return N * func(N - 1)


print(func(N))
