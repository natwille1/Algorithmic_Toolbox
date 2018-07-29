# Uses python3
import sys
import timeit

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def fibonacci_partial_sum_opt(from_, to):
	if from_ != to:
		start = fibonacci_opt(from_)
		end = calculate_sum(to)
		print start, end
		total = end - start 
	else:
		total = fibonacci_opt(to)
		print total
	return total % 10 

def fibonacci_opt(n):
    F = range(n+1)
    F.insert(0,0)
    F.insert(1,1)

    for i in range(2, n+1):
        F[i] = (F[i-1] + F[i-2]) 
    return F[n]

def calculate_sum(n):
    S = fibonacci_opt(n + 2) - 1
    return S 


if __name__ == '__main__':
   # input = sys.stdin.read();
    from_, to = 10, 200
    start = timeit.default_timer()
    print(fibonacci_partial_sum_opt(from_, to))
    end = timeit.default_timer()
    total = end - start
    print("time: %f" % total)