class delObject:
    def __del__(self):
        print("Object deleted")
obiekt1 = delObject()
obiekt2 = obiekt1
del obiekt1
del obiekt2
print("To jest ostatnia linijka mojego programu")
# hermetyzacja danych ukrywanie danych
class hermetization:
    __mojaLista = []

    def dodajDoListy(self,a):
        self.__mojaLista.append(a)

obiekt3 = hermetization()
obiekt3.dodajDoListy(1)
obiekt3.dodajDoListy(2)
obiekt3._hermetization__mojaLista.append(3)
print(obiekt3._hermetization__mojaLista)
# metody klas i metody statyczne

class Person:
    height = 180

    def __init__(self,name,age):
        self.name = name
        self.age = age
    def showNameAge(self):
        print('Name: ' + self.name + "\n" + 'Age: ' + str(self.age))
    @ classmethod
    # nie potrzeba miec obiektu aby wywolac ta metode
    def getHeight(cls):
        return cls.height
    @staticmethod
    def isAdult(age):
        return age >= 18

myPerson1 = Person('John',24)
myPerson1.showNameAge()
print(Person.getHeight())
#print(Person.showNameAge())
myPerson1.getHeight()
print(Person.isAdult(10))

# własności (property), getter, setter
class Money:
    __amount = 0

    @ property
    def showAmount(self):
        return self.__amount
    @ showAmount.setter
    def showAmount(self,add):
        self.__amount += add
    @ showAmount.getter
    def showAmount(self):
        return "My money: " + str(self.__amount)

    #def addAmount(self,add):
        #self.__amount += add

kasa = Money()
print(kasa.showAmount)
kasa.showAmount = 100
print(kasa.showAmount)
kasa.showAmount = 200
print(kasa.showAmount)
kasa.showAmount = -50
print(kasa.showAmount)
# wyrazenia regularne regular expressions
import re
a = "abc"
b = "jahsdgjhgabcalksdj"
c = "abcsdsdsabcsasasa"


print(re.match(a,b))
print(re.search(a,b))
print(re.search(a,c))
print(re.findall(a,c))
d = re.sub(a,"zzz",c)
print(d)
if re.match("^do.$","dog"):
    print("MATCH")
else:
    print('DO NOT MATCH')


