test =[1, 1, 2, 2, 2, 2, 3]

def occurenceOfElement(arr,k):
    i = 0
    count =0
    while(i<len(arr)):
        if(arr[i]==k):
            count+=1
        i+=1
    return count

print(f"{occurenceOfElement(test,2)}")