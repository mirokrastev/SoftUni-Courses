matrix = []

def add_matrix(to_extend):
    matrix.append([])
    matrix[-1].extend(to_extend)

def fn(c):
    the_sum = 0
    for i in range(len(matrix)):
        the_sum += matrix[i][c]
    return the_sum

rows, columns = list(map(int, input().split(', ')))
[add_matrix(list(map(int, input().split()))) for i in range(rows)]
[print(fn(i)) for i in range(columns)]