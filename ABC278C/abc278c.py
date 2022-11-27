class TwidaiUser:
    def __init__(self, num: int, following_users: set[int]):
        self.num = num
        self.following_users = following_users

    def add_following_user(self, user_num: int):
        self.following_users.add(user_num)

    def remove_following_user(self, user_num: int):
        self.following_users.remove(user_num)


n, q = map(int, input().split())
queries = [tuple(map(int, input().split())) for _ in range(q)]
twidai_users = [TwidaiUser(num, set()) for num in range(1, n + 1)]
for t, a, b in queries:
    twidai_user_a = twidai_users[a - 1]
    twidai_user_b = twidai_users[b - 1]
    if t == 1:
        twidai_user_a.add_following_user(twidai_user_b.num)
    elif t == 2:
        if twidai_user_b.num in twidai_user_a.following_users:
            twidai_user_a.remove_following_user(twidai_user_b.num)
    else:
        if (
            twidai_user_b.num in twidai_user_a.following_users
            and twidai_user_a.num in twidai_user_b.following_users
        ):
            print("Yes")
        else:
            print("No")
