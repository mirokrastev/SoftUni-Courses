from project.lion import Lion


class Tiger(Lion):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)

    @staticmethod
    def get_needs():
        return 45