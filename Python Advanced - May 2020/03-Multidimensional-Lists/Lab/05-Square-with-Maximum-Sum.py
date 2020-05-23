matrix = []
max_sum = None
best_result = None

def add_matrix():
    arg = list(map(int, input().split(', ')))
    matrix.append(arg)

def search_matrix(rows, columns):
    global max_sum, best_result
    for row in range(rows - 1):
        for column in range(columns - 1):
            first = matrix[row][column]
            second = matrix[row][column + 1]
            third = matrix[row + 1][column]
            fourth = matrix[row + 1][column + 1]
            two_by_two_sum = first + second + third + fourth

            if not max_sum:
                max_sum = two_by_two_sum
                best_result = [first, second, third, fourth]

            if two_by_two_sum > max_sum:
                max_sum = two_by_two_sum
                best_result = [first, second, third, fourth]

def print_matrix(matrix, result):
    print(f'{matrix[0]} {matrix[1]}')
    print(f'{matrix[2]} {matrix[3]}')
    print(f'{result}')

rows, columns = list(map(int, input().split(', ')))
[add_matrix() for i in range(rows)]
search_matrix(rows, columns)
print_matrix(best_result, max_sum)