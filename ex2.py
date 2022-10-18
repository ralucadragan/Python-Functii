# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def nr():
    a = int(input('Introduceti nr dorit: '))
    if a%2 == 0:
        print (True)
    else:
        print(False)

nr()