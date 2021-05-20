import random
import pymunk
import val

def getRgb(color):
    return (color.r, color.g, color.b)

def nextMelon(accepted_radius):
    rand = random.randint(0, len(accepted_radius)-1)
    
    return (val.all_different_radius[rand], val.all_different_color[rand])

def static_boundaries(space, screen, pygame):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    floor_p1 = (0,val.height-15)
    floor_p2 = (val.width,val.height-15)
    shape = pymunk.Segment(body, floor_p1, floor_p2, 0.0)
    space.add(body, shape)
    pygame.draw.line(screen, (0,0,0), floor_p1, floor_p2, width=1)

    body2 = pymunk.Body(body_type=pymunk.Body.STATIC)
    wall_left_p1 = (15,-100)
    wall_left_p2 = (15,val.height)
    shape = pymunk.Segment(body2, wall_left_p1, wall_left_p2, 0.0)
    space.add(body2, shape)
    pygame.draw.line(screen, (0,0,0), wall_left_p1, wall_left_p2, width=1)

    body3 = pymunk.Body(body_type=pymunk.Body.STATIC)
    wall_right_p1 = (val.width-15,-100)
    wall_right_p2 = (val.width-15,val.height)

    shape = pymunk.Segment(body3, wall_right_p1, wall_right_p2, 0.0)
    space.add(body3, shape)
    pygame.draw.line(screen, (0,0,0), wall_right_p1, wall_right_p2, width=1)

def getless(pos1, pos2):
    if pos1 <= pos2:
        return pos1
    return pos2