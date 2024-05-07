def bubbleSort(arr):
	lenghtOfArray = len(arr)
	i =0
	while(i<lenghtOfArray):
		j=0
		swapped = False
		while(j<lenghtOfArray-i-1):
			if(arr[j]>arr[j+1]):
				swapped = True
				arr[j],arr[j+1]=arr[j+1],arr[j]
			j+=1
		if(not swapped):
			break
		i+=1