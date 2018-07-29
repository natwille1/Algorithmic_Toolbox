# Uses python3
import sys
import timeit

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_euc(a, b):
	current_gcd = 1
	while current_gcd != 0:
		current_gcd = a % b
		a = b 
		b = current_gcd 
	return a

def lcm_opt(a, b):
	lcm = a * b / gcd_euc(a,b)
	return lcm 


if __name__ == '__main__':
    #input = sys.stdin.read()
    #a, b = map(int, input.split())
    a = 28851538
    b = 1183019
    #a = 6 
    #b = 8 
    start = timeit.default_timer()
    print(lcm_opt(a, b))
    stop = timeit.default_timer()
    time = stop - start
    print("time: %0.4f" % time)

