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

if __name__ == '__main__':

   # input = sys.stdin.read()
    # n = int(input)
    n = 327305
    start = timeit.default_timer()
    print(get_fibonacci_last_digit_naive(n))
    stop = timeit.default_timer()
    total = stop - start
    print("total time: %0.3f" % total)
