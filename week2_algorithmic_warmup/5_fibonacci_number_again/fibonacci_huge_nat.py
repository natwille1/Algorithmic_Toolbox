# Uses python3
import sys
import timeit 

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

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

def get_fibonacci_huge_opt(n,m):

    period = pisano_period(m)
    print period
    result = get_fibonacci_opt(n % period, m)

    return result 


if __name__ == '__main__':
    #input = sys.stdin.read();
    #n, m = map(int, input.split())
    n = 2816213588
    m = 239
    start = timeit.default_timer()
    #print(pisano_period(m))
    print(get_fibonacci_huge_opt(n,m))
    stop = timeit.default_timer()
    total = stop - start
    print("time %f" % total)
