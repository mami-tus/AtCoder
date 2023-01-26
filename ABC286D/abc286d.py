N, X = map(int, input().split())
a = []
b = []
for i in range(N):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)


dp = [[False for _ in range(X + 1)] for __ in range(N + 1)]
dp[0][0] = True
# i種類の硬貨でj円を払うことができるのか
for i in range(N):
    for j in range(X + 1):
        for k in range(b[i] + 1):
            if j - k * a[i] >= 0 and dp[i][j - k * a[i]]:
                dp[i + 1][j] = True

if dp[N][X]:
    print("Yes")
else:
    print("No")
