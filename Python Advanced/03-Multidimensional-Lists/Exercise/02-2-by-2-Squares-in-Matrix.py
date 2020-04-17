matrix = []

def add_matrix():
    arg = input().split()
    matrix.append(arg)

def fn(rows, columns):
    result = 0
    for row in range(rows - 1):
        for column in range(columns - 1):
            first = matrix[row][column]
            second = matrix[row][column + 1]
            third = matrix[row + 1][column]
            fourth = matrix[row + 1][column + 1]

            if all([first == second, first == third, first == fourth, second == third, second == fourth,
                    third == fourth]):
                result += 1

    return result

rows, columns = list(map(int, input().split()))
[add_matrix() for i in range(rows)]
print(fn(rows, columns))