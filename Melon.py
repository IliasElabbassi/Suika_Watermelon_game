"""
The melon can merge with melon of the same radius.
The melon are affected by physics.
Each melon of the same size has identical color or image, compared to the other.

"""
import val
import pymunk

class Melon():
    """
    x : Coordinate x
    y : Coordinate y
    radius : Radius of the "Melon"
    color : Color of the "Melon"
    """
    def __init__(self, x, y, radius, color, space):
        self.body = pymunk.Body(10,1000, body_type=pymunk.Body.DYNAMIC)
        self.body.position = (x, y)
        self.shape = pymunk.Circle(self.body, radius)
        self.radius = radius
        self.color = color

        space.add(self.body,self.shape)
    
    def draw(self, pygame, screen):
        pygame.draw.circle(screen, self.color, (self.body.position.x, self.body.position.y), self.radius, width=0)

    