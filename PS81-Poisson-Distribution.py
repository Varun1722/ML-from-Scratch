import math
def fact(num):
	if num<2:
		return 1
	factorial = 1
	while(num>=2):
		factorial*=num
		num-=1
	return factorial

def poisson_probability(k, lam):
	"""
	Calculate the probability of observing exactly k events in a fixed interval,
	given the mean rate of events lam, using the Poisson distribution formula.
	:param k: Number of events (non-negative integer)
	:param lam: The average rate (mean) of occurrences in a fixed interval
	"""
	val = (lam**k)*(math.exp(-1*lam))/fact(k)
	return round(val,5)
