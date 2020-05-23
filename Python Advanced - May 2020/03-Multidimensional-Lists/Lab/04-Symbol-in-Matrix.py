matrix = []

def add_matrix():
    inp = input()
    matrix.append([])
    matrix[-1].append(inp)

def search(char):
    for i in range(len(matrix)):
        if char in matrix[i][0]:
            print(f'({i}, {matrix[i][0].index(char)})')
            exit()

row = int(input())
[add_matrix() for i in range(row)]
char = input()
search(char)
print(f'{char} does not occur in the matrix')