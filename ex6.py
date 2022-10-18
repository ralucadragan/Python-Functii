# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

def string ():
    caracer = 'b'
    text = input('Introduceti textul dorit: ')
    if caracer in text:
        print(True)
    else:
        print(False)

string()

def string1(caracter):
    text = input('Introduceti textul dorit: ')
    if caracter in text:
        return True
    else:
        return False

print(string1('b'))

