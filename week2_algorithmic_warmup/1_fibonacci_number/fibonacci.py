# Uses python3
import timeit



def calc_fib(n):
	start = timeit.default_time()
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
    stop = timeit.default_time()
    total = stop - start

	print("runtime: %s" % (total))

n = int(input())
print(calc_fib(n))

