import sys

input = sys.stdin.read()
n = int(input())
a = [int(x) for x in input().split()]

product = 0 

for i in range(n):
	if a[i] > a[product]:
		product = i 
product1 = 0 

for j in range(n):

	for j in range(i + 1, n):
		product = max(product, a[i] * a[j])

print product 