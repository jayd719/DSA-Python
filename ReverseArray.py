from random import randint
test1 =[1,2,3,4,5,6]
test2 = [6,5,4,2,3,1]
test3=[]
listData = [9,1,4,7,3,8,2,5]
test5 =[5,5,5,5,5,5,5]
for i in range(0, randint(0,10)):
    test3.append(randint(0,10))
testCases =[test1,test2,test5,test3, listData,]



def reverseArray(arr):
    i =0
    n = len(arr)-1
    while(i<=n):
        arr[i],arr[n]=arr[n],arr[i]
        i+=1
        n-=1



for test in testCases:
    print(f'Before {test}')
    reverseArray(test)
    print(f'After  {test}\n\n\n')
      
