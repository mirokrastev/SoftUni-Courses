inp = input().split(', ')
def proverka(a):
    for i in a:
        if i[::-1] == i:
            print('True')
        else:
            print('False')
proverka(inp)