import pygame

pygame.init()
mode = pygame.display.set_mode((480, 700))

bg = pygame.image.load("./images/background.png")
mode.blit(bg, (0, 0))
pygame.display.update()
i = 1
while True:
    pygame.time.delay(1000)
    i += 1
    print(i)
pygame.quit()
