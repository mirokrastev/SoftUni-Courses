matrix = []

def add_matrix():
    matrix.append([])
    matrix[-1].extend(i for i in map(int, input().split(', ')))

[add_matrix() for i in range(int(input()))]

first_diagonal = []
second_diagonal = []

[first_diagonal.append(matrix[i][i]) for i in range(len(matrix))]
[second_diagonal.append(matrix[i][(len(matrix[i]) - 1) - i]) for i in range(len(matrix))]

print(f'First diagonal: {", ".join(map(str, first_diagonal))}. Sum: {sum(first_diagonal)}')
print(f'Second diagonal: {", ".join(map(str, second_diagonal))}. Sum: {sum(second_diagonal)}')