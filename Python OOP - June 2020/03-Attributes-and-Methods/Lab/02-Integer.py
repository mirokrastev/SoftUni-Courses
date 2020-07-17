import math


class Integer:
    def __init__(self, value: int):
        self.value = value

    @staticmethod
    def roman_to_int(value):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(value)):
            if i > 0 and rom_val[value[i]] > rom_val[value[i - 1]]:
                int_val += rom_val[value[i]] - 2 * rom_val[value[i - 1]]
            else:
                int_val += rom_val[value[i]]
        return int_val

    @classmethod
    def from_float(cls, value):
        if not isinstance(value, float):
            return f'value is not a float'

        return cls(math.floor(value))

    @classmethod
    def from_roman(cls, value):
        return cls(cls.roman_to_int(value))

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return f'wrong type'

        return cls(int(value))

    def add(self, integer):
        if not isinstance(integer, Integer):
            return f'number should be an Integer instance'

        return self.value + integer.value