#Find Middle of the Linked List

# Method 1: count number of items in list
# time complexity: O(N)
# space complexity: O(1)
def findMiddle(ll):
    currNode = ll.head
    count=0
    while(currNode):
        currNode= currNode.next_
        count+=1
    
    mid = count//2
    i =0
    currNode = ll.head
    while(i<mid):
        currNode = currNode.next_
        i+=1
    return currNode


#Method 2: Flody's alogrithm
def Floyds(ll):
    slowPtr = ll.head
    fastPtr =ll.head
    
    while(fastPtr is not None and fastPtr.next_ is not None):
        slowPtr = slowPtr.next_
        fastPtr = fastPtr.next_.next_
    return slowPtr