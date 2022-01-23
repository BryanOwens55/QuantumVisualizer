# Imports
import pygame
from pygame.locals import *



def main_(num):
    # Initialize the game
    pygame.init()
    width, height = 640, 600
    screen = pygame.display.set_mode((width, height))
    myfont = pygame.font.SysFont('Calibri', 20)
    titlefont = pygame.font.SysFont('Calibri', 35)
    myfont3 = pygame.font.SysFont('Calibri', 15)

    # For Question 1
    Q1_1 = myfont.render('How does the math work?', False, (255, 255, 255))

    # For Question 2
    Q2_1 = titlefont.render('What is the quantum square well?', False, (255, 255, 255))
    Q2_2 = myfont.render('The quantum square well is a potential (energy) well. In the case that is used',
                         False, (255, 255, 255))
    Q2_3 = myfont.render('in this application the potential is set to 0 inside the well and infinite out-',
                         False, (255, 255, 255))
    Q2_4 = myfont.render('side the well. This causes the particle to be completly trapped and therefore',
                         False, (255, 255, 255))
    Q2_5 = myfont.render('the potential acts like a well.',
                         False, (255, 255, 255))

    Q3_1 = titlefont.render('How Does the Math Work?', False, (255, 255, 255))
    Q3_2 = myfont.render('The following is Schrodinger Equation for the square well:',
                         False, (255, 255, 255))
    Q3_3 = myfont.render('The following is the recursion formula for Euler Method:',
                         False, (255, 255, 255))
    Q3_4 = myfont.render('The following is the recursion formula for RK2 Method:',
                         False, (255, 255, 255))
    Q3_5 = myfont.render('The following is the recursion formula for RK4 Method:',
                         False, (255, 255, 255))

    SE = pygame.image.load("images/schrodinger1.png")
    SE = pygame.transform.smoothscale(SE, (180, 80))

    well = pygame.image.load("images/square_well2.png")
    well = pygame.transform.smoothscale(well, (160, 200))

    Euler = pygame.image.load("images/Euler.png")
    Euler = pygame.transform.smoothscale(Euler, (160, 25))

    RK2 = pygame.image.load("images/RK2.png")
    RK2 = pygame.transform.smoothscale(RK2, (160, 80))

    RK4 = pygame.image.load("images/RK4.png")
    RK4 = pygame.transform.smoothscale(RK4, (210, 165))

    # For Question 3
    Q3 = myfont.render('What is the double slit experiment?', False, (255, 255, 255))
    Q4 = myfont3.render('Esc to return', False, (255, 255, 255))
    Q5 = myfont3.render('Secret Q5!', False, (255, 255, 255))

    while 1:
        screen.fill((96, 184, 252))

        if num == 1:
            screen.blit(Q3_1, (80, 10))
            screen.blit(Q3_2, (10, 90))
            screen.blit(Q3_3, (10, 220))
            screen.blit(Q3_4, (10, 290))
            screen.blit(Q3_5, (10, 400))

            screen.blit(SE, (10, 120))
            screen.blit(Euler, (10, 250))
            screen.blit(RK2, (10, 310))
            screen.blit(RK4, (10, 420))

            screen.blit(Q4, (540, 10))

        elif num == 2:
            screen.blit(Q2_1, (10, 10))
            screen.blit(Q2_2, (10, 150))
            screen.blit(Q2_3, (10, 180))
            screen.blit(Q2_4, (10, 210))
            screen.blit(Q2_5, (10, 240))
            screen.blit(well, (240, 300))
            screen.blit(Q4, (540, 10))

        elif num == 5:
            screen.blit(Q5, (10, 70))
            screen.blit(Q4, (540, 10))

        else:
            screen.blit(Q3_1, (80, 10))
            screen.blit(Q3_2, (10, 90))
            screen.blit(Q3_3, (10, 220))
            screen.blit(Q3_4, (10, 290))
            screen.blit(Q3_5, (10, 400))

            screen.blit(SE, (10, 120))
            screen.blit(Euler, (10, 250))
            screen.blit(RK2, (10, 310))
            screen.blit(RK4, (10, 420))

            screen.blit(Q4, (540, 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Check for QUIT
                pygame.quit()
                exit(0)

            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    import QM_info
                    QM_info.main_()


