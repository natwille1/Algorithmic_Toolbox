# Uses python3
import sys

def get_change(m):
    #write your code here
    values = [10,5,1]
    change = 0
    while m > 0:
    	for i in values:
    		while m/i % 10:
    		#change.append(i)
    			change += 1 
    			m = m - i 
    			print m, i
    		else:
    			continue 

    return change

if __name__ == '__main__':
    m = 28
    print(get_change(m))
