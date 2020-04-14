shirochina = int(input())
visochina = int(input())
razmeri = shirochina * visochina
torta = 0

while razmeri > torta:
    torta_parche = input()
    if torta_parche == 'STOP':
        print(f'{razmeri - torta} pieces are left.')
        break
    torta_int = int(torta_parche)
    torta += torta_int
else:
    print(f'No more cake left! You need {torta - razmeri} pieces more.')