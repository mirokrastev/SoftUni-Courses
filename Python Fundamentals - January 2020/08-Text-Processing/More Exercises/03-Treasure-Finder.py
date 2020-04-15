sequence_nums = list(map(lambda x: int(x), input().split(' ')))

while True:
    inp_raw = bytearray(input(), 'utf-8')
    if inp_raw.decode() == 'find':
        exit()
    counter = 0
    for i in range(len(inp_raw)):
        if counter > len(sequence_nums) - 1:
            counter = 0
        inp_raw[i] -= sequence_nums[counter]
        counter += 1
    inp_raw = inp_raw.decode()
    counter = 0
    material = bytearray('', 'utf-8')
    koordinati = bytearray('', 'utf-8')
    while counter < len(inp_raw):
        if inp_raw[counter] == '&':
            counter += 1
            while inp_raw[counter] != '&':
                material.append(ord(inp_raw[counter]))
                counter += 1
            counter += 1
        elif inp_raw[counter] == '<':
            counter += 1
            while inp_raw[counter] != '>':
                koordinati.append(ord(inp_raw[counter]))
                counter += 1
            counter += 1
        counter += 1
    print(f'Found {material.decode()} at {koordinati.decode()}')