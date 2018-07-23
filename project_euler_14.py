# Longest Collatz sequence
# Problem 14 
# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.
import timeit
import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts))
        else:
            print('%r  %2.2f s' % (method.__name__, (te - ts)))
        return result
    return timed

 # Generator
@timeit
def generator_solution():

    nums_dict = {}

    def collatz(n):
        yield n
        while n > 1:
            n =  n * 3 + 1  if  n % 2  else  n // 2
            yield n    

    for i in range(999999, -1, -1):
        r = sum(1 for _ in collatz(i))
        if i not in nums_dict:
            nums_dict[i] = r
        # print(r)

    m = max(nums_dict.values())

    for k, v in nums_dict.items():
        if v == m:
            return k

# Memoization

from functools import lru_cache
@timeit
def memo_solution():

    @lru_cache(None)
    def coll(num):
        if num == 1:
            return 1

        if num % 2:
            return 1 + coll(num * 3 + 1)

        return 1 + coll(num / 2)

    longest = 0
    for i in range(1, 1_000_001):
        this = coll(i)
        if this > longest:
            print(i, this)
            longest = this

    return longest

    
print(generator_solution())
print(memo_solution())


