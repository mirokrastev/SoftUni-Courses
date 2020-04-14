import sys

numbers_count = int(input())
input_count = 1
biggest_number = -sys.maxsize

while input_count <= numbers_count:
    current_number = int(input())
    input_count += 1
    if current_number > biggest_number:
        biggest_number = current_number

print(biggest_number)