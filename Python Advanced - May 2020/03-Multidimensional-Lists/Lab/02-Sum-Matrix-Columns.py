def add_matrix():
    arg = [int(i) for i in input().split(' ')]
    matrix.append(arg)


def find_sum(column):
    result = 0
    for i in range(row):
        result += matrix[i][column]

    print(result)


row, column = [int(i) for i in input().split(', ')]
matrix = []
[add_matrix() for i in range(row)]
[find_sum(i) for i in range(column)]