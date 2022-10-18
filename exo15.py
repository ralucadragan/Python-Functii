'''
15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
Ex: daca dam nr 3
Suma va fi 6 (0+1+2+3)
'''

def s():
    a = int(input('Introduceti numarul dorit: '))
    sum = 0
    for a in range(0,a+1):
        print(a)
        sum = sum + a
    print(f'Suma tuturor numerelor pana la {a} este: {sum}')

s()
