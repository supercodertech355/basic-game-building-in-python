import pygame
def main():
    pygame.init()
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Moving Circle and also colour changing sprite")

    colors = {
        'red': pygame.Color('red'),
        'green': pygame.Color('green'),
        'blue': pygame.Color('blue'),
        'yellow': pygame.Color('yellow'),
        'purple': pygame.Color('purple')
    }
    current_color = colors['purple']

    x,y = 30, 30
    sprite_width, sprite_height = 60, 60

    clock = pygame.time.Clock()

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    current_color = colors['red']
                elif event.key == pygame.K_g:
                    current_color = colors['green']
                elif event.key == pygame.K_b:
                    current_color = colors['blue']
                elif event.key == pygame.K_y:
                    current_color = colors['yellow']
                elif event.key == pygame.K_p:
                    current_color = colors['purple']

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 3
        if keys[pygame.K_RIGHT]:
            x += 3
        if keys[pygame.K_UP]:
            y -= 3
        if keys[pygame.K_DOWN]:
            y += 3

        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()

if __name__ == "__main__":
    main()