'''
19. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
'''

import datetime

birth = datetime.date(1983, 11, 2)
print(f'Data nasterii este: {birth}')

today = datetime.date.today()
print(f'Data de astazi este: {today}')
# incepem sa verificam daca luna curenta == luna in care te-ai nascut
# dca lunile sunt egale veriv daca ziua a trecut deja
# sau daca luna curenta este dupa luna de nastere

if today.month == birth.month and today.day >= birth.day or today.month > birth.month:
    nextBirthdayYear = today.year + 1
else:
    nextBirthdayYear = today.year

# get curent date
# get the date of next birthday
# next birthday date is at:
    # same born month
    # same born day
    # calculate the next birthday year
nextBirthday = datetime.date(nextBirthdayYear, birth.month, birth.day)
print(f'Next birthday: {nextBirthday}')
# date of next birtday - current date

diff = nextBirthday - today
print(f'Days left for next birthday: {diff.days}')

print ('=============================================================')

from datetime import date

today = date.today()
print("Today is:", today)
print("day is:", today.day)
print("month:", today.month)
print("year:", today.year)

print('------------------------------------------')

date_birth = datetime.date(1983, 11, 2)
print(f'Data nasterii mele este: {date_birth}')
print("day of birth whas:", date_birth.day)
print("month of birth whas:", date_birth.month)
print("year of birth whas:", date_birth.year)

print('------------------------------------------')

next_birt_year = today.year + 1
next_birt = datetime.date(next_birt_year, date_birth.month, date_birth.day)
print(f'Ziua mea de anul viitor este: {next_birt}')
print("day of birth whas:", date_birth.day)
print("month of birth whas:", date_birth.month)
print("year of birth whas:", next_birt_year)

print('------------------------------------------')

if date_birth.month < today.month:
    print("Ziua ta de nastere a trecut anul acesta.")
    print('Hai sa aflam cate zile mai sunt pana la urmatoare zi de nastere:')
    print(f'Mai sunt: {next_birt - today} zile !')
elif date_birth.month == today.month:
    print("Ziua ta este in aceasta luna? Hai sa verificam daca a trecut ziua sau urmeaza!")
    if date_birth.day < today.day:
        print (f'Imi pare rau, desi ziua ta de nastere e in aceasta luna, ea a trecut! Mai e pana la anul. :( ! Mai sunt {next_birt - today} zile')
    elif date_birth.day == today.day:
        print('Azi e ziua ta ! La multi aniiii !')
    else:
        print(f'Mai sunt {date_birth.day - today.day} zile pana la ziua ta!')
else:
    print(f'Urmeaza ziua ta de nastere din acest an! Hai sa aflam cate zile mai sunt pana atunci!')
    x = datetime.date(today.year, date_birth.month, date_birth.day)
    print(f'Pana la ziua ta din acest an mai sunt: {x - today} zile. Uraaaa!!!')



