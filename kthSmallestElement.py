test =[7, 10, 4, 3, 20, 15]


def getPivot(arr,l,r):

    pivot = arr[r]
    i = l-1
    j=l
    while(j<r):
        if(arr[j]<pivot):
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    
    i+=1
    arr[i],arr[r] = arr[r],arr[i]
    return i

def quickSort(arr,l,r):
    if(l<r):
        pivotPoint = getPivot(arr,l,r)
        quickSort(arr,l,pivotPoint-1)
        quickSort(arr,pivotPoint+1,r)


# 
# sort array and return
def kthSmallestElement(arr,k):
    quickSort(arr,0,len(arr)-1)
    return arr[k-1]




print(kthSmallestElement(test,3))
print(kthSmallestElement(test,4))
      