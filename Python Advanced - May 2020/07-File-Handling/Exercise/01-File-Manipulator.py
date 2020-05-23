def create_file(file_name):
    try:
        open(file_name, 'x')
    except FileExistsError:
        os.remove(file_name)
        open(file_name, 'x')

def add_file(file_name, content):
    file = open(file_name, 'a')
    file.write(content)
    file.write('\n')

    file.close()

def replace_files(file_name, old_string, new_string):
    if os.path.isfile(file_name):
        with open(file_name, 'r') as file:
            file_data = file.read().replace(old_string, new_string)

        with open(file_name, 'w') as file:
            file.write(file_data)
            file.close()
    else:
        print('An error occurred')

def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print('An error occurred')

while True:
    import os

    arg = input().split('-')
    command = arg[0]

    if command == 'End':
        exit()

    file_name = arg[1]

    if command == 'Create':

        create_file(file_name)
    elif command == 'Add':
        content = arg[2]

        add_file(file_name, content)
    elif command == 'Replace':
        old_string = arg[2]
        new_string = arg[3]

        replace_files(file_name, old_string, new_string)
    elif command == 'Delete':
        delete_file(file_name)