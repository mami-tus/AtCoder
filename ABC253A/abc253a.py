import statistics

nums = list(map(int, input().split()))
median = statistics.median(nums)
if nums[1] == median:
    print("Yes")
else:
    print("No")
