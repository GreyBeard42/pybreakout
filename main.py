from classes import Player
from classes import Ball
from classes import Brick

import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Atari Breakout")
clock = pygame.time.Clock()
print("\nThe games have begun!\n\n---")

left = 84
score = 0
player = Player(400,550,150,30,10)
ball = Ball(400,400,30,30,0,5)
bricks = []
for y in range(round(6)):
    color = pygame.Color(0,0,0)
    color.hsva = (round(y*(360/6)),100,100,100)
    for x in range(14):
        bricks.append(Brick(5+(x*((800-5)/14)), 5+(y*25), 800/14-5, 20, color))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("\nBye for now!\n\n---")
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    
    player.controls()
    pygame.draw.rect(screen, (255, 255, 255), (player.x, player.y, player.w, player.h))

    ball.move()
    ball.collision(player)
    if ball.y > 600-ball.h:
        ball.x, ball.y = 400-ball.w/2,400-ball.h/24
        ball.vx, ball.vy = 0,5
        player.x = 400-player.w/2
    for b in bricks:
        if b.on:
            if ball.collision(b):
                score += 10
                left -= 1
                break
    if left == 0:
        left = 84
        ball.x, ball.y = 400-ball.w/2,400-ball.h/24
        ball.vx, ball.vy = 0,5
        player.x = 400-player.w/2
        for b in bricks:
            b.on = True
    pygame.display.set_caption(str(score)+" - Atari Breakout")
    pygame.draw.rect(screen, (255, 255, 255), (ball.x, ball.y, ball.w, ball.h))

    for b in bricks:
        if b.on: pygame.draw.rect(screen, b.color, (b.x, b.y, b.w, b.h))

    pygame.display.flip()
    clock.tick(60)
