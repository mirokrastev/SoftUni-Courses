matrix = []

def add_matrix():
    matrix.append([])
    columns = list(map(int, input().split()))
    matrix[-1].extend(columns)

def diagonal():
    the_sum = 0
    for i in range(len(matrix)):
        the_sum += matrix[i][i]

    return the_sum

square_matrix = int(input())
[add_matrix() for i in range(square_matrix)]
print(diagonal())