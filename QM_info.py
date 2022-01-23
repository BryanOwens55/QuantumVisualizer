# Imports
import pygame
from pygame.locals import *


def main_():
    # Initialize the game
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    myfont = pygame.font.SysFont('Calibri', 25)
    myfont2 = pygame.font.SysFont('Calibri', 35)
    myfont3 = pygame.font.SysFont('Calibri', 15)
    main_title_1 = myfont2.render('Welcome to The Quantum Information Tab!', False, (0, 0, 0))
    title = myfont.render('How does the O.D.E. math work?', False, (255, 255, 255))
    title2 = myfont.render('What is the quantum square well?', False, (255, 255, 255))
    title3 = myfont.render('What is the double slit experiment?', False, (255, 255, 255))
    title4 = myfont3.render('Esc to return', False, (255, 255, 255))

    while 1:
        screen.fill((96,184,252))
        screen.blit(title, (10, 300))
        screen.blit(title2, (10, 340))
        screen.blit(title4, (10, 10))
        screen.blit(main_title_1, (10, 70))
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # Check for QUIT
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    import Start
                    Start.menu()
                if event.key == K_1:
                    import Quantum_reading
                    Quantum_reading.main_(1)
                if event.key == K_2:
                    import Quantum_reading
                    Quantum_reading.main_(2)
                if event.key == K_3:
                    import Quantum_reading
                    Quantum_reading.main_(3)
                if event.key == K_4:
                    import Quantum_reading
                    Quantum_reading.main_(4)
                if event.key == K_5:
                    import Quantum_reading
                    Quantum_reading.main_(5)


main_()
