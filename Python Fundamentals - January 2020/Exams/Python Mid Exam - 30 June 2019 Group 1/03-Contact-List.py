list_contact = input().split()

while True:
    cmd = input().split()
    command = cmd[0]
    if command == 'Add':
        contact = cmd[1]
        index = int(cmd[2])
        if contact not in list_contact:
            list_contact.append(contact)
        elif contact in list_contact and index <= len(list_contact) - 1 and index >= 0:
            list_contact.insert(index, contact)
    elif command == 'Remove':
        index = int(cmd[1])
        if index <= len(list_contact) - 1 and index >= 0:
            list_contact.pop(index)
    elif command == 'Export':
        startIndex = int(cmd[1])
        count = int(cmd[2])
        appender = []
        if startIndex <= len(list_contact) - 1 and startIndex >= 0:
            try:
                for i in range(count):
                    appender.append(list_contact[startIndex + i])
            except:
                print(*appender, sep=' ')
                continue
            print(*appender, sep=' ')
    elif command == 'Print' and cmd[1] == 'Normal':
        print(f'Contacts: {" ".join(list_contact)}')
        exit()
    elif command == 'Print' and cmd[1] == 'Reversed':
        list_contact.reverse()
        print(f'Contacts: {" ".join(list_contact)}')
        exit()