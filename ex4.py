# 4. Functie care returneaza aria dreptunghiului.

def aria (n1, n2):
    result = n1 * n2
    print('Aria dreptunghiului este:', result) # poate fi scris si return result

number1 = 5
number2 = 6
aria(number1, number2)

def aria2 ():
    a = 6
    b = 10
    return (a*b)

print('Aria dreptunghiului este:', aria2())

def aria3 (n3, n4):
    return('Aria dreptunghiului este:', n3 * n4)

print(aria(5,6))