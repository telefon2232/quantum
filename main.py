import random
import time
def IsPrime(n):
   d = 2
   while d * d <= n and n % d != 0:
       d += 1
   return d * d > n

def primFerma(a,n):
    if a**(n-1) % n == 1:  # для любого a, которое не делится на n.
        print("правдоподобно простое")
    else:
        print("составное")



def miller_rabin(n, k=5): # miller-rabin
    from random import randint
    if n < 2: return "Составное"
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0: return "Простое"
    s, d = 0, n-1
    while d % 2 == 0:
        s, d = s+1, d/2
        s=int(s)
        d = int(d)
    for i in range(k):
        x = pow(randint(2, n-1), d, n)
        if x == 1 or x == n-1: continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1: return 'Составное'
            if x == n-1: break
        else: return "Составное"
    return "Возможно простое"

start_time = time.time()
primFerma(10,1100101)
print("Время на алгоритм Ферма %s seconds ---" % (time.time() - start_time))
print('----------------------------------------')
second_time = time.time()
print(miller_rabin(1100101, 1111199))
print("Время на алгоритм Миллер-Рабина %s seconds ---" % (time.time() - second_time))
print('----------------------------------------')
last_time = time.time()
print(IsPrime(11001021))
print('Време обычного алгоритма %s ---'% (time.time()-last_time))