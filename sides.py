class Sides:
    """
    This class defines the sides of a room. A side can either be a door or a wall.
    """
    def __init__(self, right, left, front, back):
        self.left = left
        self.right = right
        self.front = front
        self.back = back
        