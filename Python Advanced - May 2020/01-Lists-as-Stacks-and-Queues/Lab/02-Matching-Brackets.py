def fn():
    for i in range(len(inp)):
        if inp[i] == '(':
            stack.append(i)
        elif inp[i] == ')':
            print(inp[stack.pop():i+1])

stack = []
inp = input()
fn()