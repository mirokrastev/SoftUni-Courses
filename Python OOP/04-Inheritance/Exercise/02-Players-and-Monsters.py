class Hero:
    def __init__(self, username, level):
        self.username = username
        self.level = level
        self.type = 'Hero'

    def __repr__(self):
        return f'{self.username} of type {self.type} has level {self.level}'

class Elf(Hero):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'Elf'

class MuseElf(Elf):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'MuseElf'

class Wizard(Hero):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'Wizard'

class DarkWizard(Wizard):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'DarkWizard'

class SoulMaster(DarkWizard):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'SoulMaster'

class Knight(Hero):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'Knight'

class DarkKnight(Knight):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'DarkKnight'

class BladeKnight(DarkKnight):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.type = 'BladeKnight'