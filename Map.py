
#player gives number of rooms int
# randomly generate layout of map
from random import randrange

def createMap(number):
    y = 0
    map =[]
    try:
        number = int(number)
    except:
        print('Please input a valid number without comma')

    while(y < number):
        tmp = [(y,0),(y,1),(y,2),(y,3),(y,4)]
        map.append(tmp)
        y = y+1
    return map

def printMap(map):
    #map = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j], end=' ')
        print()

def determineStart(number):
    x = randrange(0, number, 1)
    y = randrange(0, number, 1)
    start = (x,y)
    return start
