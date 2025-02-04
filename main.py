import pygame
from constants import *
from player import Player

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # creates groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # adds Player class to both groups
    Player.containers = (updatable, drawable)

    # spawns the player object in the middle of the screen
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # frequency
    dt = 0

    # game loop
    while True:  
        # makes me able to close the window providing a rerun value for clicking the QUIT button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return     
            
        updatable.update(dt) # iterates automatically over evvery object in the group and applies their update method

        screen.fill("black")

        # draws the every object in the group
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip() # refreshes the screen

        # limits FPS to 60
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
