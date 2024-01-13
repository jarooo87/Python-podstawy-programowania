#threads, multithreading (watek,wielowatkowosc)

import threading
import time
'''

def funkcja1():
    print("Tu działa funkcja 1")
    time.sleep(2)
def funkcja2():
    print("Tu działa funkcja 2")
    time.sleep(3)
def funkcja3():
    print("Tu działa funkcja 3")
    time.sleep(4)

#funkcja1()
#funkcja2()
#funkcja3()

f1 = threading.Thread(target=funkcja1,args=())
f1.start()
f2 = threading.Thread(target=funkcja2,args=())
f2.start()
f3 = threading.Thread(target=funkcja3,args=())
f3.start()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

f1.join()
f2.join()
f3.join()

'''
# daemon thread - odpalony w tle
'''
def licznik():
    licznik = 0
    while True:
        time.sleep(1)
        licznik +=1
        print(licznik)

l1 = threading.Thread(target=licznik,daemon=True)
l1.start()
a = input("Wpisz cokolwiek:")
'''
# multiprocessing odpalanie na roznych rdzeniach procka
from multiprocessing import Process,cpu_count

def licznik2(a):
    licznik2=0
    while licznik2 < a:
        licznik2 +=1
def main():
    l2 = Process(target=licznik2,args=(500000,))
    l2.start()
    l3 = Process(target=licznik2,args=(500000,))
    l3.start()
    l4 = Process(target=licznik2,args=(250000,))
    l4.start()
    l5 = Process(target=licznik2,args=(250000,))
    l5.start()

    print("Counted in time:", time.perf_counter())

if __name__ == '__main__':
    main()

print(cpu_count())




