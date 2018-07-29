# Uses python3
import sys
import timeit

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def get_fibonacci_opt(n):
    
    F = range(n+1)
    F.insert(0,0)
    F.insert(1,1)

    for i in range(2, n+1):
        F[i] = (F[i-1] + F[i-2]) % 10
    return F[n]


if __name__ == '__main__':
    #input = sys.stdin.read()
    #n = int(input)
    n = 331
    print(get_fibonacci_opt(n))
