'''
17. Functie care sa aplice o reducere de pret
Daca produsul costa 100 lei si aplicam reducere de 10%
Pretul va fi 90
Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
'''

def reducere():
    price = 100
    if price ==100:
        price *= 0.9
    print(price)

reducere()