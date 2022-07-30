red_l, red_r, blue_l, blue_r = map(int, input().split())
max_l = max(red_l, blue_l)
min_r = min(red_r, blue_r)
d = min_r - max_l
print(d if d > 0 else 0)
