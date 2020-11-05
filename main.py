import sys

from room import Room

from dungeon import Dungeon


"""
Main game loop lives here.
"""
commands = ["left", "right", "forward", "backward", "inspect", "light", "help"]

print('This is a text based adventure')
room_number = input('Please input the number of Rooms you want to play: ')
room_number = int(room_number)
print('Your commands can be "left", "right", "front", "back", "inspect", "light" or "help" if you need a reminder')


a = Dungeon(room_number)
a.crate_path()


print(a)
sys.exit()

