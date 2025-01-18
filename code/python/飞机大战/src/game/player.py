class Player:
    def __init__(self):
        self.position = (0, 0)  # 玩家初始位置
        self.health = 100  # 玩家初始生命值

    def move(self, direction):
        if direction == "up":
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == "down":
            self.position = (self.position[0], self.position[1] + 1)
        elif direction == "left":
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == "right":
            self.position = (self.position[0] + 1, self.position[1])

    def shoot(self):
        # 发射子弹的逻辑
        pass