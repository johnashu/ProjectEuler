# Lattice paths
# Problem 15 
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

import time
 
def route_num(matrix):
    t = [1] * matrix
    for i in range(matrix):
        for j in range(i):
            t[j] = t[j] + t[ j - 1]
        t[i] = 2 * t[i - 1]
    return t[matrix - 1]
 
start = time.time()
n = route_num(20)
elapsed = (time.time() - start)
print("{} found in {} seconds".format(n, elapsed))
