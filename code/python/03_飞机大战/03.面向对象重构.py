import pygame
import time
from pygame.locals import *


class HeroPlane(object):
    # 英雄飞机类
    def __init__(self, screen_temp):
        self.x = 210
        self.y = 700
        self.screen = screen_temp
        self.image = pygame.image.load("./demo/hero1.png")

    def display(self):
        self.screen.blit(self.image, (self.x ,self.y))

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_up(self):
        self.y -= 5  
    
    def move_down(self):
        self.y += 5

def key_control(hero_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否按下了键
        elif event.type == KEYDOWN:
            # 检测案件是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                hero_temp.move_left()
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                hero_temp.move_right()
            elif event.key == K_w or event.key == K_UP:
                print("up")
                hero_temp.move_up()
            elif event.key == K_s or event.key == K_DOWN:
                print("down")
                hero_temp.move_down()
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print("space")


def main():
    # 1.创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 2.创建一个背景图片
    background = pygame.image.load("demo/background.png")

    # 3.创建一飞机图片
    hero = HeroPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        hero.display()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == '__main__':
    print ("测试001")
    main()
