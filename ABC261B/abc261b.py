import itertools


N = int(input())
A = [input() for _ in range(N)]
combinations = list(itertools.combinations(range(N), 2))

for i, j in combinations:
    if A[i][j] == "W" and A[j][i] != "L":
        print("incorrect")
        exit()
    elif A[i][j] == "L" and A[j][i] != "W":
        print("incorrect")
        exit()
    elif A[i][j] == "D" and A[j][i] != "D":
        print("incorrect")
        exit()
print("correct")
