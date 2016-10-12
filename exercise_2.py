def nestedList(mylist):
    length = 0
    for i in mylist:
        if len(i) > length:
            length = len(i)
        else:
            continue
    return length

#print(nestedList([[1,2,3],[4,56,6,6,6],[6,7,8,9]]))
#print(nestedList([[],[]]))
def averageValue(mylist):
    length = nestedList(mylist)
    listLen = len(mylist)
    res = [0] * length
    temp = [0] * length
    for i in range(0,length):
        for j in range(0, listLen):
            if len(mylist[j]) >= (i + 1):
                res[i] += mylist[j][i]
                temp[i] += 1
            else:
                continue

    for i in range(0,length):
        res[i] = res[i]/temp[i]
    return res

print(averageValue([[1,2,3],[4,5],[6,7,8,9],[10]]))