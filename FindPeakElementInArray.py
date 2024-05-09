from random import randint
test1 =[1,2,3,4,5,6]
test2 = [6,5,4,2,3,1]
test3=[]
listData = [9,1,4,7,3,8,2,5]
test5 =[5,5,5,5,5,5,5]
for i in range(0, randint(0,10)):
    test3.append(randint(0,10))
testCases =[test1,test2,test5,test3, listData,]

def findPeakElement(arr):
    lenghtOfArray = len(arr)
    peakElement = None
    
    if(lenghtOfArray<=1):
        return peakElement
    
    if(arr[0]>=arr[1]):
        peakElement= arr[0]
    
    elif(arr[-1]>=arr[-2]):
       peakElement= arr[-1]
    else:
        i =1
        while(i<lenghtOfArray-2 and peakElement is None):
            if(arr[i-1]< arr[i] and arr[i+1]<arr[i]):
                peakElement = arr[i]
            i+=1
    return peakElement



for test in testCases:
    print(f'Peak For {test}\t{findPeakElement(test)}')
      
