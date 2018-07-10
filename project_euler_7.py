# 10001st prime
# Problem 7 
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?


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
