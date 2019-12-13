import tabulate

dataTable=[]

dataFile=open('riskfactors.csv')

for row in dataFile.readlines():
    dataTable.append([])
    for cell in row.split(','):
        dataTable[len(dataTable)-1].append(cell.rstrip())

outputList=[]

for x in range(1,len(dataTable[0])):
    numberList=[]
    for y in range(1,len(dataTable)):
        try:
            if '%' in dataTable[y][x]:
                number=float(dataTable[y][x][:-1])
            else:
                number=float(dataTable[y][x])
            numberList.append(number)
            

        except Exception:
            numberList.append(None)
    maximum=0
    maxPos=0
    minimum=1000000000
    minPos=0
    for i in range(len(numberList)):
        try:
            if numberList[i]>maximum:
                maximum=numberList[i]
                maxPos=i
            if numberList[i]<minimum:
                minimum=numberList[i]
                minPos=i
        except TypeError:
            continue
    outputList.append([dataTable[5][x],dataTable[minPos][0],str(minimum),dataTable[maxPos][0],str(maximum)])

print(tabulate.tabulate(outputList,headers=['Indicator','Minimum','','Maximum','']))