# ▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀[Pusheen v1.2]▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜
# ▍ Pusheen is a cute cat that bounces around your screen meowing! ▐
# ▍ No practical use has been discovered for Pusheen yet...        ▐ 
# ▍ Made by Ethan                                                  ▐
# ▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟

# SETUP
# Imports list
import random, time, pygame, sys, copy
from pygame.locals import *

# Image preloads
cat1 = pygame.image.load('/home/pi/Desktop/PythonProjects/Pusheen/Media/pusheen.jpg')
cat1 = pygame.transform.scale(cat1, (130, 130))
cat2 = pygame.image.load('/home/pi/Desktop/PythonProjects/Pusheen/Media/pusheenmeow.jpg')
cat2 = pygame.transform.scale(cat2, (130, 130))

# Settings
WIDTH = 600
HEIGHT = 500
FPS = 60

#          R    G    B
BLACK =  (0,     0,   0)
WHITE =  (255, 255, 255)
RED =    (255,   0,   0)
GREEN =  (0,   255,   0)
YELLOW = (255, 247,   0)
BLUE =   (0,     0, 255)


# X and Y variables are here!
x = 0
y = 0
xspeed = 3
yspeed = 3

# START UP
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pusheen")
clock = pygame.time.Clock()
# Sound preloads
catmeow = pygame.mixer.Sound('/home/pi/Desktop/PythonProjects/Pusheen/Media/catmeow2.ogg')
# Exit controls
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += xspeed
    y += yspeed


    if x + 125 > WIDTH:
        xspeed = -xspeed
        catmeow.stop()
        catmeow.play()
    if y + 100 > HEIGHT:
        yspeed = -yspeed
        catmeow.stop()
        catmeow.play()
    if x + 8 < 0:
        xspeed = -xspeed
        catmeow.stop()
        catmeow.play()
    if y + 25 < 0:
        yspeed = -yspeed
        catmeow.stop()
        catmeow.play()

    screen.fill(WHITE)
    screen.blit(cat1,(x, y))
    pygame.display.flip()



    clock.tick(FPS)

pygame.quit()

print("")
print("You have closed Pusheen.")
print("")

# Thank you for using Pusheen! :)
