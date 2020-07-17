class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        num = args[0]

        for i in args[1:]:
            num *= i
        return num

    @staticmethod
    def divide(*args):
        num = args[0]

        for i in args[1:]:
            num /= i
        return num

    @staticmethod
    def subtract(*args):
        num = args[0]

        for i in args[1:]:
            num -= i
        return num