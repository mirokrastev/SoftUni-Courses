def get_magic_triangle(n):
    triangle = [[0 for i in range(x+1)]
    for x in range(n)]

    for row in range(n):
        for col in range(row+1):
            if col == 0 or col == row:
                triangle[row][col] = 1
            else:
                triangle[row][col] = triangle[row-1][col-1] + \
                    triangle[row-1][col]

    return triangle