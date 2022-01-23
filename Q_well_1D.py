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


def main(num):
    pygame.init()
    width, height = 750, 400
    font1 = pygame.font.SysFont('Calibri', 15)
    font2 = pygame.font.SysFont('Calibri', 25)
    text1 = font1.render('Esc to return', False, (255, 0, 0))
    text2 = font2.render('Enter Energy Level (n):', False, (255, 255, 255))
    screen = pygame.display.set_mode((width, height))
    screen.fill((96, 184, 252))
    screen.blit(text1, (550, 10))
    screen.blit(text2, (410, 199))

    # Making input field
    user_text = ''
    base_font = pygame.font.Font(None, 20)
    input_rect = pygame.Rect(650, 200, 50, 20)
    color_passive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('chartreuse4')
    color = color_passive
    active = False

    # Math for 1D Well
    L = 2 * np.pi
    x = np.linspace(0, L, 1000) # x position
    A = (2/L) ** (1/2)  # Normalization
    y = A * np.sin(num*np.pi*x/L)

    # Setting Up the Graph To Display Onto Pygame
    fig = plt.figure(figsize=[4, 4], dpi=100)
    ax = plt.axes()
    ax.plot(x, y)
    canvas = agg.FigureCanvasAgg(fig)
    canvas.draw()
    renderer = canvas.get_renderer()
    raw_data = renderer.tostring_rgb()
    size = canvas.get_width_height()
    surf = pygame.image.fromstring(raw_data, size, "RGB")
    screen.blit(surf, (0, 0))
    pygame.display.flip()

    while True:
        # drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                    color = color_active
                else:
                    active = False
                    color = color_passive
            if event.type == pygame.KEYDOWN:
                if event.key == K_RETURN:
                    if user_text.isnumeric():
                        matplotlib.pyplot.close('all')
                        main(num=int(user_text))
                    else:
                        print('Invalid Number')
                        user_text = ""

                if event.key == K_ESCAPE:
                    import List_of_visualizers
                    List_of_visualizers.main_()

                if event.key == pygame.K_BACKSPACE and active:
                    user_text = user_text[:-1]
                elif active:
                    user_text += event.unicode

        # Updating Text Field
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        pygame.draw.rect(screen, color, input_rect)
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(80, text_surface.get_width() + 10)

        pygame.display.update()


def f(x, y, num):
    L = 2 * np.pi
    A = (2/L) ** (1/2)  # Normalization
    return A * np.sin(num*np.pi*x/L)*A * np.sin(num*np.pi*y/L)


def inf_square_well(n, m):
    x = np.linspace(0, L, 100) # x position
    y = np.linspace(0, L, 100) # x position

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y, n, m)
    return X, Y, Z


main(5)
