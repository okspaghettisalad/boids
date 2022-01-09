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

    # Rule 1: Thou shalt avoid other boids
    def turnAngle(self) -> int:
        
        angle = Vector2(1,0).angle_to(self.velocity)

        if len(boids) == 1:
            return angle

        # THIS IS ONLY FOR DRAWING A LINE FROM THE BOID TO THE CHECK POINT (in update())
        # FOR DEBBUGING AND IS TEMPORARY
        global checkPoint

        checkPoint = Vector2(self.velocity)
        clearedBoids = 0

        # goes though every integer angle from middle to visibilityAngle/2, alternating sides each iteration:
        # 10, 11, 9, 12, 8, etc.

        for i in range(self.visibilityAngle):
            if i % 2 == 0:  i *= -1
            angle += i
            #print(angle)

            checkPoint = Vector2(self.velocity)
            checkPoint.rotate(angle)

            for dist in range(1, self.visibleRange):

                checkPoint.scale_to_length(dist)
                #print(self.position + checkPoint)

                if checkPoint.x < 0 or checkPoint.x > SCR_WIDTH \
                or checkPoint.y < 0 or checkPoint.y > SCR_HEIGHT:
                    print(f"boid {boids.index(self)} detected screen barrier at {self.position + checkPoint}")
                    break

                for boid in boids:
                    if boid != self:
                        if not boid.box.collidepoint(self.position + checkPoint):
                            clearedBoids += 1
                        else:
                            print(f"boid {boids.index(self)} detected {boid} at {self.position + checkPoint}")
                            break

            #pygame.draw.line(screen, (200,200,200), self.position, self.position + checkPoint)

            if clearedBoids == len(boids)-1:
                return angle
    
        #raise Exception(f"boid {boids.index(self)} couldn't find a path")
        return 0
                        
    def update(self) -> None:

        angle = self.turnAngle()
        self.velocity.rotate(angle)
        self.position += self.velocity
        self.box = Rect(self.position.x-(self.width/2), self.position.y-(self.width/2), self.width, self.height)

        pygame.draw.rect(screen, self.color, self.box)
        pygame.draw.line(screen, (255,0,0), self.position, self.position + self.velocity, 2)

        pygame.draw.line(screen, (100,100,100), self.position, self.position + checkPoint)