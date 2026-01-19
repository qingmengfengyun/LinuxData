import pygame
import time

def main():
    #1.创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    #2.创建一个背景图片
    background = pygame.image.load("demo/background.png")

    while True:
        screen.blit(background, (0, 0))

        pygame.display.update()

        time.sleep(1)

if __name__ == '__main__':
    main()