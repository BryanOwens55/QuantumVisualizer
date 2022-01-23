# Imports
import pygame
from pygame.locals import *
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import numpy as np
from mpl_toolkits import mplot3d


matplotlib.use("Agg")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400


def main(m, n):
    pygame.init()
    width, height = 750, 400
    font1 = pygame.font.SysFont('Calibri', 15)
    font2 = pygame.font.SysFont('Calibri', 25)
    text1 = font1.render('Esc to return', False, (255, 0, 0))
    text2 = font2.render('Enter Energy Level (n):', False, (255, 255, 255))
    text3 = font2.render('Enter Energy Level (m):', False, (255, 255, 255))
    screen = pygame.display.set_mode((width, height))
    screen.fill((96, 184, 252))
    screen.blit(text1, (550, 10))
    screen.blit(text2, (410, 199))
    screen.blit(text3, (410, 249))

    # Making input field
    user_text1 = str(m)
    user_text2 = str(n)
    base_font = pygame.font.Font(None, 20)
    input_rect1 = pygame.Rect(650, 200, 50, 20)
    input_rect2 = pygame.Rect(650, 250, 50, 20)
    color_passive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('chartreuse4')
    color1 = color_passive
    color2 = color_passive
    active1 = False
    active2 = False

    L = 2 * np.pi
    A = (2/L) ** (1/2)  # Normalization
    x = np.linspace(0, L, 100) # x position
    y = np.linspace(0, L, 100) # x position
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y, m, n)

    fig = plt.figure(figsize=[4, 4], dpi=100)
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                    cmap='viridis', edgecolor='none');

    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()

    size = canvas.get_width_height()
    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, (0, 0))
    pygame.display.flip()

    while True:
        # Check For QUIT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

            # Check For Mouse Click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect1.collidepoint(event.pos):
                    active1 = True
                    color1 = color_active
                    active2 = False
                    color2 = color_passive
                elif input_rect2.collidepoint(event.pos):
                    active2 = True
                    color2 = color_active
                    active1 = False
                    color1 = color_passive
                else:
                    active1 = False
                    color1 = color_passive
                    active2 = False
                    color2 = color_passive

            # Check For Key Press
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    if user_text1.isnumeric() and user_text2.isnumeric():
                        matplotlib.pyplot.close('all')
                        main(int(user_text1), int(user_text2))
                    else:
                        print('Invalid Number')
                        user_text1 = str(m)
                        user_text2 = str(n)

                if event.key == K_ESCAPE:
                    import List_of_visualizers
                    List_of_visualizers.main_()

                if event.key == pygame.K_BACKSPACE and active1:
                    user_text1 = user_text1[:-1]
                elif event.key == pygame.K_BACKSPACE and active2:
                    user_text2 = user_text2[:-1]
                elif active1:
                    user_text1 += event.unicode
                elif active2:
                    user_text2 += event.unicode

        # Updating Text Field 1
        text_surface1 = base_font.render(user_text1, True, (255, 255, 255))
        pygame.draw.rect(screen, color1, input_rect1)
        screen.blit(text_surface1, (input_rect1.x + 5, input_rect1.y + 5))
        input_rect1.w = max(80, text_surface1.get_width() + 10)

        # Updating Text Field 2
        text_surface2 = base_font.render(user_text2, True, (255, 255, 255))
        pygame.draw.rect(screen, color2, input_rect2)
        screen.blit(text_surface2, (input_rect2.x + 5, input_rect2.y + 5))
        input_rect2.w = max(80, text_surface2.get_width() + 10)

        pygame.display.update()


def f(x, y, m, n):
    L = 2 * np.pi
    A = (2/L) ** (1/2)  # Normalization
    return A * np.sin(m*np.pi*x/L)*A * np.sin(n*np.pi*y/L)



main(5, 5)
