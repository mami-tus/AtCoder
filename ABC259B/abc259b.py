import math


a, b, d = map(int, input().split())
# (a,b)の原点からの距離をr、角度をθ、θをd°増やした角度をθ'とする
# 原点からの距離がr、角度がθ'である点の座標(x,y)が解
r = math.hypot(a, b)
theta = math.atan2(b, a)  # θを求める
theta += math.radians(d)  # θ’を求める
# 公式：sinθ = y/r, cosθ = x/r より
x = math.cos(theta) * r
y = math.sin(theta) * r
print(x, y)
