import math

primes = [2]

def check_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return n

i = 3

while primes[-1] < 1000:
    if check_prime(i):
        primes.append(check_prime(i))
    i += 1
primes = primes[:-1]

for i in primes[::-1]:
    if str(i) == str(i)[::-1]:
        print i
        break
