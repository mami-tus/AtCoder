import collections


S = input()
unique_letter = len(set(S))
if unique_letter == 3:
    print(S[0])
elif unique_letter == 2:
    # 重複してない文字を探す
    ans = [k for k, v in collections.Counter(S).items() if v == 1]
    print(ans[0])
else:
    print(-1)
