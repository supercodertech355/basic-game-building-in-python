import pygame

pygame.init()
window = pygame.display.set_mode((400, 400))
window.fill((255, 255, 255))
green = (0, 225, 0)
pygame.draw.circle(window, green, (200, 200), 50)
pygame.draw.circle(window, green, (300, 300), 50, 3)
pygame.display.update()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()