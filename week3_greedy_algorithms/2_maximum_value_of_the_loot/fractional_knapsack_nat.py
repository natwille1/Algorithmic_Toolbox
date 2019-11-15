# Uses python3
import sys

def takeThird(elem):
	return elem[2]

def get_optimal_value(capacity, weights, values):
	value = 0
	totals = [int(x)/int(y) for x,y in zip(values, weights)]
	together = zip(values,weights,totals)
	ordered = sorted(together, key=takeThird, reverse=True)
	for i in range(len(ordered)):
		if capacity == 0:
			return value
		if capacity / ordered[i][1] % 10:
			#items.append(ordered[i][1])
			value += ordered[i][0]
			capacity = capacity - ordered[i][1] 
		else:
			remain = float(capacity) / float(ordered[i][1])
			value += ordered[i][0] * remain
			capacity = capacity - (ordered[i][0] * remain)

	return value


if __name__ == "__main__":
    data = [1,10]
    n, capacity = data[0:2]
    #values = data[2:(2 * n + 2):2]
    #weights = data[3:(2 * n + 2):2]
    #values = [60,100,120]
    #weights = [20,50,30]
    values = [500]
    weights = [30]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
