# Uses python3
from sys import stdin
import timeit

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

def fibonacci_sum_squares_opt(n, m):
    total = get_fibonacci_huge_opt(n, m) * get_fibonacci_huge_opt(n+1, m)
    return total % 10



def get_fibonacci_opt(n, m):
    F = range(n+1)
    F.insert(0,0)
    F.insert(1,1)

    for i in range(2, n+1):
        F[i] = (F[i-1] + F[i-2]) % m
    return F[n]

def pisano_period(m):
    steps = 1 
    previous = 1 
    current = 1 
    while not (previous == 0 and current == 1):
        temp = (previous + current) % m 
       # print "previous: %i, current: %i, temp: %i" % (previous, current, temp) 
        previous = current
        current = temp 
        steps += 1 
    return steps  

def get_fibonacci_huge_opt(n, m):

    period = pisano_period(m)
    print period
    result = get_fibonacci_opt(n % period, m)

    return result 

if __name__ == '__main__':
    #n = int(stdin.read())
    n = 1234567890
    m = 10
    start = timeit.default_timer()
    print(fibonacci_sum_squares_opt(n, m))
    end = timeit.default_timer()
    total = end - start
    print("time: %f" % total)
