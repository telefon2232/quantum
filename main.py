import time
import random
import math


def ferma(a, x):
    final = []
    bin_x = list(bin(x-1)[2:])
    data = [a]

    for i in range(len(bin_x)-1):
        data.append((data[i] ** 2) % x)
    data.reverse()

    for i in range(len(bin_x)):
        if bin_x[i] == '1':
            final.append(data[i])

    first = final[0]
    for i in range(len(final)-1):
        first = (first*final[i+1]) % x
    if first != 1:
        first = 0
    return first


def sqrt_algo(x):
    start_time = time.time()
    if x <= 1:
        return "{}; {}; 0\n".format(x, time.time() - start_time)
    if x <= 3:
        return '{}; {}; 1\n'.format(x, time.time() - start_time)
    if x % 2 == 0:
        return "{}; {}; 0\n".format(x, time.time() - start_time)

    for i in range(3, round(math.sqrt(x))//2,2):

        if x % i == 0:
            return "{}; {}; 0\n".format(x, time.time() - start_time)
    return '{}; {}; 1\n'.format(x, time.time()-start_time)


def tests_ferma(list_number):
    count_tests = 100
    list_random = []
    start_time = time.time()
    for i in range(count_tests):
        list_random.append(random.randint(3, list_number//10))
    for j in range(count_tests):
        if ferma(list_random[j], list_number) != 1:
            return "{}; {}; 0\n".format(list_number, time.time()-start_time)

    return '{}; {}; 1\n'.format(list_number, time.time()-start_time)



f = open('not_prime9.txt', 'r').read().split(' ')
for i in f:
    i = int(i)
    with open('not_prime9.csv','a') as file:
        file.write(sqrt_algo(i) + tests_ferma(i) +'\n')
