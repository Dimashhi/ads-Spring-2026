import pygame
import random

pygame.init()

sky = (135, 206, 235)
player_col = (0, 0, 255)
enemy_col = (255, 0, 0)
obs_col = (100, 100, 100)
text_col = (0, 0, 0)

sw = 500
sh = 600
win = pygame.display.set_mode((sw, sh))
clock = pygame.time.Clock()

car_w = 40
car_h = 60

font = pygame.font.SysFont("arial", 30)

def run_chase():
    px = sw // 2
    py = sh - 100
    
    ex = random.randint(0, sw - car_w)
    ey = random.randint(50, 200)
    e_speed = 3
    
    ox = random.randint(0, sw - car_w)
    oy = -100
    o_speed = 5
    
    score = 0
    run = True
    
    while run:
        win.fill(sky)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and px > 0:
            px -= 7
        if keys[pygame.K_RIGHT] and px < sw - car_w:
            px += 7
        if keys[pygame.K_UP] and py > 0:
            py -= 7
        if keys[pygame.K_DOWN] and py < sh - car_h:
            py += 7

        ex += e_speed
        if ex <= 0 or ex >= sw - car_w:
            e_speed *= -1
            
        oy += o_speed
        if oy > sh:
            oy = -50
            ox = random.randint(0, sw - car_w)
            score += 1 

        p_rect = pygame.Rect(px, py, car_w, car_h)
        e_rect = pygame.Rect(ex, ey, car_w, car_h)
        o_rect = pygame.Rect(ox, oy, car_w, car_h)

        if p_rect.colliderect(e_rect):
            score += 10
            ex = random.randint(0, sw - car_w)
            ey = random.randint(50, 200)

        if p_rect.colliderect(o_rect):
            run = False

        pygame.draw.rect(win, player_col, p_rect)
        pygame.draw.rect(win, enemy_col, e_rect)
        pygame.draw.rect(win, obs_col, o_rect)
        
        txt = font.render("Score: " + str(score), True, text_col)
        win.blit(txt, (10, 10))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

run_chase()