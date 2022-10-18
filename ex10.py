'''
10. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
'''


def funct():
    if numar in set_numere:
        print(f'Nu am adaugat numarul in set. Acesta exista deja')
        return False
    else:
        set_numere.append(numar)
        print(f'Am afaugat numarul nou in set.')
        return True


numar = int(input('Introduceti numarul dorit: '))
set_numere = [1, 6, 9, 10, 71 , 3, 56]

funct()

print(f'Noul set de numere este: {set_numere}')

