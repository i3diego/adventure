import sys

from room import Room
from player import Player
import Map

"""
Main game loop lives here.
"""
commands = ["left", "right", "forward", "backward", "inspect", "light", "help"]

print('This is a text based adventure')
room_number = input('Please input the number of Rooms you want to play: ')
room_number = int(room_number)
print('Your commands can be "left", "right", "forward", "backward", "inspect", "light" or "help" if you need a reminder')

#mockup for testing purposes
sides_entrance = {
    "left" : 'wall',
    "right" : 'door',
    "front" : 'door',
    "back" : 'wall'
}

#mockup for testing purposes
sides_r1 = {
    "left" : 'door',
    "right" : 'wall',
    "front" : 'wall',
    "back" : 'door'
}

#mockup for testing purposes
sides_r2 = {
    "left" : 'door',
    "right" : 'wall',
    "front" : 'wall',
    "back" : 'door'
}

#mockup for testing purposes
entrance = Room(sides_entrance,'light', [], 'entrance', (0,0))
room1 = Room(sides_r1, 'light', [], 'room 1', (0,1))
room2 = Room(sides_r2, 'light', [], 'room 2', (1,0))
current_room = None
avatar = Player()

map = Map.createMap(room_number)
Map.printMap(map)
print('start')
print(Map.determineStart(room_number))


map = [[entrance, room1],[room2]]

def quitGame(*args):
    print("I'm quitting")
    sys.exit()

def move(direction, avatar, current_room):
    #left -> x -1
    #right -> x +1
    if (current_room.sides[direction] == 'door'):
        if(direction == 'left'):
            avatar.updateX(-1)
        elif (direction == 'right'):
            avatar.updateX(1)
        elif (direction == 'front'):
            avatar.updateY(1)
        elif (direction == 'back'):
            avatar.updateY(-1)
    elif (current_room.sides[direction] == 'wall'):
        print('you ran into a wall BONK')
    current_room = map[avatar.x][avatar.y]

def inspect(*args):
    print('inspection')
    #print(kwargs.current_room.objects)

def printHelp(*args):
    print(' You may use the following commands: ')
    print(commands)

def light(*args):
    print('Torch lit')

switcher = {
   "left"   : move,
   "right"  : move,
   "front"  : move,
   "back"   : move,
   "inspect": inspect,
   "help"   : printHelp,
   "light"  : light,
   "quit"   : quitGame
} 

def evalCommand(command, avatar):
    try:
        return switcher[command](command, avatar, current_room)
    except KeyError:
        print('unknow command')
    

print('Welcome try to escape')
current_room = map[avatar.x][avatar.y]

while 1 < 2:
    print("You are currently here " +current_room.name)
    command = input("Enter command: ")
    action = evalCommand(command, avatar), current_room
    current_room = map[avatar.x][avatar.y]


