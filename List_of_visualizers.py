# Imports
import pygame
from pygame.locals import *
import numpy as np

def main_():


    # Initiate visuals
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    myfont = pygame.font.SysFont('Calibri', 40)
    myfont2 = pygame.font.SysFont('Calibri', 25)
    myfont3 = pygame.font.SysFont('Calibri', 15)

    main_title = myfont.render('Quantum Visualizer Modes:', False, (0, 0, 0))
    title2 = myfont2.render('1. Square Well Visualizer (1D)', False, (255, 255, 255))
    title3 = myfont2.render('2. Square Well Visualizer (2D)', False, (255, 255, 255))
    title4 = myfont2.render('3. ODE Visualizer (1st Order)', False, (255, 255, 255))
    title5 = myfont2.render('4. ODE Visualizer (2nd Order)', False, (255, 255, 255))
    title6 = myfont3.render('Esc to return', False, (255, 255, 255))

    while 1:

        active = False

        screen.fill((96,184,252))

        screen.blit(title2, (180, 300))
        screen.blit(title3, (180, 340))
        screen.blit(title4, (180, 380))
        screen.blit(title5, (180, 420))
        screen.blit(main_title, (100, 150))
        screen.blit(title6, (10, 10))
        pygame.display.flip()

        for event in pygame.event.get():
            # Check for QUIT
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            # Check for Keys
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    import Start
                    Start.menu()
                if event.key == K_1:
                    import Q_well_1D
                    Q_well_1D.main(1)
                if event.key == K_2:
                    import Q_well_2D
                    Q_well_2D.main(1,1)
                if event.key == K_3:
                    import ODE_1D
                    ODE_1D.main([0,1,2,3,4], [0,1,2,3,4])
                if event.key == K_4:
                    import ODE_2D
                    ODE_2D.main([0,1,2,3,4], [0,1,2,3,4])


main_()
