import pygame
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
        self.width = 9
        self.height = 9

        # initial conditions not controlled by constructor
        self.box = Rect(self.position.x-(self.width/2), self.position.y, self.width, self.height)

        boids.append(self)


    def update(self) -> None:

        # Rule 1: Thou shalt avoid other boids

        # starts at midddle value, then alternates between middle+j and middle-j:   90, 91, 89, ... 
        i = Vector2(1,0).angle_to(self.velocity)
        for j in range(self.visibilityAngle):
            if j % 2 == 0:
                j *= -1
            i += j

            farVisPoint = self.position + self.velocity
            farVisPoint.scale_to_length(self.visibleRange)
            farVisPoint.rotate(i)
            print(farVisPoint)

            lineSlope = (farVisPoint.y - self.position.y) / (farVisPoint.x - self.position.x)

            passedChecks = 0
            for boid in boids:
                if boid != self:
                    if boid.box.collidepoint():
                        pass
                    #if not visBox.colliderect(boid.box):
                        #passedChecks += 1

            if passedChecks == len(boids)-1:
                self.velocity.rotate(i)
                self.position += self.velocity
                break

        self.box = Rect(self.position.x-(self.width/2), self.position.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.box)
        pygame.draw.line(screen, (100,100,100), self.position, farVisPoint)
        pygame.draw.line(screen, (255,  0,  0), self.position, self.position + self.velocity, 2)