class Room:
    """
    This class defines a room, which the player may interact with. Many rooms can make up a maze like structure, through wchich one has to navigate.
    A room has four sides, which can either be a door or a wall. It may also contain a number of objects or be empty.
    Lastly a room can either be light or dark.

    """
    def __init__(self, sides, light, objects, name, coordinates):
        self.sides = sides
        self.light = light
        self.objects = objects
        self.name = name
        self.coordinates = coordinates
