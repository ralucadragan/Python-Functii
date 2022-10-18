# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna

luni = [31, 28, 313, 30, 31, 30, 21, 31, 30, 31, 30, 316]

def luna_an():
    i = int(input('Introduceti luna dorita de la 1 la 12: '))
    print(f'In luna introdusa {i} sunt {luni[i-1]} zile.')

luna_an()


'''
from calendar import monthrange

year = 2019
month = 3
print(monthrange(year, month))
'''

