# python3

import sys
input = sys.stdin.read()
print input 

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    i = 1
    for first in range(n):
        if n[first] > n[i]:
            i = n[first]
    ii = 1
    for second in range(n):
        if n[second] != i and n[second] > ii:
            ii = n[second]
    return i * ii


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
