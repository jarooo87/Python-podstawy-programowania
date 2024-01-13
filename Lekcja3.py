# petla obiektowa for
mojaLista = ['Andrzej','Tomek', 'Adam', 'Mariusz']
licznik = 0
while licznik < len(mojaLista):
    print(mojaLista[licznik])
    licznik += 1

for a in mojaLista:
    print(a)
for b in range(10):
    print(b)

#for i in range(3):
    #login = input('Login:')
    #password = input(('Password:'))
    #if login == 'admin' and password == 'abc':
       # print('Authorization at attempt', i+1)
# funkcje

def mojaFunkcja():
    print('To jest moja funkcja')
    print('Cialo funkcji')

mojaFunkcja()

def funkcjaLiczbowa(liczba1):
    print(liczba1 + 1)

funkcjaLiczbowa(3)
funkcjaLiczbowa(1)

def funkcjaDwaArgumenty(l1,l2):
    print(l1 + l2)

funkcjaDwaArgumenty(3,2)

def print_label(name):
    print('Name and course:')
    print('Name:', name)
    print('Course: English')

amount = int(input('Number of students:'))
for i in range(amount):
    name = input('Students name:')
    print_label(name)
print('Goodbye!')

def myFunction(z):
    return z + z
dodawanie = myFunction(2)
print(dodawanie)

def get_result(score):
    if score >= 50 and score < 100:
        result = " 3rd certificate"
    elif score >= 100 and score < 200:
        result = "2nd certificate"
    elif score >= 200:
        result = "1st certificate"
    else:
        result = "I'm sorry ;)"
    return result

name = input('Student name:')
score = int(input('Your score:'))
result = get_result(score)
print(name, '-', result)
if result == "1st certificate":
    print(' You received voucher to McDonalds')

def average_grade(name):
    grade = input('Grade (off to exit):')
    summa = 0
    total = 0
    while grade != 'off':
        summa += int(grade)
        total += 1
        grade = input('Grade (off to exit):')
    average = summa/total
    return average
name = input('Student name:')
average = average_grade(name)
print(average)






