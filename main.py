import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from shot import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    running = True

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)    

    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    asteroid_field = AsteroidField()
    Shots.containers = (shots, updatables, drawables)    

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for drawable in drawables:
            drawable.draw(screen)

        updatables.update(dt)

        for comet in asteroids:
            for shot in shots:
                if comet.get_collision(shot):
                    comet.split()
                    shot.kill()        
            if comet.get_collision(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()

        dt = clock.tick(60) / 1000








if __name__ == "__main__":
    main()