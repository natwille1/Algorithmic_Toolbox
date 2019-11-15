# Uses python3
import sys

def get_change(m):
    #write your code here
    a, b , c = 10, 5, 1
    change = 0
    while m > 0:
    	if m > a:
    		change += m / a 
    		m %= a
    	elif m > b:
    		change += m / b
    		m %= b 
    	else: 
    		change += m / c
    		break

    return change

if __name__ == '__main__':
    m = 28
    print(get_change(m))
