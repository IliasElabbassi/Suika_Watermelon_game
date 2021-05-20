# collision handling
import math
from utils import getless, getRgb
import val
from Melon import *

"""
fromula : squareRoot((p1.x-p2.x)²+(p1.y-p2.y)²)

if the radius of the two circle is greater or equal to the distance between the two points then the circle are colliding
"""
def check_collision(melon1, melon2):
    distance = get_distance(melon1, melon2)
    return melon1.radius+melon2.radius >= distance

def get_distance(melon1, melon2):
    return abs(math.sqrt(pow(melon1.body.position.x - melon2.body.position.x, 2)+pow(melon1.body.position.y - melon2.body.position.y, 2)))

def get_melons_colliding(melons, test=False):
    colliding = [] # [(melon1, melon2), (a,b)]
    
    for melon in melons:
        
        for melon2 in melons:
            if (melon2, melon) in colliding:
                        continue
            if melon != melon2 and melon.radius == melon2.radius:
                is_colliding = check_collision(melon, melon2)
                if is_colliding:
                    colliding.append((melon, melon2))
                    #print("colliding: {0}, {1}".format(melon, melon2))

    return colliding

"""
For each colliding melons we check if they have the same radius
if they does we merge them and create a bigger melon.
At the middle of the distance of the two point
"""
def on_collision(collidings, melons, space, accepted_radius):
    for colliding in collidings:
        #if colliding[0].radius == colliding[1].radius:
        # we merge them
        (melons, accepted_radius) = merge(colliding[0], colliding[1], melons, space, accepted_radius)
        #print("merge: {0}, {1}".format(colliding[0], colliding[1]))
    
    return (melons, accepted_radius)

def compute_new_coord(coord, coord2):
    x = abs(coord.x-coord2.x)/2 + getless(coord.x, coord2.x)
    y = abs(coord.y-coord2.y)/2 + getless(coord.y, coord2.y)
    return [int(x),int(y)]

def get_new_radius(rad):
    index = val.all_different_radius.index(rad)
    if index >= len(val.all_different_radius)-1:
        index = len(val.all_different_radius)-1
    else:
        index = index+1    
    new_radius_color = val.all_different_color[index]
    
    return (val.all_different_radius[index], new_radius_color)

def merge(melon1, melon2, melons, space, accepted_radius):
    if melon1 in melons and melon2 in melons:
        melons.remove(melon1)
        melons.remove(melon2)
        space.remove(melon1.body, melon1.shape)
        space.remove(melon2.body, melon2.shape)
        
        (new_radius, color) = get_new_radius(melon1.radius)
        coord = compute_new_coord(melon1.body.position, melon2.body.position)
        melons.append(Melon(coord[0], coord[1], new_radius, getRgb(color), space))
        
        if new_radius not in accepted_radius:
            accepted_radius.append(new_radius)
        
    return (melons, accepted_radius)


