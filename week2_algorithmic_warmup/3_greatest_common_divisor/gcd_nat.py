# Uses python3
import sys
import timeit 

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
    #	print d 
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_euc(a, b):
	current_gcd = 1
	while current_gcd != 0:
		current_gcd = a % b
		a = b 
		b = current_gcd 
	return a


if __name__ == "__main__":
   # input = sys.stdin.read()
   # a, b = map(int, input.split())
    a = 28851538
    b = 1183019
    start1 = timeit.default_timer()
    print(gcd_naive(a, b))
    stop1 = timeit.default_timer()
    total1 = stop1-start1
    start2 = timeit.default_timer()
    print(gcd_euc(a,b))
    stop2 = timeit.default_timer()
    total2 = stop2 - start2
    print("naive: %0.3f. euc: % 0.3f" % (total1, total2))
