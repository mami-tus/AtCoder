s = input()
t = input()

l = len(t)
for i in range(len(t)):
    if s[i] == "?" or t[i] == "?":
        continue
    if s[i] != t[i]:
        l = i
        break

r = len(t)
for i in range(len(t)):
    if s[-i - 1] == "?" or t[-i - 1] == "?":
        continue
    if s[-i - 1] != t[-i - 1]:
        r = i
        break

for x in range(len(t) + 1):
    if x <= l and len(t) - x <= r:
        print("Yes")
    else:
        print("No")
