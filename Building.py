import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((1000, 800))
r = pygame.Rect(300, 300, 400, 400)
pygame.draw.rect(screen, (255, 200, 0), r, 0)

r = pygame.Rect(350, 450, 40, 40)
pygame.draw.rect(screen, (0, 0, 0), r, 0)

r = pygame.Rect(400, 450, 40, 40)
pygame.draw.rect(screen, (0, 0, 0), r, 0)

r = pygame.Rect(350, 500, 90, 120)
pygame.draw.rect(screen, (0, 0, 0), r, 0)

r = pygame.Rect(500, 500, 90, 200)
pygame.draw.rect(screen, (0, 50, 255), r, 0)

points = [(200, 300), (500, 100), (800, 300)]
pygame.draw.polygon(screen, (255, 0, 0), points)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()