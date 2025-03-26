import math

def softmax(scores: list[float]) -> list[float]:
	
	probabilities = []
	total_sum = 0
	for x in scores:
		total_sum += math.exp(x)
	for x in scores:
		probabilities.append(math.exp(x)/total_sum)
	return probabilities
