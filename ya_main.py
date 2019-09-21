import pygame

pygame.init()
coord_x = 210
coord_y = 500
coordTow_y = 700
pygame.display.set_caption("飞机大战")
mode = pygame.display.set_mode((480, 700))
bg = pygame.image.load("./images/background.png")
yingxiong = pygame.image.load("./images/life.png")
clock = pygame.time.Clock()

while True:
    clock.tick(60)
    mode.blit(bg, (0, 0))
    if coord_y > -57:
        mode.blit(yingxiong, (coord_x, coord_y))
        coord_y -= 1

    if -65 < coord_y < 0:
        mode.blit(yingxiong, (coord_x, coordTow_y))
        coordTow_y -= 1
        if coordTow_y == 625:
            coord_y = 625
            coordTow_y = 700
    pygame.display.update()
pygame.quit()
