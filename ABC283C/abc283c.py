s = input()
count = 0
zero_count = 0
is_continuous_zero = False
for i in s:
    if i != "0":
        count += 1
        is_continuous_zero = False
    else:
        if is_continuous_zero:
            zero_count += 1
            if zero_count % 2 != 0:
                count += 1
        else:
            zero_count = 1
            count += 1
            is_continuous_zero = True
print(count)
