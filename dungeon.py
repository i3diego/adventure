from room import Room
from random import random, choice, sample

class Dungeon:
    def __init__(self, dungeon_depth):
        # if ( dungeon_depth <= 3):
            # dungeon_depth = 3
        self.dungeon_depth = 7 if dungeon_depth < 7 else dungeon_depth
        self.entrance = Room(Room(),True)

        #self.start_room = Room(north=(Room(south=(self.start_room, True)), True))
    
    def crate_path(self,):
        #0 bis 3
        directions = ['north', 'east', 'south', 'west']
        rooms = [Room() for i in range(self.dungeon_depth-2)]
        #print(rooms)

        direction = choice(directions)
        current_room = rooms.pop()
        start_room = Room(direction, current_room)
        past_directions = []
        past_directions.append(direction)

        reverse_direction = {
            'north' : 'south',
            'east' : 'west',
            'south' : 'north',
            'west' : 'east'
        }

        while rooms:
            penultimate_direction = reverse_direction[past_directions[-2]] if len(past_directions) > 1 else []
            remaining_directions = set(directions) - set(current_room.occupied_directions()) - set(penultimate_direction)

            current_direction = sample(remaining_directions, 1)[0]
            next_room = rooms.pop()
            current_room.add_neighbour(current_direction, next_room)
            current_room = next_room
        print(start_room)



            
