class Bullet:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def move(self):
        self.position[0] += self.direction[0]
        self.position[1] += self.direction[1]