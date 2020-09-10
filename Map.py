
from random import randrange

def createMap(room_number):
    """
    Create a series of nested lists, which form the games map matrix. The matrix then gets filled with a player chosen number of rooms, in a random layout.

    number - The player ist asked for a number at the beginning of the game, which ist the used to determine the size of the matrix.
    """
    x = 0
    map =[]
    try:
        room_number = int(room_number)
    except:
        print('Please input a valid number without comma')

    while(x < room_number):
        y = 0
        column = []
        while(y < room_number):
            column.append((x,y))
            y +=1
        map.append(column)
        x +=1
    print(map)
    return map

def printMap(map):
    """
    Prints a game map in a matrix like style

    map - Current map of the game
    """
    #map = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j], end=' ')
        print()

def determineStart(room_number):
    """
    Creates the first set of coordinates, at which the player will spawn, also these coordinates will be the entrance.

    number - The player ist asked for a number at the beginning of the game, which ist the used to determine the size of the map matrix.
    """

    x = randrange(0, room_number, 1)
    y = randrange(0, room_number, 1)
    start = (x,y)
    return start

def layoutMap(start , map, rooms):
    """
    Creates the layout of the game map. To do so, all possible pairs of coordinates, which are adjacent to an already taken pair are calculated and one ist selected randomly.

    For example, if (0,0) ist already taken, we have two possible next coordinates, either (1,0) or (0,1). Say (0,1) got selected, for the next iteration possible solutions could be
    (1,0), (1,1) and (0,2)

    start - Coordinates of the first room.
    map - Current game map.
    return map
    """
    #insert entrance
    #
    pass
