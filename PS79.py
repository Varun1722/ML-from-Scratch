import math

def binomial_probability(n, k, p):
	"""
    Calculate the probability of achieving exactly k successes in n independent Bernoulli trials,
    each with probability p of success, using the Binomial distribution formula.
    """
	# Your code here
	probability = p**k * (1-p)**(n-k)
	fact=1
	for i in range(min(k,n-k)):
		fact = (fact * (n-i))/(i+1)

	probability = probability * fact
	return round(probability, 5)
