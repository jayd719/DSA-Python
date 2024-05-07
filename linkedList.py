class Node():
    def __init__(self,data):
        self.data= data
        self.next = None
    def __str__(self) :
        return f'{self.data}'
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.count = 0
    
    def append(self,data):
        newNode = Node(data)
        
        if self.head ==None:
            self.head= newNode
        else:
            currNode = self.head
            while(currNode.next!=None):
                currNode= currNode.next 
            currNode.next = newNode
        
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next_
    def __str__(self):
        returnString =''
        node = self.head
        while node:
            returnString +=f"{node.data} "
            node = node.next_
        return returnString
        