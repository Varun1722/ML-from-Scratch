import numpy as np
def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	n=len(a[0])
	m=len(b)
	if n!=m:
		return -1

	c=[0]*len(a)
	for i in range(len(a)):
		c[i]=np.dot(a[i],b)

	return c
