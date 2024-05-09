from random import randint

listData = [9,1,4,7,3,8,2,5]
data1 = [1,2,3,4,5,6,9,8]
data2 = [1,2,3,4,5,6]
data3 = [6,5,4,3,2,1,0]

data4=[]
for i in range(0, randint(0,10)):
    data4.append(randint(0,10))

testCases =[listData,data1,data2,data3,data4]

# timeComplexity: O(n^2)
# space complexity: O(1)
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

def merge(left, right):
    arr=[]
    j,i=0,0
    while(i<len(left) and j <len(right)):
        if[right[j]>left[i]]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    while(i<len(left)):
        arr.append(left[i])
        i+=1
    while(j<len(right)):
        arr.append(right[j])
        j+=1
        
    return arr

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    return merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))
        
        
        

def seleticonSort(arr):
    i =0
    lenghtOfArray = len(arr)
    while(i<lenghtOfArray):
        minIndex =i
        j=i+1
        while(j<lenghtOfArray):
            if(arr[j]<arr[minIndex]):
                minIndex= j
            j+=1
        arr[i],arr[minIndex] = arr[minIndex],arr[i]
        i+=1
        

for test in testCases:
    print(f'Before:\t{test}')
    seleticonSort(test)
    print(f'After:{test}\t\n\n')        
