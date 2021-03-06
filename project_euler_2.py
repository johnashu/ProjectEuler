# Even Fibonacci numbers
# Problem 2 
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fib(n):
 a, b = 1, 1
 for i in range(n-1):
  a, b = b, a + b
 return a
c = 0
for i in range(2, 100):
    x = fib(i)
    if x < 4000000 and x%2 == 0:
        print(x)
        c += x 
print(c) #4613732
