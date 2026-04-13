import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)

w = 600
h = 400

screen = pygame.display.set_mode((w, h))
timer = pygame.time.Clock()
speed = 15
block = 10

font_style = pygame.font.SysFont("arial", 25)

def my_score(score):
    val = font_style.render("Score: " + str(score), True, yellow)
    screen.blit(val, [0, 0])

def draw_snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], block, block])

def run_game():
    over = False
    close = False

    x1 = w / 2
    y1 = h / 2
    x1_change = 0
    y1_change = 0

    body = []
    length = 1

    foodx = round(random.randrange(0, w - block) / 10.0) * 10.0
    foody = round(random.randrange(0, h - block) / 10.0) * 10.0

    while not over:

        while close == True:
            screen.fill(red)
            msg = font_style.render("You lost! Press C to play or Q to quit", True, black)
            screen.blit(msg, [w / 6, h / 3])
            my_score(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        over = True
                        close = False
                    if event.key == pygame.K_c:
                        run_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block
                    x1_change = 0

        if x1 >= w or x1 < 0 or y1 >= h or y1 < 0:
            close = True
        
        x1 += x1_change
        y1 += y1_change
        screen.fill(green)
        pygame.draw.rect(screen, red, [foodx, foody, block, block])
        
        head = []
        head.append(x1)
        head.append(y1)
        body.append(head)
        
        if len(body) > length:
            del body[0]

        for x in body[:-1]:
            if x == head:
                close = True

        draw_snake(block, body)
        my_score(length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, w - block) / 10.0) * 10.0
            foody = round(random.randrange(0, h - block) / 10.0) * 10.0
            length += 1

        timer.tick(speed)

    pygame.quit()
    quit()

run_game()