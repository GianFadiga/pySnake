'''
Snake game by Gianlucca Fadiga
Initial version made with pygame 1.9.6
Tutorial and instructing by Programador Sagaz in the bellow link
YouTube tutorial: (https://www.youtube.com/watch?v=H4TXHI9BRCQ)
This is a simple snake game made with pygame for educational purposes,
I'm learning Git and GitHub, so I'm using this project to learn how to use it
for branches and commits.
'''

import pygame
import random
from pygame.locals import *


def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x // 10 * 10, y // 10 * 10)


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_random()
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

my_direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = 0 #UP
            if event.key == K_RIGHT:
                my_direction = 1 #RIGHT
            if event.key == K_DOWN:
                my_direction = 2 #DOWN
            if event.key == K_LEFT:
                my_direction = 3 #LEFT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])
    
    if my_direction == UP:
        if snake[0][1] == 0:
            snake[0] = (snake[0][0], 590)
        else:
            snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        if snake[0][1] == 590:
            snake[0] = (snake[0][0], 0)
        else:
            snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == LEFT:
        if snake[0][0] == 0:
            snake[0] = (590, snake[0][1])
        else:
            snake[0] = (snake[0][0] - 10, snake[0][1])
    if my_direction == RIGHT:
        if snake[0][0] == 590:
            snake[0] = (0, snake[0][1])
        else:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    
    for pos in snake:
        screen.blit(snake_skin, pos)
    pygame.display.update()