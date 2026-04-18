import pygame
import datetime

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Clock')
clock = pygame.time.Clock()
FPS = 50
done = False

img_main = pygame.image.load('Practice9/mickeys_clock/images/mainclock.png')
img_main = pygame.transform.scale(img_main, (600, 600))

img_min = pygame.image.load('Practice9/mickeys_clock/images/rightarm.png') 
img_min = pygame.transform.scale(img_min, (800, 700))

img_sec = pygame.image.load('Practice9/mickeys_clock/images/leftarm.png')
img_sec = pygame.transform.scale(img_sec, (40, 500))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    now = datetime.datetime.now()
    h_val = int(now.strftime("%I"))
    m_val = int(now.strftime("%M"))
    s_val = int(now.strftime("%S"))

    rot_min = m_val * 6 * -1
    rot_sec = s_val * 6 * -1

    surf_min = pygame.transform.rotate(img_min, rot_min)
    surf_sec = pygame.transform.rotate(img_sec, rot_sec)
    
    screen.fill((255, 255, 255))
    screen.blit(img_main, (100, 100))
    
    pos_sec = (400 - surf_sec.get_width() // 2, 400 - surf_sec.get_height() // 2)
    pos_min = (400 - surf_min.get_width() // 2, 400 - surf_min.get_height() // 2)
    
    screen.blit(surf_sec, pos_sec)
    screen.blit(surf_min, pos_min)
    
    pygame.draw.circle(screen, (0, 0, 0), (400, 400), 22)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()