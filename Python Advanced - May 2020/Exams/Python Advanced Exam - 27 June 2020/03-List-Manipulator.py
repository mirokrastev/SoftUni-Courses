def list_manipulator(arr, command, third_param, *args):
    if command == 'add':
        if args:
            if third_param == 'beginning':
                for i in args[::-1]:
                    arr.insert(0, i)

            elif third_param == 'end':
                for i in args:
                    arr.append(i)

    elif command == 'remove':
        if third_param == 'beginning':
            if args:
                for i in range(args[0]):
                    arr.pop(0)
            else:
                arr.pop(0)

        elif third_param == 'end':
            if args:
                for i in range(args[0]):
                    arr.pop()
            else:
                arr.pop()

    return arr