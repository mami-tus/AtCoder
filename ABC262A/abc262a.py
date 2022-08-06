Y = int(input())
calc = Y % 4
if calc == 1:
    print(Y + 1)
elif calc == 2:
    print(Y)
elif calc == 3:
    print(Y + 3)
else:
    print(Y + 2)
