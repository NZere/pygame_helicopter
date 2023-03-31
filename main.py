import pygame

pygame.init()  # initialize
size = (700, 500)
screen_width = size[0]
screen_height = size[1]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('N-game')
clock = pygame.time.Clock()

heli = pygame.image.load("heli_right.png")
heli = pygame.transform.scale(heli, (screen_width//10, screen_width//10))

background_image = pygame.image.load("plx-5.png")
background_image = pygame.transform.scale(background_image, size)


x = screen_width//2 - screen_width//20
y = screen_height//2 - screen_height//20

dx = 0
dy = 0
game_over = False
while not game_over:
    x += dx
    y += dy
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dx = 10
            if event.key == pygame.K_LEFT:
                dx = -10
            if event.key == pygame.K_UP:
                dy = -10
            if event.key == pygame.K_DOWN:
                dy = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                dy = 0
    screen.fill((255, 255, 255))
    screen.blit(background_image, (0, 0))
    screen.blit(heli, (x, y))
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
