try:
    import pygame
    import time
    import math

    pygame.init()
    pygame.font.init
    screen = pygame.display.set_mode((500, 600))

    GREY = (150, 150, 150)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    font = pygame.font.SysFont('sans', 40)
    text_1 = font.render('+', True, BLACK)
    text_2 = font.render('+', True, BLACK)
    text_3 = font.render('START', True, BLACK)
    text_4 = font.render('-', True, BLACK)
    text_5 = font.render('-', True, BLACK)
    text_6 = font.render('RESET', True, BLACK)

    running = True
    total_secs = 0
    total = 0
    start = False
    r_sec = 90
    r_min = 50

    clock = pygame.time.Clock()

    while running:
        clock.tick(60)
        screen.fill(GREY)
        sound = pygame.mixer.Sound('countdown.wav')
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #draw button
        pygame.draw.rect(screen, WHITE, (100, 50, 50, 50)) # x, y, width, height
        pygame.draw.rect(screen, WHITE, (200, 50, 50, 50))
        pygame.draw.rect(screen, WHITE, (300, 50, 150, 50))
        pygame.draw.rect(screen, WHITE, (100, 200, 50, 50))
        pygame.draw.rect(screen, WHITE, (200, 200, 50, 50))
        pygame.draw.rect(screen, WHITE, (300, 200, 150, 50))

        screen.blit(text_1, (113, 53))  
        screen.blit(text_2, (213, 53)) 
        screen.blit(text_3, (310, 58)) 
        screen.blit(text_4, (118, 205)) 
        screen.blit(text_5, (218, 205)) 
        screen.blit(text_6, (310, 208)) 

        pygame.draw.rect(screen, BLACK, (55, 525, 390, 40))
        pygame.draw.rect(screen, WHITE, (60, 530, 380, 30))

        # draw clock
        pygame.draw.circle(screen, BLACK, (250, 400), 100)
        pygame.draw.circle(screen, WHITE, (250, 400), 95)
        pygame.draw.circle(screen, BLACK, (250, 400), 5)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.pause()
                    if (100 < mouse_x < 150) and (50 < mouse_y < 100):
                        total_secs += 60
                        total = total_secs
                        print("press + minute")
                    if (200 < mouse_x < 250) and (50 < mouse_y < 100):
                        total_secs += 1
                        total = total_secs
                        print("press + second")
                    if (300 < mouse_x < 450) and (50 < mouse_y < 100):
                        total = total_secs
                        start = True
                        print("total_secs: " + str(total_secs))
                        print("press Start")
                    if (100 < mouse_x < 150) and (200 < mouse_y < 250):
                        total_secs -= 60
                        total = total_secs
                        print("press - minute")
                    if (200 < mouse_x < 250) and (200 < mouse_y < 250):
                        total_secs -= 1
                        total = total_secs
                        print("press - second")
                    if (300 < mouse_x < 450) and (200 < mouse_y < 250):
                        total_secs = 0
                        start = False
                        print("press Reset")

        if start:
            total_secs -= 1
            if total_secs == 0:
                print("THE END")
                pygame.mixer.Sound.play(sound)
            time.sleep(1)
        
        if total_secs < 0:
            start = False
            total = 0
            total_secs = 0

        secs = total_secs % 60
        mins = (total_secs - secs) / 60
        mins = int(mins)

        time_now = str(mins) + " : " + str(secs)
        text_time = font.render(time_now, True, BLACK)
        screen.blit(text_time, (120, 120))

        x_sec = 250 + int(r_sec * math.sin(6 * secs * math.pi / 180))
        y_sec = 400 - int(r_sec * math.cos(6 * secs * math.pi / 180))
        pygame.draw.line(screen, BLACK, (250, 400), (int(x_sec), int(y_sec)))

        x_min = 250 + int(r_min * math.sin(6 * mins * math.pi / 180))
        y_min = 400 - int(r_min * math.cos(6 * mins * math.pi / 180))
        pygame.draw.line(screen, RED, (250, 400), (int(x_min), int(y_min)))

        if total != 0:
            pygame.draw.rect(screen, RED, (60, 530, int(380 * (total_secs/total)), 30))

        pygame.display.flip()

    pygame.quit()

except Exception as bug:
    print(bug)

input()