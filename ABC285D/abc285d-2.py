N = int(input())
usernames = dict()
for _ in range(N):
    current, new = input().split()
    usernames[current] = new


for current in list(usernames.keys()):
    new = usernames.pop(current, None)
    while new != None:
        if new == current:
            print("No")
            exit()
        new = usernames.pop(new, None)

print("Yes")
