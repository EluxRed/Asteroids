import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # creates groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # adds Player class to 2 groups
    Player.containers = (updatable, drawable)

    # adds Asteroid class to 3 groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # adds AsteroidField class to 1 group
    AsteroidField.containers = (updatable)

    #adds Shot class to 3 groups
    Shot.containers = (shots, updatable, drawable)

    # spawns the player object in the middle of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # creates an asteroid field
    asteroid_field = AsteroidField()

    # frequency
    dt = 0

    # game loop
    while True:  
        # makes me able to close the window providing a rerun value for clicking the QUIT button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return     
            
        updatable.update(dt) # iterates automatically over every object in the group and applies their update method

        for obj in asteroids:
            if obj.collides_with(player):
                raise SystemExit("Game over!")
            
        for obj in asteroids:
            for bullet in shots:
                if bullet.collides_with(obj):
                    obj.split()
                    bullet.kill()

        screen.fill("black")

        # draws the every object in the group
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip() # refreshes the screen

        # limits FPS to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
