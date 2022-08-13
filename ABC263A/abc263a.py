import collections


nums = list(map(int, input().split()))
count = collections.Counter(nums)
most_common_count = count.most_common()  # 出現回数多い順にする
if most_common_count[0][1] == 3 and most_common_count[1][1] == 2:
    print("Yes")
else:
    print("No")
