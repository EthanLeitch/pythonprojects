# ===========DON'T PRESS ENTER===============
# A.K.A the lamest game in the universe
# Made by Ethan (https://github.com/EthanLeitch)
# ===========================================
import time
import sys
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def display_box(screen, message):
    fontobject=pygame.font.SysFont('Arial', 18)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255, 255, 255)),
                ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    pygame.display.flip()

def get_key():
    while True:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key

if __name__ == "__main__":

    #RGB color presets
    white = (255,255,255)
    black = (0  ,0  ,0  )
    red = (255, 0, 0)
    Sec = 0
    Min = 0
    HighScore = 0

    pygame.init()
    pygame.display.set_caption('Do not press Enter.')

    # Graphics initialization
    full_screen = False    
    window_size = (1024, 768)
    pygame.init()      
    if full_screen:
        surf = pygame.display.set_mode(window_size, HWSURFACE | FULLSCREEN | DOUBLEBUF)
    else:
        surf = pygame.display.set_mode(window_size)

    now = time.clock()

    # Create a display box
    while True:

        surf.fill(black)
        
        display_box(surf, "Do not press enter.")
        pygame.display.flip()
        
        inkey = get_key()
        if inkey == K_RETURN or inkey == K_KP_ENTER:
            break

    duration = time.clock() - now

    surf.fill(black)
    pygame.display.flip()

    display_box(surf, "...seriously?")
    time.sleep(2.3)
    if duration > HighScore:
        HighScore = duration
    pygame.display.quit()
    pygame.quit()

print("")
print("The time it took for you to press enter is %s seconds." % (duration))
print("")
#End program
