# zbiory(sets) wartosci podane w zbiorze sie nie powtarzaja
mojeLiczby = {1,2,3,4,5}
print(mojeLiczby)
mojTekst = set(["a","b","c"])
print(mojTekst)

mojeLiczby.add(6)
print(mojeLiczby)
mojeLiczby.add(6)
print(mojeLiczby)
mojeLiczby.remove(1)
print(mojeLiczby)
print(3 in mojeLiczby)
mojeLiczby.clear()
print(mojeLiczby)

# dzialania na zbiorach
a = {1,2,3,4,5}
b = {4,5,6,7,8}

print(a|b) # suma
print(a&b) # czesci wspolne
print(a-b)
print(b-a)
# Programowanie obiektowe OOP

class Auto:

    def __init__(self,model,age):
        self.model = model
        self.age = age
    name = 'Audi'
    color = 'Red'


    def carDetails(self,info):
        return(info + "Car name: " + self.name + "\n" + "Car color: " + self.color,
               "Car model: " + self.model + "Car age: " + str(self.age)
              )

nowyObiekt = Auto("3",4)
print(nowyObiekt.color)
print(nowyObiekt.name)
nowyObiekt2 = Auto("XF",2)
nowyObiekt2.name = 'Honda'
print(nowyObiekt2.name)
print(nowyObiekt2.carDetails("Car details: "))

# dziedziczenie klas

class Bikes(Auto):
    def funkcja(self):
        print("My bike is the best !!")

obiektBike1 = Bikes("10",7)
obiektBike1.funkcja()
obiektBike1.carDetails("asasa")
class Planes(Auto):
    def infoPlane(self):
        print("ain't got no plane!!")
obiektPlane1 = Planes("Boeing",5)
obiektPlane1.infoPlane()