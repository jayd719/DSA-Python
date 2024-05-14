arr1 =[1, 3, 4, 5, 7]
arr2 =[2, 3, 5, 6]

def usingSets(arr1,arr2):
    setOne = set(arr1)
    setTwo = set(arr2)
    
    print(f'Intersection : {setOne.intersection(setTwo)}')
    print(f'Union:         {setOne.union(setTwo)}')
    

usingSets(arr1,arr2)