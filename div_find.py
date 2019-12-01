import math
import random
from RSA import ferma

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    elif a <= b:
        return gcd(a, b % a)

def last(count,n):
    z = list(range(2, count))
    for i in range(2, count):
        f = random.randint(0, count-4)
        s = random.randint(0, count-4)
        z[f], z[s] = z[s], z[f]

    for i in range(count-2):
        if gcd(z[i],n) != 1:
            continue
        R = 1
        while ferma(z[i], R, n) != 1:
            R += 1
     #   print('HI')
        if R % 2 == 0:
            b = ferma(z[i],R//2,n)
            k1 = gcd(b+1,n)
            k2 = gcd(b-1,n)
            if n % k1 == 0 and k1 != n and k1 != 1:
                return k1
            if n % k2 == 0 and k2 != n and k2 != 1:
                return k2



def check_prime(N):
    if N % 2 == 0:
        return 2
    log = math.ceil(math.log2(N))
    for i in range(3, log, 2):
        l = 2
        r = N
        while r - l > 1:
            mid = (l + r) // 2

            res = mid ** i

            if res == -1 or  res > N:
                r = mid - 1

            else:
                l = mid
        if l**i ==N:
            print('Число найдено! {}'.format(l))
            return -1
        if r**i == N:
            print('Число найдено! {}'.format(r))
            return -1







#N = 17**5

#check_prime(N)

for i in range(3,1000):
    if check_prime(i)==-1:
        continue
    print(i,")",last(1002,i))
