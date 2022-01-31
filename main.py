import time

#2d cellular automation
#rule: 150?

def run():
    #Times run
    N = 101
    #Table
    table = fillTable(N)
    table[N//2] = 1
    for i in range(N):
        printTable(table)
        time.sleep(.1)
        newTable = table.copy()
        for j in range(len(table)):
            #sum of neighbors
            sum = 0
            if j == 0:
                sum = table[j] + table[j+1]
            elif j == len(table)-1:
                sum = table[j-1] + table[j]
            else:
                sum = table[j-1] + table[j] + table[j+1]

            if sum == 1 or sum == 3:
                newTable[j] = 1
            else:
                newTable[j] = 0
        table = newTable.copy()

def printTable(table):
    str = ""
    for i in range(len(table)):
        if table[i] == 0:
            str += " "
        else:
            str += "0"
    print(str)

def fillTable(n):
    table = []
    for i in range(n):
        table.append(0)
    return table

run()
