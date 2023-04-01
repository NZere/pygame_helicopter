import pygame

pygame.init()  # initialize
size = (700, 500)
screen_width = size[0]
screen_height = size[1]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('N-game')
clock = pygame.time.Clock()

heli_right = pygame.image.load("heli_right.png")
heli_right = pygame.transform.scale(heli_right, (screen_width//10, screen_width//10))

heli_left = pygame.image.load("heli_left.png")
heli_left = pygame.transform.scale(heli_left, (screen_width//10, screen_width//10))

background_image = pygame.image.load("plx-5.png")
background_image = pygame.transform.scale(background_image, size)


x = screen_width//2 - screen_width//20
y = screen_height//2 - screen_height//20

dx = 0
dy = 0

flying_up = False
heading_right = True

rect_platforms = [
    pygame.Rect(0, 0, 40, 500),
    pygame.Rect(400, 400, 100, 40),
    pygame.Rect(0, 460, 500, 40)
]

game_over = False
while not game_over:
    if flying_up:
        dy -= 0.8
    else:
        dy += 0.5
        if dy > 10:
            dy = 10

    x += dx
    heli_rect = pygame.Rect(x, y, screen_width//10, screen_width//12)
    for platform in rect_platforms:
        if heli_rect.colliderect(platform):
            x -= dx

    y += dy
    heli_rect = pygame.Rect(x, y, screen_width // 10, screen_width // 12)
    for platform in rect_platforms:
        if heli_rect.colliderect(platform):
            y -= dy
            dy = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                heading_right = True
                dx = 7
            if event.key == pygame.K_LEFT:
                heading_right = False
                dx = -7
            if event.key == pygame.K_UP:
                flying_up = True
            if event.key == pygame.K_DOWN:
                dy = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                if dx > 0:
                    dx = 0
            if event.key == pygame.K_LEFT:
                if dx < 0:
                    dx = 0
            if event.key == pygame.K_UP:
                flying_up = False
            if event.key == pygame.K_DOWN:
                if dy > 0:
                    dy = 0
    screen.fill((255, 255, 255))
    screen.blit(background_image, (0, 0))
    for platform in rect_platforms:
        pygame.draw.rect(screen, (0, 0, 255), platform)

    if heading_right:
        screen.blit(heli_right, (x, y))
    else:
        screen.blit(heli_left, (x, y))
    pygame.display.flip()
    clock.tick(20)

pygame.quit()
