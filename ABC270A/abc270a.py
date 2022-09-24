a, b = map(int, input().split())


def get_corrected_test(score: int) -> list:
    corrected_test = [False, False, False]
    if score == 0:
        pass
    elif score == 1:
        corrected_test = [True, False, False]
    elif score == 2:
        corrected_test = [False, True, False]
    elif score == 3:
        corrected_test = [True, True, False]
    elif score == 4:
        corrected_test = [False, False, True]
    elif score == 5:
        corrected_test = [True, False, True]
    elif score == 6:
        corrected_test = [False, True, True]
    else:
        corrected_test = [True, True, True]
    return corrected_test


a_corrected_test = get_corrected_test(a)
b_corrected_test = get_corrected_test(b)
ans = 0
if a_corrected_test[0] or b_corrected_test[0]:
    ans += 1
if a_corrected_test[1] or b_corrected_test[1]:
    ans += 2
if a_corrected_test[2] or b_corrected_test[2]:
    ans += 4
print(ans)
