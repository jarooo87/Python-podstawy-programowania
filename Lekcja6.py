# obsluga wyjatkow w bloku (try except)
a = 1
b = 0
#print(a/b)
try:
    lista = []
    print(lista[0])
    print(a + "a")
    print(a/b)

    print("Ta linijka wyswietli sie gdy wyjatek jest obsluzony")
except (ZeroDivisionError, TypeError):
    print("Podzieliles przez zero albo blad typow danych")
except:
    print("Blad innego rodzaju !!")
finally:
    print("wykonuje sie nie zaleznie od bloku try except")

def divideby1(x,y):
    if y == 1:
        raise Exception("Podzieliles przez 1 to juz nie pojdzie")
    print(x/y)

try:
    divideby1(2,1)
except:
    print("Nie dziel przez 1")

# operacje na plikach (tekstowy .txt)

mojPlik = open("test.txt","a")

if mojPlik.writable():
    mojPlik.write(input("wpisz tekst:") + "\n")

mojPlik.close()

mojPlik = open("test.txt", "r")
if mojPlik.readable():
    print("To jest w pliku test.txt:")
    for i in mojPlik:
        print(i)

# slownik dictionary(kolekcja) lista to 1 element kolekcji

lista = [1,2,3,"a"]
#print(lista[3])
# slownik sklada sie z dwoch argumentow:klucz(objasnienie),wartosc
slownik = {1: "Imiona",2: "Nazwiska",4: "Wiek"}
print(slownik)
print(slownik[2])
slownik[3] = 777
print(slownik)
slownik[7] = True
print(slownik)
slownik["haha"] = 123
print(slownik)
#print(slownik[6])
print(slownik.get(6,'nie ma takiego klucza'))
for i in slownik.keys():
    print(i)
for i in slownik.values():
    print(i)
for i in slownik.items():
    print(i)
slownik.pop("haha")
print(slownik)
print(sorted(slownik))
print(slownik)
