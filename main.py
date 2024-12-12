# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # create a clock object to help control the frame rate
    dt = 0 # initialize the delta time variable

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if the user clicks the close button
                return
            
        screen.fill("black") # fill the screen with black color
        pygame.display.flip() # update the display
        dt = clock.tick(60) / 1000 # limit the frame rate to 60 fps


if __name__ == "__main__":
    main()
    # This line ensures the main() function is only called when this file is run directly; 
    # it won't run if it's imported as a module. 
    # It's considered the "pythonic" way to structure an executable program in Python.