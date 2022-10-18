'''
16. Functie care primesete 2 liste de numere (numerele pot fi dublate)
Returnati numerele comune

Ex:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}
'''

def numere_dublate():
    list1 = [1, 1, 2, 3]
    list2 = [2, 2, 3, 4]
    raspuns = []
    for i in list1:
        if i in list2 and i not in raspuns:
            raspuns.append(i)
    print(raspuns)

numere_dublate()