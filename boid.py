import pygame, math
from pygame import Rect, Vector2, constants
from screen import *

boids = []

class Boid:

    def __init__(self, position:Vector2=Vector2(SCR_WIDTH/2,SCR_HEIGHT/2), velocity:Vector2=Vector2(0,-10)) -> None:

        self.position = position
        self.velocity = velocity

        # constants
        self.visibleRange = 60
        self.visibilityAngle = 90
        self.color = (199,146,234)
        self.width = 10
        self.height = 10

        # *initial conditions* not controlled by constructor
        self.box = Rect(self.position.x-(self.width/2), self.position.y-(self.width/2), self.width, self.height)

        boids.append(self)

    def collisionCheck(self) -> int:

        unsafeAngles = []

        for boid in boids:
            if boid != self:
                if self.position.distance_to(boid.position) < self.visibleRange:
                    
                    pass

        # 90, 91, 89, 92, 88, ... 0, 180  (if 90 is start and 180 is visibility angle)
        angle = Vector2(1,0).angle_to(self.velocity)
        for i in range(self.visibilityAngle):
            if i % 2: angle *= 1
            angle += i

            if angle not in unsafeAngles:
                return angle

    # Rule 1: Thou shalt avoid other boids
    def update(self) -> None:

        angle = self.collisionCheck()

        self.velocity.rotate(angle)
        self.position += self.velocity
        self.box = Rect(self.position.x-(self.width/2), self.position.y-(self.width/2), self.width, self.height)

        pygame.draw.circle(screen, (150,150,150), self.position, self.visibleRange, 2)

        pygame.draw.rect(screen, self.color, self.box)
        pygame.draw.line(screen, (255,0,0), self.position, self.position + self.velocity, 2)