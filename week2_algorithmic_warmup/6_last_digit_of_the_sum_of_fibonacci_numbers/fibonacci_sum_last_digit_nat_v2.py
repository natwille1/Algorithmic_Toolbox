# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fibonacci_opt(n):
    F = range(n+1)
    F.insert(0,0)
    F.insert(1,1)

    for i in range(2, n+1):
        F[i] = (F[i-1] + F[i-2]) % 10 
    return F[n]

def calculate_sum(n):
    S = fibonacci_opt(n + 2) - 1
    return S 

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

def get_fibonacci_huge_opt(n,m):

    period = pisano_period(m)
    print period
    result = get_fibonacci_opt(n % period, m)

    return result 


if __name__ == '__main__':
    n = 3
    print(calculate_sum(n))
