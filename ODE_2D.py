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



def main(x,y):
    pygame.init()
    width, height = 750, 400
    font1 = pygame.font.SysFont('Calibri', 15)
    font2 = pygame.font.SysFont('Calibri', 25)
    font3 = pygame.font.SysFont('Calibri', 20)
    enter_text = 'Enter values (x_0, y_0, N, Solver,'
    enter_text1_5 = 'end point):'
    enter_text2 = '(RK2 (1), RK4 (2), Euler (3))'

    text1 = font1.render('Esc to return', False, (255, 0, 0))
    text2 = font2.render(enter_text, False, (255, 255, 255))
    text2_5 = font2.render(enter_text1_5, False, (255, 255, 255))
    text3 = font3.render(enter_text2, False, (255, 255, 255))
    screen = pygame.display.set_mode((width, height))
    screen.fill((96, 184, 252))
    screen.blit(text1, (550, 10))
    screen.blit(text2, (410, 179))
    screen.blit(text2_5, (410, 207))
    screen.blit(text3, (410, 240))

    # Making input field
    user_text = ''
    base_font = pygame.font.Font(None, 20)
    input_rect = pygame.Rect(410, 270, 60, 20)
    color_passive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('chartreuse4')
    color = color_passive
    active = False

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

                    numbers = user_text.split(',')
                    active = False
                    color = color_passive
                    user_text = ''
                    print(numbers)
                    x_0 = int(numbers[0])
                    y_0 = int(numbers[1])
                    n = int(numbers[2])
                    b = int(numbers[4])
                    ODE_solver = int(numbers[3])
                    t, x, y = ODE(n, x_0, y_0, ODE_solver, b)
                    main(t, x)

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


def f(r,t):
    """
    Function representing the ODE
    Includes some 1st order and 2nd order examples/tests
    """
    g = 9.81
    l = 0.1
    theta = r[0]
    w = r[1]
    ftheta = w
    fw = (-g / l) * np.sin(theta)
    return np.array([ftheta, fw], float)
    # return ode


"""
Define ODE and solving methods
"""

# DEFINE GENERALIZED ODE SOLVER FUNCTIONS
def euler(x_0,y_0,b,a,N):
    """
    Performs euler estimation of ode
    """

    h = (b-a)/N
    t_array = np.arange(a,b,h)
    x_array = []
    y_array = []
    r = [x_0,y_0]
    for t in t_array:
        x_array.append(r[0])
        y_array.append(r[1])
        r = np.add(r,h*f(r,t))
    return t_array, x_array, y_array


def rk2(x_0,y_0,b,a,N):
    """
    """
    r = [x_0,y_0]
    h = (b-a)/N
    t_array = np.arange(a,b,h)
    x_array = []
    y_array = []
    for t in t_array:
        x_array.append(r[0])
        y_array.append(r[1])
        k1 = h*f(r,t)
        k2 = h*f([r[0]+0.5*k1[0],r[1]+0.5*k1[1]],t+0.5*h)
        r = np.add(r,k2)
        print(t)
    return t_array, x_array, y_array

def rk4(x_0,y_0,b,a,N):
    """
    """
    r = [x_0,y_0]
    h = (b-a)/N
    t_array = np.arange(a,b,h)
    x_array = []
    y_array = []
    for t in t_array:
        x_array.append(r[0])
        y_array.append(r[1])
        k1 = h*f(r,t)
        k2 = h*f(np.add(r,0.5*k1),t+0.5*h)
        k3 = h*f(np.add(r,0.5*k2),t+0.5*h)
        k4 = h*f(np.add(r,k3),t+h)
        r = np.add(r,(1/6)*(k1 + 2*k2 + 2*k3 + k4))
    return t_array, x_array, y_array

def ODE(N, x_0, y_0, ode_type, b):

    a = 0
    if b < a:
        a, b = b, a
    if ode_type == 1:
        return rk2(x_0, y_0, b, a, N)
    elif ode_type == 2:
        return rk4(x_0, y_0, b, a, N)
    else:
        return euler(x_0, y_0, b, a, N)


main([0,1,2,3,4,5], [0,1,2,3,4,5])