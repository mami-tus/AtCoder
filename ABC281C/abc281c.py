n, t = map(int, input().split())
lengths = list(map(int, input().split()))
time = t % sum(lengths)
for i, length in enumerate(lengths):
    if time < length:
        print(i + 1, time)
        break
    time -= length
