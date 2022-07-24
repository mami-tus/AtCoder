red_l, red_r, blue_l, blue_r = map(int, input().split())
# red_lとblue_lを比較して小さい方の数直線を固定する
if red_l <= blue_l:
    fixed_color_l = red_l
    fixed_color_r = red_r
    not_fixed_color_l = blue_l
    not_fixed_color_r = blue_r
else:
    fixed_color_l = blue_l
    fixed_color_r = blue_r
    not_fixed_color_l = red_l
    not_fixed_color_r = red_r

if fixed_color_r <= not_fixed_color_l:
    print(0)
elif fixed_color_r < not_fixed_color_r:
    print(fixed_color_r - not_fixed_color_l)
else:
    print(not_fixed_color_r - not_fixed_color_l)
