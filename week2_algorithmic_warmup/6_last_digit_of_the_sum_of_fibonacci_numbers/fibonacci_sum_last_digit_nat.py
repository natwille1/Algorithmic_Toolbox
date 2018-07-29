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



if __name__ == '__main__':
    n = 3
    print(calculate_sum(n))
