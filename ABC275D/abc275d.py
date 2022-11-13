class Memo:
    def __init__(self):
        self.memo = {}

    def func(self, k: int) -> int:
        if k == 0:
            return 1
        if k in self.memo.keys():
            return self.memo[k]
        self.memo[k] = self.func(k // 2) + self.func(k // 3)
        return self.memo[k]


N = int(input())
memo = Memo()
print(memo.func(N))
