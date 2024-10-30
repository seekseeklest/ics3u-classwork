import pygame

pygame.init()

#colors
sky_blue = (1, 0, 51)
brick_red = (126, 43, 28)
grass_green = (124, 252, 0)
pumpkin_orange = (248, 114, 23)

circle1_x = 150
circle1_y = 120
circle2_x = 180
circle2_y = 120

width = 1000
height = 600

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

n = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(sky_blue)

    pygame.draw.rect(screen, brick_red, (200, 300, 200, 200))
    pygame.draw.rect(screen, grass_green, (0, 500, 1000, 100))
    moon = pygame.draw.circle(screen, (218, 238, 242), (circle1_x, circle1_y), 50)
    moon_shadow = pygame.draw.circle(screen, sky_blue, (circle2_x, circle2_y), 50)


    if circle1_x == 150:
        while n <= 5:
            circle2_y += 5
            n += 1

            if circle1_x < (width/2):
                circle1_x += 1
                circle2_x += 1
   


    pygame.display.flip()
    clock.tick(30)

pygame.quit()