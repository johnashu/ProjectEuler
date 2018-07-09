# Largest palindrome product
# Problem 4 
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    """ Check if a number is a Palindrome """
    try:
        if str(num) == str(num)[::-1]:
            return True
        else:
            return False
    except ValueError:
        print("That's not a valid number, Try Again !")

print(is_palindrome(9009))

def largest(n):
    """ Check for the largest n * n - digit numbers """
    n = int('9' * n) + 1
    for i in reversed(range(n)):
        for j in reversed(range(n)):
            if is_palindrome(i * j):
                return i * j

l = largest(3)
print(l)
