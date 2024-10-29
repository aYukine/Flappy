import pygame
import random

pygame.init()

px = 100
py = 225
vel = 1
accel = 1.06
click = 0
score = 0
font = pygame.font.Font(None, 32)
cooldown = 30
time = 0
t_c = 60
bx1 = 0
bx2 = 600
rotation = 0
flappy = pygame.image.load('NicePng_flappy-bird-pipes-png_5857711.png')
flaoppy = pygame.transform.scale(flappy, (50, 50))
background = pygame.image.load('46888871-624a3900-ce7f-11e8-808e-99fd90c8a3f4.png')
bg = pygame.transform.scale(background, (600, 500))
pipe_up = pygame.transform.scale(pygame.image.load('pipe up.png'), (200, 450))
pipe_down = pygame.transform.scale(pygame.image.load('pipe down.png'), (200, 450))
lost = False

screen = pygame.display.set_mode((600, 500))

print("hello")
class Pipe:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        screen.blit(pipe_down, (self.x, self.y - 450))
        screen.blit(pipe_up, (self.x, self.y + 150))

    def move(self):
        self.x -= 3


def update_screen():

    if lost:
        screen.blit(font.render("Idiot", True, (0, 0, 0)), (280, 250))
        screen.blit(font.render("Space to restart", True, (0, 0, 0)), (220, 300))
    else:
        screen.blit(bg, (bx1, 0))
        screen.blit(bg, (bx2, 0))
        for pipie in pipes:
            pipie.move()
            pipie.draw()
        screen.blit(font.render("Clicks :  " + str(click), True, (255, 255, 255)), (20, 20))
        screen.blit(font.render("Passes :  " + str(score), True, (255, 255, 255)), (260, 20))
        screen.blit(font.render("Time :  " + str(time), True, (255, 255, 255)), (490, 20))
        flap = pygame.transform.rotate(flaoppy, rotation)
        screen.blit(flap, (px, py))
    pygame.display.update()


pipes = []


run = True
fps = pygame.time.Clock()

while run:
    rotation -= 1
    jump = False
    cooldown -= 3
    t_c -= 1
    bx1 -= 3
    bx2 -= 3
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump = True
                if lost:
                    score = 0
                    time = 0
                    click = 0
                    px = 100
                    py = 225
                    vel = 1
                    cooldown = 30
                    pipes.clear()
                    lost = False

    FPS = fps.tick(60)
    py += vel
    vel = vel*accel
    spawn = random.randint(0, 400)

    if jump:
        click += 1
        py -= 30
        vel = 1
        rotation = 10

    if cooldown == 0:
        cooldown = 600
        pipes.append(Pipe(600, spawn))

    if t_c == 0:
        time += 1
        t_c = 60

    for pipe in pipes:
        if pipe.x <= -200:
            pipes.pop(pipes.index(pipe))

        if -100 <= pipe.x <= 150 and pipe.y <= py <= pipe.y + 100:
            pass

        elif pipe.x >= 150 and 0 <= py <= 450:
            pass

        elif pipe.x <= -100 and 0 <= py <= 450:
            pass

        else:
            lost = True

        if -103 < pipe.x <= -100:
            score += 1

    if py >= 450:
        lost = True

    if bx1 <= -600:
        bx1 = 600
    if bx2 <= -600:
        bx2 = 600

    update_screen()
