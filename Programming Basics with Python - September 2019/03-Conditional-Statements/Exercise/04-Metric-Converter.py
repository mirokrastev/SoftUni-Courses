chislo = float(input())
merna_edinica = input()
kum_merna_edinica = input()

if merna_edinica == 'm':
    if kum_merna_edinica == 'cm':
        sum = chislo * 100
        print(f'{sum:.3f}')
    elif kum_merna_edinica == 'mm':
        sum = chislo * 1000
        print(f'{sum:.3f}')
elif merna_edinica == 'cm':
    if kum_merna_edinica == 'm':
        sum = chislo * 0.01
        print(f'{sum:.3f}')
    elif kum_merna_edinica == 'mm':
        sum = chislo * 10
        print(f'{sum:.3f}')
elif merna_edinica == 'mm':
    if kum_merna_edinica == 'm':
        sum = chislo * 0.001
        print(f'{sum:.3f}')
    elif kum_merna_edinica == 'cm':
        sum = chislo * 0.1
        print(f'{sum:.3f}')