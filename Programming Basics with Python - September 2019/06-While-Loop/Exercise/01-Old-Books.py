book = input()
library_capacity = int(input())
books_searched = 1

while books_searched <= library_capacity:
    books_searched += 1
    books_inputed = input()

    if books_inputed == book:
        books_searched -= 2
        print(f'You checked {books_searched} books and found it.')
        exit()

books_searched -= 1
print(f'The book you search is not here!\nYou checked {books_searched} books.')