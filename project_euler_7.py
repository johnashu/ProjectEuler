# 10001st prime
# Problem 7 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# BRUTE FORCE
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
            break
    return True

c = 0
for i in range(2, 120000):
    if is_prime(i):
        c += 1
        print(c, ': ', i)
        if c == 10001:            
            print(c, ':', i)
            break

#ELEGENT

import itertools
def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def get_primes_erat(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))

res = get_primes_erat(104749)
print(len(res))
