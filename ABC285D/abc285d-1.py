class Service:
    def __init__(
        self, users_num: int, usernames: list[list[str]], current_usernames: list[str]
    ) -> None:
        self.users_num = users_num
        self.usernames = usernames
        self.current_usernames = current_usernames
        self.new_usernames = []

    def can_change_usernames(self) -> bool:
        while len(self.current_usernames) != 0:
            for i in range(len(self.current_usernames)):
                current, new = self.usernames[i]
                # print(current, new, self.users_num, len(self.current_usernames))
                if new in self.current_usernames and new not in self.new_usernames:
                    continue
                else:
                    self.current_usernames.remove(current)
                    self.new_usernames.append(new)
            if self.users_num == len(self.current_usernames):
                return False
        return True


n = int(input())
usernames = [list(input().split()) for _ in range(n)]
current_usernames = []
for current, new in usernames:
    current_usernames.append(current)
service = Service(n, usernames, current_usernames)
if service.can_change_usernames():
    print("Yes")
else:
    print("No")
