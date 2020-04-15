book_shelf = input().split('&')

while True:
    cmd = input().split(' | ')
    command = cmd[0]
    if command == 'Done':
        print(*book_shelf, sep=', ')
        exit()
    if command == 'Add Book':
        book_name = cmd[1]
        if book_name not in book_shelf:
            book_shelf.insert(0, book_name)
    elif command == 'Take Book':
        book_name = cmd[1]
        if book_name in book_shelf:
            book_shelf.remove(book_name)
    elif command == 'Swap Books':
        book_one = cmd[1]
        book_two = cmd[2]
        if book_one in book_shelf and book_two in book_shelf:
            book_shelf[book_shelf.index(book_two)], book_shelf[book_shelf.index(book_one)] = book_shelf[book_shelf.index(book_one)], book_shelf[book_shelf.index(book_two)]
    elif command == 'Insert Book':
        book_name = cmd[1]
        book_shelf.append(book_name)
    elif command == 'Check Book' and int(cmd[1]) <= len(book_shelf) and int(cmd[1]) >= 0:
        index_book = int(cmd[1])
        print(f'{book_shelf[index_book]}')