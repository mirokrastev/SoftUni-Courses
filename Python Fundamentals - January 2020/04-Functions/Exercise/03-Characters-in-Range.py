char_one = input()
char_two = input()
def characters(a,b):
    sum_char_one = ord(char_one)
    sum_char_two = ord(char_two)
    for i in range(sum_char_one + 1, sum_char_two):
        print(chr(i), end=' ')
characters(char_one, char_two)