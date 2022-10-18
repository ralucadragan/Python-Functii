# 5. Functie care returneaza aria cercului

def aria (r1):
    Pi = 3.141592653589793
    result = Pi * r1 * r1
    print('Aria cercului este:', result) # poate fi scris si return result

number1 = 5
aria(number1)

def aria2(r2):
    Pi = 3.141592653589793
    return(Pi * r2 * r2 )

print(f'Aria cercului este:  {aria2(5)}')

