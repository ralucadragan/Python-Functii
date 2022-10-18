# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive.

lista = [3, 9, 10, -9, 6, -45, 3, -3]

def funct():
    numere_pozitive = []
    for i in lista:
        if i >= 0:
            numere_pozitive.append(i)
    #print(f'Lista cu numere pozitive este: {numere_pozitive}')
    return (numere_pozitive)

print(f'Lista cu numere pozitive este: {funct()}')
