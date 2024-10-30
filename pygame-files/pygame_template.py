import pygame

pygame.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


circle_x = 200
circle_y = 200


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255)) 

    pygame.draw.circle(screen, (0, 0, 255), (circle_x, circle_y), 30)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()