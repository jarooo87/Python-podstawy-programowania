# lista, slownik, krotka(Tuple)
# jej elementow nie mozna zmieniac
lista = []
slownik = {}
krotka = (1,2,3,4,5,6,7,"a","b")
print(krotka[0])
print(krotka)
print(krotka.count(3))
# count zlicza ilosc wystapien elementu
print(krotka.index(7))
# wycinki
print(krotka[0:3])
print(krotka[0:7:2])
print(krotka[::-1])
# formatowanie typu tekstowego String
args = ["imie", 22]
#zdanie = "Podaj swoje {0} i wpisz swoj wiek: {1}".format(args[0],args[1])
zdanie = f"Podaj swoje {args[0]} i wpisz swoj wiek: {args[1]}"
print(zdanie)
print("/".join(["a","b","c"]))
print("Ala ma kota".replace("kota","psa"))
print("Ala ma kota".startswith("ma"))
print("Ala ma kota".endswith("Ala"))
print("a" in "Ala ma kota")
print("Ala ma kota".upper())
print("Ala ma kota".lower())
print("ala ma kota".capitalize())
# funkcje listy
lista2 = [10,20,30,41]

if all([i % 2 == 0 for i in lista2]):
    print("wszystkie liczby sa parzyste")
if any([i % 2 == 0 for i in lista2]):
    print("Przynajmniej jedna liczba jest parzysta")

for i in lista2:
    print(i)
for i in enumerate(lista2):
    print(i)
# lambda tzw funkcja anonimowa
print("-------LAMBDA-------")

def mnozenie(a):
    return a * 2
print(mnozenie(3))
mnozenie2 = lambda a:a * 2
print(mnozenie2(5))

dodawanie = lambda a,b,c: a+b+c
print(dodawanie(1,2,3))
# mapa i filtr

mojaLista = [1,2,3,4,5,6,7]
listaString = ["a","b"]

def jakasFunkcja(a):
    return a + "z"

mapa = map(jakasFunkcja,listaString)
print(list(mapa))

funkcjaFiltr = filter(lambda x:x % 2 == 0,mojaLista)
print(list(funkcjaFiltr))

# generatory (yield)

def funkcjaGeneratora():
    i = 0
    while i < 5:
        yield i
        i += 1
print((funkcjaGeneratora()))

for i in funkcjaGeneratora():
    print(i)





