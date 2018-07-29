# python3

import sys
import numpy as np
import random 
import timeit

#inp = [7,4,5,6]

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0 
    for first in range(n):
        for second in range(first +1, n):
            max_product = max(max_product, numbers[first] * numbers[second])
    return max_product


def max_pairwise_product_fast(numbers):
    n = len(numbers)
    i = -1
    for first in range(n):
        if i == -1 or numbers[first] > numbers[i]:
            i = first
    ii = -1
    for second in range(n):
        if second != i and (ii == -1 or numbers[second] > numbers[ii]):
            ii = second
    return numbers[i] * numbers[ii]

def stress_test(o, p):
    while True:
        n = random.randint(2, o)
        m = np.random.randint(n, size=p)
        print m 
        result1 = max_pairwise_product(m)
        result2 = max_pairwise_product_fast(m)
        if result1 == result2:
            print("Ok")
            #print result1, result2
        else:
            print("test case failed: %s %s" % (result1, result2))
            return





if __name__ == '__main__':
   # print(max_pairwise_product(inp))
    print(stress_test(9, 5))

