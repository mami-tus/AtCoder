s = input()
try:
    if len(s) != 8 or s[1] == "0" or not s[0].isupper() or not s[7].isupper():
        raise Exception
    int(s[1:7])
    print("Yes")
except:
    print("No")
