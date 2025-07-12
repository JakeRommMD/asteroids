import pygame
from constants import *
from player import *



def main():
    pygame.get_init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0


    
    # The infinite while loop (your game loop)
    while True:
        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Draw the player
        updatable.update(dt)
        # Fill screen with black
        screen.fill("black")
        # Draw the player
        for obj in drawable:
            obj.draw(screen)
        # Refresh the display
        pygame.display.flip()

        dt = clock.tick(60) / 1000.0  # Frame rate control  






if __name__ == "__main__":
    main()