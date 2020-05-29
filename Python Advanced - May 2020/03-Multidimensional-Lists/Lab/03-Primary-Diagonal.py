def add_matrix():
    arg = [int(i) for i in input().split()]
    matrix.append(arg)


def calc_diagonal(index):
    global diagonal
    diagonal += matrix[index][index]


row_column = int(input())
matrix = []
diagonal = 0
[add_matrix() for i in range(row_column)]
[calc_diagonal(i) for i in range(len(matrix))]
print(diagonal)