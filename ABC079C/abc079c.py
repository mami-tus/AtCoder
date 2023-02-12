abcd = input()
for bit in range(1 << 3):
    formula = abcd[0]
    for i in range(3):
        formula += " "
        if bit & (1 << i):
            formula += "+"
        else:
            formula += "-"
        formula += abcd[i + 1]
        formula += " "

    if sum(map(int, formula.split())) == 7:
        print(formula.replace(" ", "") + "=7")
        exit()
