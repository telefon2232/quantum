import random
import time
import main


def ferma(a, x, p):
    final = []
    bin_x = list(bin(x)[2:])
    data = [a]

    for i in range(len(bin_x)-1):
        data.append((data[i] ** 2) % p)
    data.reverse()

    for i in range(len(bin_x)):
        if bin_x[i] == '1':
            final.append(data[i])

    first = final[0]
    for i in range(len(final)-1):
        first = (first*final[i+1]) % p
    return first


def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    elif a <= b:
        return gcd(a, b % a)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)



def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n






def create_big_prime():
    count = 0
    list_prime = []
    start_time = time.time()
    while count != 2:
        z = random.randint(2**1024, 2**2048)
        if main.ferma(5, z) == 1:
            count_tests = 100
            list_random = []
            start_time = time.time()
            for i in range(count_tests):
                list_random.append(random.randint(3, z // 10))
            for j in range(count_tests):
                if main.ferma(list_random[j], z) != 1:
                    continue


            print(z)
            count += 1
            list_prime.append(z)
    print('Затреченное время: {}'.format(time.time()-start_time))
    return list_prime


def encrypter(q, p):
    n = q * p  # Их перемножение
    e = 3
    f_n = (p - 1) * (q - 1)  # Вычисление фи от n

    # Эта функция ищет взаимнопростое число с фи от n
    for i in range(4, 100):
        if gcd(i, f_n) == 1:
            e = i
            break

    d = (mulinv(e, f_n))  # испольуем расширенные алгоритм евклида

    check = (d * e) % f_n
    if check != 1:
        exit(1)

    c = (m ** e) % n  # По формуле шифруем
    return c, d, n


def decrypter(c, d, n):
    return ferma(c, d, n)  # По тесту ферма дешифруем

#q = 5720186828255166492955324855446305161336783196837190313323769969984619286314892718143587099967066632661154671741215978206536459810555884272204261432255220686919142094220368078803030011052105279953116299157459785463119814097876788924201203685559314511986849197154184820672711620439201309792438254924548671361676797939813024902252800781933824359663229863573490459146644549997724813592411381187042142361251272710389772783784205425908538499052537667823464063979616023480994523562882295049936953713963776753229627287525501672745541225433366211291737209930805876472399075279196126516304019847933946992207654441896000487521
#p = 15015012064889801100506764681306715846840200455569575043840384935703672101595713451001788301528658822086370498632171819572419955967130762326585390882715893260164530278564784136459765066779867445052809506213132803666770650612178520248577381616585408950690333632241126973505156298648366581558447836764226178627297961196475754287566104886085612103513081377692627312361931316855473127217162286602971490358248666528858910224397228159661898445572909344769458476938035810572113625298287918267550045527587541319892804018326199642312428585718683988516254368045853090656184132483166341429296065475742401929369871087600902414927

p,q = create_big_prime()  # Если нам нужны новые огромные простые числа


m = 1243  # Наше сообщение

c, d, n = encrypter(q, p)

print(decrypter(c, d, n))  # Выводим расшифрованное сообщение



