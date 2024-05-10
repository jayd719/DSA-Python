

def sumOfSubArray(arr,sum):
    i =0
    while(i<len(arr)):
        currentSum =arr[i]
        if(currentSum==sum):
            return arr[i]
        j =i+1
        while(j<len(arr)):
            currentSum +=arr[j]
            if(currentSum==sum):
                return arr[i:j+1]
            j+=1
        
        i+=1
    return None


def slidingWindow(arr,sum):
    currSum = arr[0]
    start =0
    i =1
    while(i<len(arr)):
        if(currSum==sum):
            return arr[start:i]
        currSum+=arr[i]
        while(currSum>sum and start<i-1):
            currSum-=arr[start]
            start+=1    
        
        i+=1




test1 =[1, 4, 0, 0, 3, 10, 5]
test2 =[1, 4, 20, 3, 10, 5]

print(sumOfSubArray(test1,7))
print(sumOfSubArray(test2,13))

print('\n\n')
print(slidingWindow([1, 2, 3, 4, 5],9))
print(slidingWindow(test2,13))