import time
import random


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


    return first


def tests_ferma(list_number):
    count_tests = 100
    list_random = []
    start_time = time.time()
    for i in range(count_tests):
        list_random.append(random.randint(3, list_number//10))
    for j in range(count_tests):
        if ferma(list_random[j],list_number) != 1:
            print("Число {} составное\nПотраченное время: {}\n\n".format(list_number, time.time()-start_time))
            return
    print('Число {} возможно простое\nЗатреченное время: {}\n\n'.format(list_number, time.time()-start_time))


f = open('prime15.txt', 'r').read().split(' ')

for i in f:
    tests_ferma(int(i))
