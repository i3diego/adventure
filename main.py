import sys
from room import Room
from player import Player

"""
Main game loop lives here.
"""
commands = ["left", "right", "forward", "backward", "inspect", "light", "help"]

print('This is a text based adventure')
print('Your commands can be "left", "right", "forward", "backward", "inspect", "light" or "help" if you need a reminder')


sides_entrance = {
    "left" : 'wall',
    "right" : 'door',
    "front" : 'wall',
    "back" : 'wall'
}

sides_r1 = {
    "left" : 'door',
    "right" : 'wall',
    "front" : 'wall',
    "back" : 'wall'
}

sides_r2 = {
    "left" : 'wall',
    "right" : 'wall',
    "front" : 'wall',
    "back" : 'door'
}

entrance = Room(sides_entrance,'light', [], 'entrance', (0,0))
room1 = Room(sides_r1, 'light', [], 'room 1', (0,1))
room2 = Room(sides_r2, 'light', [], 'room 2', (1,0))
current_room = None
avatar = Player()

map = [[entrance, room1],[room2]]

def quitGame(*args):
    print("I'm quitting")
    sys.exit()

def move(**kwargs):
    if (kwargs.current_room[kwargs.direction] == 'door'):
        current_room = kwargs.next_room
        print('you have entered '+ current_room.name)
        return
    if (current_room[kwargs.direction] == 'wall'):
        print('you hit yourself on a wall "BONK"')
        return

def inspect(*args):
    print('insepection')
    #print(kwargs.current_room.objects)

def printHelp(*args):
    print(' You may use the following commands: ')
    print(commands)

def light(*args):
    print('Torch lit')

switcher = {
   "left"    : move,
   "right"   : move,
   "forward" : move,
   "backward": move,
   "inspect" : inspect,
   "help"    : printHelp,
   "light"   : light,
   "quit"    : quitGame    
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
    print(map[0][1].name)


