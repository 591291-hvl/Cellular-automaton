##
from copy import copy, deepcopy
import time




def run():
    N = 100
    table = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ]
    # table = [
    #     [0,0,1,0,0],
    #     [0,0,0,1,0],
    #     [0,1,1,1,0],
    #     [0,0,0,0,0],
    #     [0,0,0,0,0]
    # ]

    for i in range(N):
        #print
        print("=======================")
        printTable(table)
        print("=======================")
        #sleep
        time.sleep(.2)
        
        newTable = deepcopy(table)

        for j in range(len(table)):

            for k in range(len(table[j])):
                sum = getSum(table, j, k)
                if table[j][k] == 1:
                    if sum <= 1 or sum >= 4:
                        newTable[j][k] = 0
                    else:
                        newTable[j][k] = 1
                else:
                    if sum == 3:
                        newTable[j][k] = 1
                    else:
                        newTable[j][k] = 0
        table = deepcopy(newTable)


def getSum(sumTable,y ,x):
    sum = 0
    if x == 0:
        #exclude left side
        if y == 0:
            #exclude top
            sum = sumTable[y+1][x] + sumTable[y][x+1] + sumTable[y+1][x+1]
        elif y == len(sumTable)-1:
            #exclude bottom
            sum = sumTable[y-1][x] + sumTable[y][x+1] + sumTable[y-1][x+1]
        else:
            sum = sumTable[y+1][x] + sumTable[y][x+1] + sumTable[y+1][x+1] + sumTable[y-1][x] + sumTable[y-1][x+1]
    elif x == len(sumTable[y])-1:
        #exclude right side
        if y == 0:
            #exclude top
            sum = sumTable[y+1][x] + sumTable[y][x-1] + sumTable[y+1][x-1]
        elif y == len(sumTable)-1:
            #exclude bottom
            sum = sumTable[y-1][x] + sumTable[y][x-1] + sumTable[y-1][x-1]
        else:
            sum = sumTable[y+1][x] + sumTable[y][x-1] + sumTable[y+1][x-1] + sumTable[y-1][x] + sumTable[y-1][x-1]
    else:
        if y == 0:
            #excludes top
            sum = sumTable[y][x-1] + sumTable[y+1][x-1] + sumTable[y+1][x] + sumTable[y+1][x+1] + sumTable[y][x+1]
        elif y == len(sumTable)-1:
            #excludes bottom
            sum = sumTable[y][x-1] + sumTable[y-1][x-1] + sumTable[y-1][x] + sumTable[y-1][x+1] + sumTable[y][x+1]
        else:
            sum = sumTable[y+1][x+1] + sumTable[y+1][x] + sumTable[y+1][x-1] + sumTable[y][x+1] + sumTable[y][x-1] + sumTable[y-1][x+1] + sumTable[y-1][x] + sumTable[y-1][x-1]
    return sum

def printTable(table):
    str = ""
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == 0:
                str += " "
            else:
                str += "X"
        if not i == len(table[i])-1:
            str += "\n"
    print(str)


run()
