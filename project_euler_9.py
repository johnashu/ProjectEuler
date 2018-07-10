# Special Pythagorean triplet
# Problem 9 
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# n = 1000

def Pythagorean_Triplets(n):
    """ A generator to calculate Pythagorean Triplets and the product of Triplets for number entered """
    for num in range(1, n):
        for dig in range(num, n - num):
            i = n - num - dig
            if num * num + dig * dig == i * i:
                yield "\n\tSum of Triples: {}\n\tTriplet: {}, {}, {}\n\tProduct: {}".format(n, num, dig, i, num * dig * i)

r = Pythagorean_Triplets(12)
for x in r:
    print(x)
