inp = input()
result = ''
i = 0
var = ''

while i < len(inp):
    if inp[i].isnumeric():
        try:
            if inp[i+1].isnumeric():
                nums = f'{inp[i]}{inp[i+1]}'
                result += var * int(nums)
                var = ''
                i += 2
                continue
        except:
            pass
        result += var * int(inp[i])
        var = ''
        i += 1
    else:
        var += inp[i].upper()
        i += 1
print(f'Unique symbols used: {len(set(result))}')
print(result)