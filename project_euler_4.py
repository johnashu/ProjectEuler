# Largest palindrome product
# Problem 4 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    """ Check if a number is a Palindrome """
    return int(str(num)[::-1]) == num

print(is_palindrome(9009))

def largest(n):
    """ Check for the largest n * n - digit numbers """

    n = int('9' * n) + 1

    current = 0

    for i in reversed(range(n)):
        for j in reversed(range(n)):
            if is_palindrome(i * j) and (i * j) > current:
                current = i*j
                
    return current

l = largest(3)
print(l)

