from random import random

class Room:
    """
    This class defines a room, which the player may interact with. Many rooms can make up a maze like structure, through wchich one has to navigate.
    A room has four sides, which can either be a door or a wall. It may also contain a number of objects or be empty.
    Lastly a room can either be light or dark.

    """
    def __init__(self, north=(None,None), east =(None,None), south=(None,None), west=(None,None)):
        # tuple v1 room refrence, v2 locked or not bool
        self.north = (None,None)
        self.east  = (None,None)
        self.south = (None,None)
        self.west  = (None,None)
        self.neighbours ={}
        self.iluminated = True
        self.loot = []

    def populate(self):
        items = {
            "torch" : 0.5,
            "Small Key": 0.5
        }
        #[item for item in items.keys() if random() <= items[item]]
        self.loot = [item for item, chance in items.items() if random() <= chance]
        self.iluminated = random() <= 0.7

    def add_neighbour(self, direction, room):
        reverse_direction = {
            'north' : 'south',
            'east' : 'west',
            'south' : 'north',
            'west' : 'east'
        }
        if direction not in self.neighbours and reverse_direction[direction] not in room.neighbours:
            self.neighbours[direction] = room
            room.neighbours[reverse_direction[direction]] = self

    def occupied_directions(self):
        return list(self.neighbours.keys())

    def __repr__(self):
       return f"Room id:{id(self)} neighbours:{self.neighbours}"

    def __str__(self):
        return f"Room id:{id(self)} neighbours:{self.neighbours}"
        