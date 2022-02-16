#! /usr/bin/python
import pygame
import numpy as np
from math import pi
import sys
__all__ = ["pygame", "sys"]



def update(dots, nextDots, start): #applying rules and update cells
    if not start:
        return nextDots
    for i in range(height):
        for j in range(width):
            around = 0
            if i == 0 and j == 0:
                if dots[i+1][j]:
                    around += 1
                if dots[i+1][j+1]:
                    around += 1
                if dots[i][j+1]:
                    around += 1
            elif i == height - 1 and j == 0:
                if dots[i-1][j]:
                    around += 1
                if dots[i-1][j+1]:
                    around += 1
                if dots[i][j+1]:
                    around += 1
            elif i == 0 and j == width - 1:
                if dots[i+1][j]:
                    around += 1
                if dots[i+1][j-1]:
                    around += 1
                if dots[i][j-1]:
                    around += 1
            elif i == height - 1 and j == width - 1:
                if dots[i-1][j]:
                    around += 1
                if dots[i-1][j-1]:
                    around += 1
                if dots[i][j-1]:
                    around += 1
            elif i == 0:
                if dots[i+1][j-1]:
                    around += 1
                if dots[i+1][j]:
                    around += 1
                if dots[i+1][j+1]:
                    around += 1
                if dots[i][j+1]:
                    around += 1
                if dots[i][j-1]:
                    around += 1
            elif i == height -1:
                if dots[i-1][j-1]:
                    around += 1
                if dots[i-1][j]:
                    around += 1
                if dots[i-1][j+1]:
                    around += 1
                if dots[i][j+1]:
                    around += 1
                if dots[i][j-1]:
                    around += 1
            elif j == 0:
                if dots[i + 1][j + 1]:
                    around += 1
                if dots[i][j + 1]:
                    around += 1
                if dots[i - 1][j + 1]:
                    around += 1
                if dots[i + 1][j]:
                    around += 1
                if dots[i - 1][j]:
                    around += 1
            elif j == width - 1:
                if dots[i + 1][j - 1]:
                    around += 1
                if dots[i][j - 1]:
                    around += 1
                if dots[i - 1][j - 1]:
                    around += 1
                if dots[i + 1][j]:
                    around += 1
                if dots[i - 1][j]:
                    around += 1
            else:
                if dots[i + 1][j + 1]:
                    around += 1
                if dots[i][j + 1]:
                    around += 1
                if dots[i - 1][j + 1]:
                    around += 1
                if dots[i + 1][j - 1]:
                    around += 1
                if dots[i][j - 1]:
                    around += 1
                if dots[i - 1][j - 1]:
                    around += 1
                if dots[i + 1][j]:
                    around += 1
                if dots[i - 1][j]:
                    around += 1
            if dots[i][j] == 1 and around < 2:
                nextDots[i][j] = 0
            elif dots[i][j] == 1 and (around == 2 or around == 3):
                nextDots[i][j] = 1
            elif dots[i][j] == 1 and around > 3:
                nextDots[i][j] = 0
            elif dots[i][j] == 0 and around == 3:
                nextDots[i][j] = 1
            else:
                nextDots[i][j] = nextDots[i][j]
    return nextDots
def draw(nextDots, dots): #modifed cells based on given dots
    try:
        for dot in dots:
            nextDots[dot[0]][dot[1]] = 1
    except IndexError:
        pass
    return nextDots
def drawGlider(nextDots, event): #draw glider at given position
    x, y = event.pos[1]//zoomRate, event.pos[0]//zoomRate #given position
    dots = np.array([[1, 0], [0, 1], [-1, -1], [-1, 0], [-1, 1]]) #pixels of glider
    dots = dots + [x, y]
    return draw(nextDots, dots)
def drawGosperGliderGun(nextDots, event): #draw Gosper Glider gun at given position
    x, y = event.pos[1]//zoomRate, event.pos[0]//zoomRate
    dots = np.array([[0, 0], [-1, 1], [-1, 0], [-1, -1], [-2, 2], [-2, -2], [-3, 0], [-4, 3], [-4, -3], [-5, 3], [-5, -3], [-6, 2], [-6, -2], [-7, 1], [-7, 0], [-7, -1], [-16, 1], [-16, 0], [-17, 1], [-17, 0], [3, 1], [3, 2], [3, 3], [4, 1], [4, 2], [4, 3], [5, 0], [5, 4], [7, -1], [7, 0], [7, 4], [7, 5], [17, 2], [17, 3], [18, 2], [18, 3]])
    dots = dots + [x, y]
    return draw(nextDots, dots)
def drawSimkinGliderGun(nextDots, event): #draw Simkin Glider Gun at given position
    x, y = event.pos[1]//zoomRate, event.pos[0]//zoomRate
    dots = np.array([[0, 0], [0, 1], [0, 2], [1, 0], [1, 3], [2, 0], [2, 3], [4, 3], [5, -1], [5, 3], [6, 0], [6, 2], [7, 1], [10, 0], [10, 1], [11, 0], [11,1], [0, -5], [-1, -5], [-1, -6], [0, -7], [1, -7], [2, -7], [2, -8], [-13, 11], [-13, 12], [-14, 11], [-14, 12], [-16, 8], [-16, 9], [-17, 8], [-17, 9], [-20, 11], [-20, 12], [-21, 11], [-21, 12]])
    dots = dots + [x, y]
    return draw(nextDots, dots)
def drawTurtle(nextDots, event): #draw turtle at given position
    x, y = event.pos[1]//zoomRate, event.pos[0]//zoomRate
    dots = np.array([[0, 3], [0, 2], [0, 0], [0, -1], [0, -3], [0, -4], [1, 1], [1, -2], [2, 3], [2, -4], [3, 3], [3, -4], [5, 3], [5, 2], [5, 1], [5, 0], [5, -1], [5, -2], [5, -3], [5, -4], [6, 4], [6, 3], [6, -4], [6, -5], [-1, 2], [-1, 1], [-1, -2], [-1, -3], [-2, 4], [-2, 2], [-2, -3], [-2, -5], [-3, 4], [-3, 3], [-3, -4], [-3, -5], [-4, 4], [-4, 3], [-4, 1], [-4, -2], [-4, -4], [-4, -5], [-5, 0], [-5, -1]])
    dots = dots + [x, y]
    return draw(nextDots, dots)




pygame.init()
vInfo = pygame.display.Info()
size = [width, height] = np.array([160, 90])
zoomRate = 6
screen = pygame.display.set_mode((width * zoomRate, (height+10) * zoomRate))
zoom = pygame.Surface(size)
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 15) #construct a font
clear = font.render('Clear' , True , (255, 255, 255)) #render the text
glider = font.render('Glider' , True , (255, 255, 255))
GosperGliderGun = font.render('Gosper Glider Gun' , True , (255, 255, 255))
SimkinGliderGun = font.render('Simkin Glider Gun' , True , (255, 255, 255))
turtle = font.render('Turtle' , True , (255, 255, 255))


dots = np.array([[0]*width for i in range(height)])
nextDots = np.array([[0]*width for i in range(height)])
for i in range(height):
    for j in range(width):
        dots[i][j] = 0
        nextDots[i][j] = 0


start = False #start moving or pause
graph = '' #which graph to draw(glider, glider gun, turtle)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN: #press blankspace to start/pause
            if event.key == pygame.K_SPACE:
                 start = not start
        elif event.type == pygame.MOUSEBUTTONDOWN: #click left key of mouse
				#detect if user click on a buttons
            if clearX-5 <= mousePos[0] <= clearX-5+80 and clearY <= mousePos[1] <= clearY+25:
                nextDots = np.zeros(nextDots.shape)
                dots = np.zeros(nextDots.shape)
            elif gliderX-5 <= mousePos[0] <= gliderX-5+90 and gliderY <= mousePos[1] <= gliderY+25:
                graph = '' if graph == 'glider' else 'glider'
            elif GosperGliderGunX-5 <= mousePos[0] <= GosperGliderGunX-5+240 and GosperGliderGunY <= mousePos[1] <= GosperGliderGunY+25:
                graph = '' if graph == 'glider gun' else 'glider gun'
            elif SimkinGliderGunX-5 <= mousePos[0] <= SimkinGliderGunX-5+240 and SimkinGliderGunY <= mousePos[1] <= SimkinGliderGunY+25:
                graph = '' if graph == 'glider gun2' else 'glider gun2'
            elif turtleX-5 <= mousePos[0] <= turtleX-5+90 and turtleY <= mousePos[1] <= turtleY+25:
                graph = '' if graph == 'turtle' else 'turtle'
            else:
                if event.button == 1:
                    if graph == 'glider':
                        drawGlider(nextDots, event)
                    elif graph == 'glider gun':
                        drawGosperGliderGun(nextDots, event)
                    elif graph == 'glider gun2':
                        drawSimkinGliderGun(nextDots, event)
                    elif graph == 'turtle':
                        drawTurtle(nextDots, event)
                    else:
                        #default: draw a pixel
                        try:
                            nextDots[event.pos[1]//zoomRate][event.pos[0]//zoomRate] = 1
                        except IndexError:
                            pass	
				#continuously draw with the mouse's movement
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1 and graph == '':
                try:
                    nextDots[event.pos[1]//zoomRate][event.pos[0]//zoomRate] = 1
                except IndexError:
                    pass

    nextDots = update(dots, nextDots, start)

	#draw on GUI
    for i in range(height):
        for j in range(width):
            dots[i][j] = nextDots[i][j]
            if dots[i][j] == 0:
                zoom.fill((255, 255, 255), ((j, i), (1, 1)))
            elif dots[i][j] == 1:
                zoom.fill((0, 0, 0), ((j, i), (1, 1)))


    mousePos = pygame.mouse.get_pos()



	#draw buttons
    clearX, clearY = 10, (height+3)*zoomRate
    if (clearX-5 <= mousePos[0] <= clearX-5+80 and clearY <= mousePos[1] <= clearY+25):
        pygame.draw.rect(screen, (204, 41, 0), [clearX-5, clearY,80,25])
    else:
        pygame.draw.rect(screen, (128, 26, 0), [clearX-5, clearY,80,25])
    screen.blit(clear, (clearX, clearY))

    gliderX, gliderY = 100, (height+3)*zoomRate
    if (gliderX-5 <= mousePos[0] <= gliderX-5+90 and gliderY <= mousePos[1] <= gliderY+25) or graph == 'glider':
        pygame.draw.rect(screen, (115, 115, 115), [gliderX-5, gliderY,90,25])
    else:
        pygame.draw.rect(screen, (77, 77, 77), [gliderX-5, gliderY,90,25])
    screen.blit(glider, (gliderX, gliderY))

    GosperGliderGunX, GosperGliderGunY = 210, (height+3)*zoomRate
    if (GosperGliderGunX-5 <= mousePos[0] <= GosperGliderGunX-5+240 and GosperGliderGunY <= mousePos[1] <= GosperGliderGunY+25) or graph == 'glider gun':
        pygame.draw.rect(screen, (115, 115, 115), [GosperGliderGunX-5, GosperGliderGunY,240,25])
    else:
        pygame.draw.rect(screen, (77, 77, 77), [GosperGliderGunX-5, GosperGliderGunY,240,25])
    screen.blit(GosperGliderGun, (GosperGliderGunX, GosperGliderGunY))

    SimkinGliderGunX, SimkinGliderGunY = 480, (height+3)*zoomRate
    if (SimkinGliderGunX-5 <= mousePos[0] <= SimkinGliderGunX-5+240 and SimkinGliderGunY <= mousePos[1] <= SimkinGliderGunY+25) or graph == 'glider gun2':
        pygame.draw.rect(screen, (115, 115, 115), [SimkinGliderGunX-5, SimkinGliderGunY,240,25])
    else:
        pygame.draw.rect(screen, (77, 77, 77), [SimkinGliderGunX-5, SimkinGliderGunY,240,25])
    screen.blit(SimkinGliderGun, (SimkinGliderGunX, SimkinGliderGunY))

    turtleX, turtleY =730, (height+3)*zoomRate
    if (turtleX-5 <= mousePos[0] <= turtleX-5+90 and turtleY <= mousePos[1] <= turtleY+25) or graph == 'turtle':
        pygame.draw.rect(screen, (115, 115, 115), [turtleX-5, turtleY,90,25])
    else:
        pygame.draw.rect(screen, (77, 77, 77), [turtleX-5, turtleY,90,25])
    screen.blit(turtle, (turtleX, turtleY))


    screen.blit(pygame.transform.scale(zoom, size*zoomRate), (0, 0))
    pygame.display.update()
    clock.tick(60)
