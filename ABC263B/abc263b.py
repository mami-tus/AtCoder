# 人Nの親（１代前）
# リストのPiー2番目の値を見る、Piが１になるまで続けてその繰り返し回数が答え


N = int(input())
parents = list(map(int, input().split()))
count = 1
parent = parents[(N - 2)]  # 人Nの親
while parent != 1:
    parent = parents[(parent - 2)]
    count += 1
print(count)
