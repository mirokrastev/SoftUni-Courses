matrix = []

def add_matrix():
    arg = list(map(int, input().split()))
    matrix.append(arg)

def fn(square_matrix):
    d_left = 0
    d_right = 0
    for diagonal_left in range(square_matrix):
        d_left += matrix[diagonal_left][diagonal_left]
    for diagonal_right in range(square_matrix):
        d_right += matrix[diagonal_right][(len(matrix[diagonal_right]) - 1) - diagonal_right]

    return abs(d_left - d_right)

square_matrix = int(input())
[add_matrix() for i in range(square_matrix)]
print(fn(square_matrix))