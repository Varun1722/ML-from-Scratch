import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	# print(np.unique(x),np.max(x))
	if n_col==None:
		n_col=np.max(x)+1
	# res = [[0]*n_col]*len(x)
	res = np.zeros((len(x),n_col))
	for i in range(len(x)):
		res[i][x[i]]=1.0
	return np.array(res)
