s = input()
if (
    len(s) != 8
    or s[1] == "0"
    or not s[0].isalpha()
    or not s[7].isalpha()
    or not s[1:7].isdecimal()
):
    print("No")
else:
    print("Yes")
