# 引入pygame包
import pygame


def main():
    # 创建窗口，设置窗口的宽和高
    window = pygame.display.set_mode([500, 500])

    # 设置窗口标题
    pygame.display.set_caption("飞机大战 ")

    # 设置窗口图表

    # 1.加载图片
    game_icon = pygame.image.load("res/game.ico")

    # 2.用图片对象设置窗口
    pygame.display.set_icon(game_icon)


if __name__ == '__main__':
    main()


input()

