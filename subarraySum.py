

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
    i=0




test1 =[1, 4, 0, 0, 3, 10, 5]
test2 =[1, 4, 20, 3, 10, 5]

print(sumOfSubArray(test1,5))
print(sumOfSubArray(test2,13))