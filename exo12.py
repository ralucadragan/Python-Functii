'''
12. Functie calculator care sa returneze 4 valori
Suma, diferenta, inmultirea, impartirea a 2 numere

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
'''

def calculator(n1, n2):
    a = n1 + n2
    print ('Suma:', a)
    b = n1 - n2
    print ('Diferenta:', b)
    c = n1 * n2
    print ('Inmultirea:', c)
    d = n1 / n2
    print('Impartirea:', d)

calculator (10, 2)