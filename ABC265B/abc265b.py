n, m, t = map(int, input().split())
consumed_times = list(map(int, input().split()))
bonus_info = [list(map(int, input().split())) for _ in range(m)]
# 持ち時間から足し引きして、0以下になった時点でNoを出力、最後まで繰り返し可能だったらYes
# もしボーナス部屋の番号XだったらYをプラス
for i in range(1, n):
    for x, y in bonus_info:
        if i == x:
            t = t + y - consumed_times[i - 1]
        else:
            t = t - consumed_times[i - 1]
    if t <= 0:
        print("No")
        exit()
print("Yes")
