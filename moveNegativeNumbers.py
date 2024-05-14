# Move all negative numbers to beginning and positive to end with constant extra space
# arr=[12, 11, -13, -5, 6, -7, 5, -3, -6]
arr=[1, 2,  -4, -5, 2, -7, 3, 2, -6, -8, -9, 3, 2,  1]

def moveNegativeToOneSide(arr):
    left =0
    right = len(arr)-1
    
    while(left<=right):
        if(arr[left]<0 and arr[right]<0):
            left+=1
            
        elif(arr[left]>0 and arr[right]<0 ):
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        elif (arr[left]>0 and arr[right]>0):
            right-=1
        else:
            left+=1
            right-=1


def moveToOneSideMethodTwo(arr):
   left =0
   right = len(arr)-1
   while(left<=right):
        if arr[left]<0:
           left+=1
        elif arr[right]>0:
            right-=1
        else:
            arr[left],arr[right]=arr[right],arr[left]

print(arr)
print('After Operation \n')
moveToOneSideMethodTwo(arr)
print(arr)
        