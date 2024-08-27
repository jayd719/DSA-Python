str1 = 'geeks quiz practice code'
str2 = 'i love programming very much'


def reverseString(string):
    returnString =""
    tempList = string.split(" ")
    n = len(tempList)-1
    while(n>=0):
        returnString+=f"{tempList[n]} "
        n-=1
    
    return returnString[:-1]



print(str1)
print(reverseString(str1))
print(str2)
print(reverseString(str2))
