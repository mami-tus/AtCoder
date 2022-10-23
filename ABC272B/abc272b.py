import itertools

n, m = map(int, input().split())
participants = []
for i in range(m):
    kx = list(map(int, input().split()))
    x = kx[1:]
    participants.append(x)
# 2人の組み合わせを列挙
combinations = list(itertools.combinations(range(1, n + 1), 2))
for combi in combinations:
    has_participated = False
    for j in participants:
        if combi[0] in j and combi[1] in j:
            has_participated = True
            break
    # 2人の組み合わせが参加した舞踏会が存在しなければその時点でNo
    if not has_participated:
        print("No")
        exit()
print("Yes")
