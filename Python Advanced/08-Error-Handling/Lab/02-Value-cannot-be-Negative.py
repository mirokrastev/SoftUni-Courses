class ValueCannotBeNegative(Exception):
    """
    Raises an error if the number is negative
    """

for i in range(5):
    arg = int(input())
    if arg < 0:
        raise ValueCannotBeNegative