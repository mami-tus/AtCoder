n = int(input())
s_list = input()

x = ""
is_between = False
for i in range(n):
    if s_list[i].isalpha():
        x += s_list[i]
    if is_between:
        if s_list[i] == ",":
            x += ","
        if s_list[i] == '"':
            x += '"'
            is_between = False
    else:
        if s_list[i] == ",":
            x += "."
        if s_list[i] == '"':
            x += '"'
            is_between = True
print(x)
