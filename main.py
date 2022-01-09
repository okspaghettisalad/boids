import pygame, random
from pygame import constants
from screen import *
from boid import *


#for i in range(2):
#    Boid(Vector2(random.randint(0,SCR_WIDTH),random.randint(0,SCR_HEIGHT)), Vector2(0,10).rotate(random.randint(0,360)))

Boid(Vector2(SCR_WIDTH/2,SCR_HEIGHT-10), Vector2(0,-10))
Boid(Vector2(SCR_WIDTH/2,10), Vector2(0,10))

running = True
while running:

    pygame.time.wait(120)
    screen.fill((0,0,0))

    for boid in boids:
        boid.update()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False