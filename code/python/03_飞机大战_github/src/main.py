import pygame
from game.game_manager import GameManager

def main():
    pygame.init()
    game_manager = GameManager()
    game_manager.start_game()
    pygame.quit()

if __name__ == "__main__":
    main()