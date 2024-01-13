#nadpisywanie funkcji
def dodawanie(z):
    print(z + 1)
dodawanie(3)

def dodawanie(z,x):
    print(z + x)

dodawanie(2,6)

def funkcja1 (a):
    return a * a
print(funkcja1(4))

def funkcja2(funkcja1,a):
    return funkcja1(a) * a
print(funkcja2(funkcja1,3))
# rekurencja
# silnia 4 = 4*3*2*1
def silnia(a):
    if a <= 1:
        return 1
    else:
        return a * silnia(a - 1)

print(silnia(5))
# modul losowy
#import random
#print(random.randint(1,10))
#from random import randint
#print(randint(1,5))
from random import *
print(randint(5,8))

#name = input("Give me your name:(off to exit)")
#while name != 'off':
    #teamRnd = randint(1,3)
    #print(name, 'team',teamRnd)
    #name = input("Give me your name:(off to exit)")

#total = int(input("The number of teams:"))
#t1 = randint(1,total)
#t2 = randint(1,total)
#print('Team ', t1, 'plays with', t2)

# modul matematyczny z ang. math
import math
a = 2.12
print(round(a))
print(math.ceil(a))
print(math.floor(a))
print(math.pow(a,2))
print(math.sqrt(a))
from time import *

start = time()
print(start)
sleep(5)
end = time()
print(end)
#total = round(end) - round(start)
total = round(end-start,3)
print(total)

stopwatch = input('1 - start, 0 - stop:')
while stopwatch != '0':
    if stopwatch == '1':
        poczatek = time()
    else:
        print("Action not found")
    stopwatch = input('1 - start, 0 - stop:')
koniec = time()
totalTime = koniec - poczatek
print("Czas", round(totalTime,2), 'sekund')


