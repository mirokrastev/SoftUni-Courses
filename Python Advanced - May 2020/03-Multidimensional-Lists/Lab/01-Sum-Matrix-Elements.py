def add_matrix():
    arg = [int(i) for i in input().split(', ')]
    matrix.append(arg)


def calculate_matrix(matrix):
    result = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            result += matrix[row][column]
    return result


row, column = [int(i) for i in input().split(', ')]
matrix = []
[add_matrix() for i in range(row)]
the_sum = calculate_matrix(matrix)
print(the_sum)
print(matrix)