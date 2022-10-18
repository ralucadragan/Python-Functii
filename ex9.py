'''
9. Functie care nu returneaza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale.
'''


def numere():
    if numar1 > numar2:
        print(f'Primul numar {numar1} este mai mare decat al doilea numar {numar2}')
    elif numar1 < numar2:
        print(f'Al doilea numar {numar2} este mai mare decat primul numar {numar1}')
    else:
        print('Numerele sunt egale')

numar1 = int(input('Introduceti primul numar: '))
numar2 = int(input('Introduceti al doilea numar: '))
numere()

