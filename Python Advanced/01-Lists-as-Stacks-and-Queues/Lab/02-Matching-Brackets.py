def matching_brackets(string):
    s = []
    match = []
    for i in range(len(string)):
        if string[i] == '(':
            s.append(i)
        elif string[i] == ')':
            match.append(string[s.pop():i+1])
    [print("".join(i)) for i in match]

matching_brackets(input())