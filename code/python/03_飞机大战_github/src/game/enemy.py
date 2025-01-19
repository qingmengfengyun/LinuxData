class Enemy:
    def __init__(self, position, enemy_type):
        self.position = position
        self.enemy_type = enemy_type
        self.health = 100  # 敌人的生命值

    def move(self):
        # 控制敌人的移动行为
        pass

    def shoot(self):
        # 敌人发射子弹
        pass