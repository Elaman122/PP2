import pygame

pygame.init()

window = pygame.display.set_mode((500, 300))

color1 = (64,224,197)

pygame.mixer.init()

pygame.mixer.music.load("EDWXRDX_-_ZEMLYA_(musmore.com).mp3")

pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("TRITICUM_-_NOSTALGIA_(musmore.com).mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                pygame.mixer.music.stop()
                pygame.mixer.music.load("Dan_Korshunov_-_Na_Zare_(musmore.com).mp3")
                pygame.mixer.music.play()
            elif event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()
                pygame.quit()
                exit()

    window.fill(color1)
    pygame.display.update()