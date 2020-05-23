matrix = []

def add_matrix():
    arg = list(map(int, input().split()))
    matrix.append(arg)


def fn(rows, columns):
    the_sum = -999999999999999
    result = []
    for row in range(rows - 2):
        for column in range(columns - 2):
            first = matrix[row][column]
            second = matrix[row][column + 1]
            third = matrix[row][column + 2]
            fourth = matrix[row + 1][column]
            fifth = matrix[row + 1][column + 1]
            sixth = matrix[row + 1][column + 2]
            seventh = matrix[row + 2][column]
            eighth = matrix[row + 2][column + 1]
            ninth = matrix[row + 2][column + 2]
            three_by_three = first + second + third + fourth + fifth + sixth + seventh \
                             + eighth + ninth
            if three_by_three > the_sum:
                the_sum = three_by_three
                result = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth]

    print(f'Sum = {the_sum}')
    print(f'{result[0]} {result[1]} {result[2]}')
    print(f'{result[3]} {result[4]} {result[5]}')
    print(f'{result[6]} {result[7]} {result[8]}')

rows, columns = list(map(int, input().split()))
[add_matrix() for i in range(rows)]
fn(rows, columns)