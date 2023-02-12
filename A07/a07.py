d = int(input())
n = int(input())
l_list = []
r_list = []
for _ in range(n):
    l, r = map(int, input().split())
    l_list.append(l)
    r_list.append(r)

# 前日比
day_before_last = [0] * (d + 2)  # 最初と最後に0を追加して初期化
for i in range(n):
    day_before_last[l_list[i]] += 1
    day_before_last[r_list[i] + 1] -= 1

ans = [0] * (d + 2)  # 最初と最後に0を追加して初期化
for d in range(1, d + 1):
    ans[d] = ans[d - 1] + day_before_last[d]
    print(ans[d])
