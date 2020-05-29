def add_matrix():
    arg = [int(i) for i in input().split()]
    matrix.append(arg)


def primary_diagonal():
    result = 0
    for row in range(len(matrix)):
        result += matrix[row][row]

    return result


def secondary_diagonal():
    result = 0
    for row in range(len(matrix)):
        result += matrix[row][(len(matrix) - 1) - row]

    return result


square_matrix = int(input())
matrix = []
[add_matrix() for i in range(square_matrix)]
primary_diagonal_sum = primary_diagonal()
secondary_diagonal_sum = secondary_diagonal()
print(abs(primary_diagonal_sum - secondary_diagonal_sum))