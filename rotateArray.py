def rotate(arr):
    n=len(arr)-1
    temp = arr[-1]
    while(n>0):
        arr[n]=arr[n-1]
        n-=1
    
    arr[0]= temp
    
    
arr=[1, 2, 3, 4, 5]
rotate(arr)

print(arr)

