test1 = [0, 1, 2, 0, 1, 2]
test2 =[0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]


def sortArray(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    
    while(mid<=high):
        if(arr[mid]==1):
            mid+=1
        elif (arr[mid]==0):
            arr[mid],arr[low]=arr[low],arr[mid]
            mid+=1
            low+=1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1

print(test1)
sortArray(test1)
print(test1)
print('\n\n\n')
print(test2)
sortArray(test2)
print(test2)