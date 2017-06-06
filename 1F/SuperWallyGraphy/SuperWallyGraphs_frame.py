import pygame
import math
pygame.init()
size = width, height = (600,500)
area = pygame.display.set_mode(size)
area.fill((255,255,255))
Clock = pygame.time.Clock()
font = pygame.font.SysFont('arial',20)
last_pos = None
done = False


########### Variabili ##########################################################

BLACK = (0,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
function = input("y = ")
eq_0x = width//2
eq_0y = height//2
u = 20

########### Funzioni ###########################################################

def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y),0)

def event_loop():
    global u
    global done
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_PLUS:
                u += 5
            if event.key == pygame.K_MINUS and u != 5:
                u -= 5
                

def draw_graph():
    for x in range(width*10):
        global function
            
        real_x = x/10
        x = -((eq_0x - real_x)/u)
        y = eval(function)
        real_y = height-(int(y * u) + eq_0y)
        #print(y)
        area.set_at((math.floor(real_x),real_y),BLUE)
        

def main_loop():
    while not done:
        area.fill(WHITE)
        draw_graph()
        event_loop()
        pygame.display.flip()
    pygame.quit()
                
function = function.replace('^','**')
function = function.replace('cos(','math.cos(')
function = function.replace('sin(','math.sin(')
function = function.replace('tan(','math.tan(')
function = function.replace('pi','math.pi')
function = function.replace('e','math.e')
function = function.replace(':','/')
    
main_loop()

