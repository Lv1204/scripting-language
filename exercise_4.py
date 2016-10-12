from pylab import hist,show,figure,title
PATH = 'data.csv'
METHOD = 'r'
#1
def readFile(path, method):
    f = open(path, method)
    info = []
    for line in f:
        temp = line[:len(line)-1]
        info.append(temp.split(';'))
    f.close()
    return info

#print(readFile('data.csv', 'r'))
#2
def getInfo(givenname, firstname, path, method):
    info = readFile(path, method)
    for i in range(0, len(info)):
        if givenname == info[i][0] and firstname == info[i][1]:
            return [info[i][3], i, info]
        else:
            continue
    return None


#print(getInfo('ADRIAENSSENS', 'Kilian', 'data.csv', 'r'))
#3
def changeGrade(givenname,
                firstname,
                grade,
                path,
                method):
    score,index,data = getInfo(givenname,
                               firstname,
                               path,
                               method)
    data[index][3] = str(grade)
    f = open('output.csv','w')
    for line in data:
        f.write(line[0]
                + ','
                + line[1]
                + ','
                + line[2]
                + ','
                + line[3]
                + '\n')
    return f

'''changeGrade('ADRIAENSSENS', 'Kilian', 20, 'data.csv', 'r')'''
#4
def divdeGroup():
    info = readFile(PATH, METHOD)
    group = {}
    for line in info:
        if line[2] in group:
            group[line[2]].append(line)
        else:
            group.setdefault(line[2], [])
            group[line[2]].append(line)
    return group

#print(divdeGroup())

#5
def allGrade():
    info = readFile(PATH, METHOD)
    res = []
    for line in info:
        res.append(float(line[3]))
    return res

#gradeAll = allGrade()
#print(type(gradeAll[0]))

#6
'''def graphicShow():
    info = allGrade()
    MIN = int(min(info)) - 1
    MAX = int(max(info)) + 1
    step = MAX - MIN
    res = [0] * step
    for i in range(0, len(info)):
        if int(info[i] - MIN) > 0:
            res[int(info[i] - MIN) + 1] += 1
        else:
            res[int(info[i] - MIN)] += 1
    return res
'''
def graphicShow():
    info = allGrade()
    MAX = int(max(info))
    MIN = int(min(info))
    step = MAX - MIN + 1
    res = [0] * step
    for i in range(0, len(info)):
        if (int(info[i] - MIN) < (info[i] - MIN)):
            res[int(info[i] - MIN) + 1] += 1
        else:
            res[int(info[i] - MIN)] += 1
    return res
def printH():
    figure()
    n,bins,patches = hist(graphicShow(), 21, range=(0,22), normed=0, histtype='stepfilled')
    title('Groupx')
    show()
printH()
#print(min(graphicShow()),max(graphicShow()))
#print(graphicShow())