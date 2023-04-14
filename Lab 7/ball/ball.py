import pygame
pygame.init()

W = 600
H = 600

screen = pygame.display.set_mode((W, H))

color1 = (255, 255, 255)
color2 = (255, 0, 0)

x = 300
y = 300
r = 25

def draw_ball(x, y):
    pygame.draw.circle(screen, color2, (x, y), r)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 20
            elif event.key == pygame.K_RIGHT:
                x += 20
            elif event.key == pygame.K_UP:
                y -= 20
            elif event.key == pygame.K_DOWN:
                y += 20

    if x - r < 0:
        x = r
    elif x + r > W:
        x = H - r
    if y - r < 0:
        y = r
    elif y + r > W:
        y = H - r
    
    screen.fill(color1)
    draw_ball(x, y)
    pygame.display.update()
    