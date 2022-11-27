class Figure:
    def __init__(self, height: int, width: int, elements: list[list[str]]) -> None:
        self.height = height
        self.width = width
        self.elements = elements

    def get_transposed_figure(self) -> list[list[str]]:
        return list(map(list, zip(*self.elements)))


h, w = map(int, input().split())
figure_s = Figure(h, w, [list(input()) for _ in range(h)])
figure_t = Figure(h, w, [list(input()) for _ in range(h)])
transposed_s = figure_s.get_transposed_figure()
transposed_t = figure_t.get_transposed_figure()
if sorted(transposed_s) == sorted(transposed_t):
    print("Yes")
else:
    print("No")
