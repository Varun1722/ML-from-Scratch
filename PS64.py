import numpy as np

def gini_impurity(y):
	"""
	Calculate Gini Impurity for a list of class labels.

	:param y: List of class labels
	:return: Gini Impurity rounded to three decimal places
	"""
	y=np.array(y)
	n=len(y)
	no_classes = len(np.unique(y))
	classes = [0]*no_classes
	for i in range(n):
		classes[y[i]]+=1
	sum_sq=0
	for values in classes:
		sum_sq += values**2
	return round(1-(sum_sq/(n**2)),3)
