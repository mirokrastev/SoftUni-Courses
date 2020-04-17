matrix = []

def append_matrix(columns_app):
    matrix.append([])
    matrix[-1].extend(columns_app)

def sum_matrix():
    the_sum = 0
    for i in range(len(matrix)):
        the_sum += sum(matrix[i])
    return the_sum

rows,columns = map(int, input().split(', '))
[append_matrix(list(map(int, input().split(', ')))) for i in range(rows)]
print(sum_matrix())
print(matrix)