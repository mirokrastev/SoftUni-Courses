from collections import deque
import math


def calculate(symbol):
    if symbol in {'*', '+', '-', '/'}:
        result = str(eval(symbol.join(numbers)))
        numbers.clear()
        numbers.append(result)
        return

    numbers.append(symbol)


inp = deque(input().split())
numbers = deque()

while inp:
    calculate(inp.popleft())

print(int(float(numbers[0])))