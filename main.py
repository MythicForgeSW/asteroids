# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # create a clock object to help control the frame rate
    dt = 0 # initialize the delta time variable
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # create a player object

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if the user clicks the close button
                return
            
        screen.fill("black") # fill the screen with black color
        player.update(dt) # update the player object with the delta time before rendering
        player.draw(screen) # draw the player object on the screen
        pygame.display.flip() # update the display with the new screen
        dt = clock.tick(60) / 1000 # limit the frame rate to 60 fps and get the time passed since the last frame

if __name__ == "__main__":
    main()
    # This line ensures the main() function is only called when this file is run directly; 
    # it won't run if it's imported as a module. 
    # It's considered the "pythonic" way to structure an executable program in Python.