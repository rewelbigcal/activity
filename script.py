A = [
    [18, 19, 2],
    [5, 9, 9]
]
print(A)

B = [
    [2, 0, 2],
    [3, 1, 3]
]
print(B)

C = [
    [18 + 2], [19 + 0], [2 + 2],
    [5 + 3], [9 + 1], [9 + 3],
]
print(C)

D = [
    [2 * 18], [2 * 19], [2 * 2],
    [2 * 5], [2 * 9], [2 * 9],
]
print(D)

E = [
    [2, 0, 2],
    [3, 1, 3]
]
result = [[E[j][i] for j in range(len(E))] for i in range(len(E))]
print(result)

X = [
    [20], [19], [4], [8], [10], [12]
]

Y = [
    [2, 3],
    [0, 1],
    [2, 3]
]
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
print(result)

G = [
    [20 + 19 + 4 + 8 + 10 + 12]
]
print(G)
matrix = [[0 for _ in range(3)] for _ in range(2)]
print(matrix)