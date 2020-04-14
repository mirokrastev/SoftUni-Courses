broi_dni = float(input())
broi_sladkari = float(input())
broi_torti = float(input())
broi_gofreti = float(input())
broi_palachinki = float(input())

torti = broi_torti * 45
gofreti = broi_gofreti * 5.80
palachinki = broi_palachinki * 3.20
obshta_suma_chovek = (torti + gofreti + palachinki) * broi_sladkari
obshta_suma = obshta_suma_chovek * broi_dni
suma_razhodi = obshta_suma - 1/8 * obshta_suma

print(f'{suma_razhodi:.2f}')