class TwidaiUser:
    def __init__(self, num: int, followers: list[int]):
        self.num = num
        self.followers = followers


n, q = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(q)]
twidai_users = [TwidaiUser(num, []) for num in range(1, n + 1)]
for t, a, b in queries:
    twidai_user_a = twidai_users[a - 1]
    twidai_user_b = twidai_users[b - 1]
    if t == 1:
        if twidai_user_b.num not in twidai_user_a.followers:
            twidai_user_a.followers.append(twidai_user_b.num)
    elif t == 2:
        if twidai_user_b.num in twidai_user_a.followers:
            twidai_user_a.followers.remove(twidai_user_b.num)
    else:
        if (
            twidai_user_b.num in twidai_user_a.followers
            and twidai_user_a.num in twidai_user_b.followers
        ):
            print("Yes")
        else:
            print("No")
