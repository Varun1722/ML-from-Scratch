def performance_metrics(actual: list[int], predicted: list[int]) -> tuple:
	# Implement your code here
	true_positive,true_negs, false_pos , false_neg = 0,0,0,0
	for i in range(len(actual)):
		if(actual[i]==predicted[i]==1):
			true_positive+=1
		elif(actual[i]==predicted[i]==0):
			true_negs+=1
		elif(actual[i]==0):
			false_pos += 1
		else:
			false_neg += 1
		
	confusion_matrix=[[true_positive, false_neg],[false_pos,true_negs]]

	# print(confusion_matrix)
	accuracy=(true_positive+true_negs)/(len(actual))

	precision = true_positive/(true_positive+false_pos)

	recall= true_positive/(true_positive+false_neg)
	f1=2*(precision*recall/(precision+recall))
	negativePredictive = true_negs/(true_negs+false_neg)
	specificity = true_negs/(true_negs+false_pos) 

	return confusion_matrix, round(accuracy, 3), round(f1, 3), round(specificity, 3), round(negativePredictive, 3)
