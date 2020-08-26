class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.inventory = { 
            'torch': 0,
            'keys': 0,
        }

    def getX(self):
        return self.x

    def setX(self, new_x):
        self.x = new_x
    
    def updateX(self, val):
        self.x += val

    def updateY(self, val):
        self.y += val

    def getY(self):
        return self.y
    
    def setY(self, new_y):
        self.y = new_y
