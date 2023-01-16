N = int(input())
usernames = dict()
for _ in range(N):
    current, new = input().split()
    usernames[current] = new
print(usernames, list(usernames.keys()))

for current in list(usernames.keys()):
    new = usernames.pop(current, None)
    print(current, new, usernames)
    while new != None:
        print(current, new, usernames)
        if new == current:
            print("No")
            exit()
        new = usernames.pop(new, None)

print("Yes")
