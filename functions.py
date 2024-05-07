def linearSearch(linkedList,key):
    currNode = linkedList.head
    returnNode = None
    while(currNode and returnNode is None):
        if(currNode.data == key):
            returnNode = currNode
        currNode = currNode.next
    return returnNode

def ceilingNumberLinear(linkedList, key):
    currNode = linkedList.head
    while(currNode and currNode.data<key):
        currNode = currNode.next
    return currNode

def binarySearch(arr,l,r,key):
    while(l<=r):
        mid = (l+r)//2
        if(arr[mid]==key):
            return arr[mid]
        elif(arr[mid]<key):
            l = mid+1
        else:
            r=mid-1
    return -1

def binarySearchRec(arr,l,r,key):
    if(l<=r):
        mid = (l+r)//2
        if(arr[mid]==key):
            return arr[mid]
        elif(arr[mid]<key):
            binarySearchRec(arr,mid+1,r,key)
        else:
            binarySearchRec(arr,l,r-1,key)
    return -1