import random
import pygame as pg
import time
from pygame.locals import *

pg.init()

font = pg.font.Font('font.otf', 20)

width = 740
height = 240

gameplatex = 640
gameplatey = 240

step = 30

screen = pg.display.set_mode((width, height))

pg.display.set_caption("Snake Game")

running = True

dx, dy = 0, 0

angle = "up"

xpos = (gameplatex // step // 2) * step
ypos = (gameplatey // step // 2) * step

last_tick = time.monotonic()
tick_rate = 1/4
applex = random.randint(0, gameplatex // step - 1) * step
appley = random.randint(0, gameplatey // step - 1) * step
score = 0
register = 0
snake_body = []

while running:

    now = time.monotonic()
    if now - last_tick >= tick_rate:
        last_tick = now

        xpos += dx
        ypos += dy

        if xpos < 0 or xpos + step > gameplatex:
            running = False
        elif ypos < 0 or ypos + step > gameplatey:
            running = False

        screen.fill((0, 0, 0))

        screen.blit(
            font.render("Score: " + str(score), True, (255, 255, 255)),
            (gameplatex + 10, 10)
        )

        pg.draw.line(screen, (255, 255, 255), (gameplatex, 0), (gameplatex, gameplatey), 1)
        if applex == xpos and appley == ypos:
            score = score + 1   
            applex = random.randint(0, gameplatex // step - 1) * step
            appley = random.randint(0, gameplatey // step - 1) * step
            snake_body.insert(0, (xpos, ypos))

        snake_body.insert(0, (xpos, ypos))
        snake_body.pop(len(snake_body) - 1)

        for each in snake_body:
            pg.draw.rect(screen, (0,255,0), (each[0], each[1], step, step))

        pg.draw.rect(screen, (0,0,255), (xpos, ypos, step, step))
        pg.draw.rect(screen, (255,0,0), (applex, appley, step, step))
        print(xpos, ypos, score)
        pg.display.update()

    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

        if e.type == pg.KEYDOWN:
            if e.key == pg.K_UP:
                dx, dy = 0, -step
                angle = "up"

            elif e.key == pg.K_DOWN:
                dx, dy = 0, step
                angle = "down"

            elif e.key == pg.K_RIGHT:
                dx, dy = step, 0
                angle = "right"

            elif e.key == pg.K_LEFT:
                dx, dy = -step, 0
                angle = "left"
            if (xpos + dx, ypos + dy) in snake_body:
                running = False

pg.quit()
