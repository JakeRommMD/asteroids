import pygame
from constants import *



def main():
    pygame.get_init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # The infinite while loop (your game loop)
    while True:
        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill screen with black
        screen.fill("black")
        
        # Refresh the display
        pygame.display.flip()
    print("Starting Asteroids!")
    print("Screen width:", constants.SCREEN_WIDTH)
    print("Screen height:", constants.SCREEN_HEIGHT)



if __name__ == "__main__":
    main()