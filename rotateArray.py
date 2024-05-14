def rotate(arr):
    n=len(arr)
    i =1
    temp = arr[-1]
    while(i<n):
        arr[i]=arr[i-1]
        i=i+1
    
    arr[0]= temp
    
    
arr=[1, 2, 3, 4, 5]
rotate(arr)

print(arr)