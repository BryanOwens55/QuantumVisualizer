# Imports
import pygame
from pygame.locals import *


def menu():

    # Start the Application
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    myfont = pygame.font.SysFont('Calibri', 30)
    myfont2 = pygame.font.SysFont('Calibri', 40)

    main_title_1 = myfont2.render('Welcome to The Quantum Visualizer', False, (0, 0, 0))
    title = myfont.render('Press Space to Start!', False, (255, 255, 255))
    title2 = myfont.render('Press Entre for some Quantum information!', False, (255, 255, 255))
    atom = pygame.image.load("images/atom.png")
    atom = pygame.transform.scale(atom, (200, 200))

    while 1:

        screen.fill((96,184,252))
        screen.blit(title, (200, 400))
        screen.blit(title2, (60, 440))
        screen.blit(main_title_1, (30, 40))
        screen.blit(atom, (218, 140))
        pygame.display.flip()

        for event in pygame.event.get():
            # Check for QUIT
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    import List_of_visualizers
                    List_of_visualizers.main_()
                if event.key == K_RETURN:
                    import QM_info
                    QM_info.main_()


menu()
