k = 9
while k > 0:
    print("k = ", k)
    k-=1

for k in range(9,0,-1):
    print("k = ",k)

def findMax(yourList):
    length = len(yourList)
    if length > 0:
        listMax = yourList[0]
        for i in yourList:
            if i > listMax:
                listMax = i
        return listMax
    else:
        return None

def findMin(yourList):
    length = len(yourList)
    if length > 0:
        listMin = yourList[0]
        for i in yourList:
            if i < listMin:
                listMin = i
        return listMin
    else:
        return None

def findBoundary(mylist):
    return [findMax(mylist),findMin(mylist)]


a = [1,2,3,4,5]
print(type(findBoundary(a)))