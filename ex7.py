'''
7. Functie fara return, primeste un string si printeaza pe ecran:
Nr de caractere lower case este x
Nr de caractere upper case exte y
'''

def string():
    text = input('Introduceti textul dorit: ')
    count_l_c = 0
    count_u_c = 0
    for i in text:
        if (i.islower()):
            count_l_c = count_l_c + 1
        else:
            count_u_c = count_u_c + 1
    print(f'Nr de caractere lower case este: {count_l_c}')
    print(f'Nr de caractere upper case este: {count_u_c}')

string()