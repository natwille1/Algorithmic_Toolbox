# Uses python3
import sys
import timeit

PISANO = 60

def fibonacci_partial_sum_opt(from_, to):
    F = range(to+1)
    F.insert(0,0)
    F.insert(1,1)

    for i in range(PISANO - 2):
        F[i] = (F[i-1] + F[i-2]) % 10
    #return F[n]

    from_ %= PISANO
    to %= PISANO

    if to < from_:
        to += PISANO

    result = 0 

    for i in range(from_, to + 1):
        result += F[i%PISANO]

    return result % 10 


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

if __name__ == '__main__':
   # input = sys.stdin.read();
    from_, to = 10, 200
    start = timeit.default_timer()
    print(fibonacci_partial_sum_opt(from_, to))
    end = timeit.default_timer()
    total = end - start
    print("time: %f" % total)