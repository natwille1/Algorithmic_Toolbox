# Uses python3
import timeit


def calc_fib(n):

	F = range(n+1)
	F.insert(0,0)
	F.insert(1,1)

	for i in range(2, n+1):
		F[i] =F[i-1] + F[i-2]
	return F[n]

n = 10
start = timeit.default_timer()
print(calc_fib(n))
stop = timeit.default_timer()
total = stop - start
print("total time: %0.3f" % total)


# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55

