nums = int(input())

for i in range(nums):
    inp_raw = input()
    name = ''
    age = ''
    counter = 0
    while counter < len(inp_raw):
        if inp_raw[counter] == '@':
            counter += 1
            while inp_raw[counter] != '|':
                name += inp_raw[counter]
                counter += 1
        elif inp_raw[counter] == '#':
            counter += 1
            while inp_raw[counter] != '*':
                age += inp_raw[counter]
                counter += 1
        counter += 1
    print(f'{name} is {age} years old.')