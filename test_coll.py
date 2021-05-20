import pygame, pymunk
import collision

def static_ball(space, coord, radius=50):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    body.position = (coord[0], coord[1])
    shape = pymunk.Circle(body, radius)
    space.add(body,shape)

    return shape

def draw_ball(balls):
    for ball in balls:
        pos_x = int(ball.body.position.x)
        pos_y = int(ball.body.position.y)
        surface1 = screen.convert_alpha()
        surface1.fill([0, 0, 0, 0])
        pygame.draw.circle(surface1, (255, 0, 0, 128), (pos_x, pos_y), ball.radius)
        screen.blit(surface1, (0,0))
        pygame.draw.circle(screen, (0, 0, 0),(pos_x, pos_y), ball.radius, width=1)
        pygame.draw.circle(screen, (255,0,0), (pos_x, pos_y), 3)
        
def draw_line_betweenBalls(ball1, ball2):
    pos_x = int(ball1.body.position.x)
    pos_y = int(ball1.body.position.y)
    pos_x2 = int(ball2.body.position.x)
    pos_y2 = int(ball2.body.position.y)
    pygame.draw.line(screen, (0,0,0), (pos_x, pos_y), (pos_x2, pos_y2))

def draw_text(text, at):
    textsurface = font.render(text, False, (0, 0, 0))
    screen.blit(textsurface,(at[0],at[1]))

pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 20)
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (0,500)

game_running = True

balls = []
balls.append(static_ball(space, (685,60)))
balls.append(static_ball(space, (324,627)))

distance = collision.get_distance(balls[0], balls[1])

balls.append(static_ball(space, (balls[0].body.position.x,balls[0].body.position.y), distance))

def getless(pos1, pos2):
    if pos1 <= pos2:
        return pos1
    return pos2

x = abs(balls[0].body.position.x-balls[1].body.position.x)/2 + getless(balls[0].body.position.x, balls[1].body.position.x)
y = abs(balls[0].body.position.y-balls[1].body.position.y)/2 + getless(balls[0].body.position.y, balls[1].body.position.y)
pos_text_distance = (x, y)
print(pos_text_distance)
mousse_pos = (0,0)

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEMOTION:
            mousse_pos = pygame.mouse.get_pos()
    
    screen.fill((217,217,217))
    
    # check collision
    collidings = collision.get_melons_colliding(balls, test=False)
    collision.on_collision(collidings)
    
    draw_ball(balls)
    draw_line_betweenBalls(balls[0], balls[1])
    draw_text("ball 1 : ({0}, {1})".format(balls[0].body.position.x, balls[0].body.position.y), (50,10))
    draw_text("ball 2 : ({0}, {1})".format(balls[1].body.position.x, balls[1].body.position.y), (50,30))
    draw_text("distance : {0}".format(distance), (50,50))
    draw_text("{0}".format(distance), pos_text_distance)
    draw_text("mousse position : ({0}, {1})".format(mousse_pos[0], mousse_pos[1]), (500,700))
    
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)
