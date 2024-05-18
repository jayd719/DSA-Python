arr= [10, 5, 1, 4, 3, 5, 6]

freq ={}

i =0
while(i<len(arr)):
    if arr[i] in freq:
        print(arr[i])
        break
    else:
        freq[arr[i]]=1
    i+=1
