# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    res = 0
    for i in range(1, n + 1):
    	old = i 
    	new = i + 1
    	summands.append(i)
    	list_sum = sum(summands)
    	if list_sum < n:

    	if res < n:
    		res += i 
    		summands.append(i)
    return summands

if __name__ == '__main__':
    #input = sys.stdin.read()
   # n = int(input)
    n = 8
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x)
