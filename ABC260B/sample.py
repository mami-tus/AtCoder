from __future__ import annotations  # リストの型アノテーションつけるため


class Examinee:
    def __init__(self, id: int, math: int, english: int) -> None:
        self.id = id
        self.math = math
        self.english = english
        self.is_passed = False

    def __repr__(self) -> str:
        return f"[id: {self.id}, math: {self.math}, eng: {self.english}, passed: {self.is_passed}]"


N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
examinees: list[Examinee] = []  # 変数examineesにExaminee型の要素を格納したリストを指定

for i in range(N):
    examinees.append(Examinee(i + 1, A[i], B[i]))  # examinees = [[id: 1, math: 80, eng: 40, passed: False], ...

# 数学の点数を降順で、同点の場合id小さい順でソート
# x=examineesの各要素.is_passedなどで値にアクセスできる 例:examinees[0].is_passed = False
math_order = sorted(
    filter(lambda x: not x.is_passed, examinees),  # まだ合格してない人だけを抽出したリスト作成
    key=lambda x: (x.math, -1 * (x.id)),  # idにマイナスつけることで番号小さい順に並ぶ
    reverse=True,  # 降順でソート
)

for i in range(X):
    math_order[i].is_passed = True

english_order = sorted(
    filter(lambda x: not x.is_passed, examinees),
    key=lambda x: (x.english, -1 * (x.id)),
    reverse=True,
)
for i in range(Y):
    english_order[i].is_passed = True

score_order = sorted(
    filter(lambda x: not x.is_passed, examinees),
    key=lambda x: (x.math + x.english, -1 * (x.id)),
    reverse=True,
)
for i in range(Z):
    score_order[i].is_passed = True

for passed in filter(lambda x: x.is_passed, examinees):
    print(passed.id)
