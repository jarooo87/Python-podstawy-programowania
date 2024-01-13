# zagniezdzanie if
wzrost = 180
waga = 90

if wzrost >= 180:
    if waga >= 90:
        print('wzrost i waga sa zgodne')
# operatory logiczne and i or
# and 2 awrunki musza byc true
if wzrost >= 180 and waga > 90:
    print('wzrost i waga ok')
# or jeden warunek musi byc true
if wzrost >= 190 or waga > 90:
    print('wzrost ok waga nie jest zgodna')
else:
    print('waga i wzrost sie nie zgadzaja')
# petla while z ang.podczas
licznik = 0
# nieskonczona petla while
while licznik < 3:
    print(licznik)
    licznik = licznik + 1
    # 4 spacje lub to cialo petli
print('koniec petli while ten kod jest poza petla')
while True:
    print(licznik)
    licznik += 1
    if licznik >= 10:
        break
print('koniec')
# break przerywa/zatrzymuje petle while
# gra zgadywanka z komputerem
from random import randint
liczbaWylosowanaPrzezKomputer = randint(1,10)
mojaOdpowiedz = 0
i = 0
print('Zgadnij liczbe w przedziale 1-10')
#while mojaOdpowiedz != liczbaWylosowanaPrzezKomputer:
 #   i += 1
  #  mojaOdpowiedz = int(input('Podaj liczbe:'))
   # if mojaOdpowiedz>liczbaWylosowanaPrzezKomputer:
    #    print("wylosowana liczba jest mniejsza od Twojej")
    #elif mojaOdpowiedz<liczbaWylosowanaPrzezKomputer:
      #  print("wylosowana liczba jest wieksza od Twojej liczby")
print('Udalo Ci sie zgadnac za:', i, 'razem')
# lista przetrzymuje wieksza ilosc danych
liczba = 3
imie = "Jan"

mojaLista = [1, 4, 9, 'Jan', 'Marek', 999, 3.14]
print(mojaLista)
print(mojaLista[5])
nazwisko = "Nowak"
print(nazwisko[0])
mojaLista += ['imie','nazwisko','wiek']
print(mojaLista)
print(mojaLista * 2)
print(mojaLista)
# wyswietlanie iloscie elementow w liscie funkcja len z ang. lenght
print("Długosc listy", len(mojaLista))
# stawiajac kropke po nazwie zmiennej mamy dostep do jej metod
mojaLista.append('ABC')
print(mojaLista)
mojaLista.insert(0,777)
print(mojaLista)
mojaLista.remove(777)
print(mojaLista)

lista2 = [9, 66, 53, 3, 41]
print("minimalna wartosc", min(lista2))
print("maksymalna wartosc", max(lista2))
print(lista2)
lista2.sort()
print(lista2)
lista2.reverse()
print(lista2)
lista2.clear()
print(lista2)

