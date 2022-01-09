angle = 90
for i in range(90):
    if i % 2 == 0:  i *= -1
    angle += i
    print(angle)

                #"""if self.position.x + checkPoint.x < 0 \
                #or self.position.x + checkPoint.x > SCR_WIDTH \
                #or self.position.y + checkPoint.y < 0 \
                #or self.position.y + checkPoint.y > SCR_HEIGHT:
                #    print(f"boid {boids.index(self)} detected screen barrier at {self.position + checkPoint}")
                #    # angleUnsafe doesn't need to be called here beceause one break statement will go back to the angle loop
                #    break"""