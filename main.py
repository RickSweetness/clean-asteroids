import pygame
from constants import *

def main():
    pygame.init
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.display.flip()








if __name__ == "__main__":
    main()