def operate(operator, *args):
    result = 0

    if operator == "+":
        for arg in args:
            result += arg
    elif operator == "-":
        for arg in args:
            result -= arg
    elif operator == "*":
        result = 1
        for arg in args:
            result *= arg
    elif operator == "/":
        result = 1
        for arg in args:
            result /= arg

    return result