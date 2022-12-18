n = int(input())
s_list = input()

count = 0
comma_index = []
for i, s in enumerate(s_list):
    if not s.isalpha() and s != ",":
        # "の時
        count += 1
    if count % 2 == 0:
        # 括られてない時
        if s == ",":
            comma_index.append(i)
s_list = list(s_list)
for j in comma_index:
    s_list[j : j + 1] = "."
print("".join(s_list))
