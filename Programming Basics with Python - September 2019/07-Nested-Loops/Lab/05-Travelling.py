class Programa:
    def __init__(self):
        self.inputer()

    def destination(self, inp, money_needed, pari):
        while True:
            money_saved = float(input())
            pari += money_saved
            if pari >= money_needed:
                print(f'Going to {inp}!')
                break

    def inputer(self):
        while True:
            inp = input()
            if inp == 'End':
                exit()
            money_needed = float(input())
            pari = 0
            self.destination(inp, money_needed, pari)


if __name__ == '__main__':
    Programa()