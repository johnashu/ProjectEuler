# Largest prime factor
# Problem 3 
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def factor(numberToFactor, arr=list()):
    i = 2
    maximum = numberToFactor / 2 + 1
    while i < maximum:
        if numberToFactor % i == 0:
            return factor(numberToFactor/i,arr + [i])
        i += 1
    return list(set(arr + [numberToFactor]))

print(int(max(factor(600851475143)))) #6857
