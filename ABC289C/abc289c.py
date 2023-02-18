n, m = map(int, input().split())
s_list = []
for _ in range(m):
    c = input()
    s = list(map(int, input().split()))
    s_list.append(s)

ans = 0
# m個の集合を1個以上選ぶ
for bit in range(1, 1 << m):
    selected_set = set()
    for i in range(m):
        if bit & (1 << i):
            # その桁のbitが立っている
            selected_set |= set(s_list[i])
    if selected_set == set(range(1, n + 1)):
        ans += 1
print(ans)
