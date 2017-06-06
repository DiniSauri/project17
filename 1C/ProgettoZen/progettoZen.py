import pygame
import random
# grandezza schermo
x_max = 600 
y_max = 500

# variabili per palla
p_x = 300    # posizione x della palla
p_y = 100    # posizione y della palla
p_raggio = 30
p_r = 55 # red
p_g = 130 # green 
p_b = 217 # blue
p_velx = 5
p_vely = 5
# variabili per barra
b_x = 300       # coordinata x della barra
b_y = 450       # coordinata y della barra
b_l = 80        # lunghezza della barra
b_spessore = 20 # spessore della barra 

acc_1 = 0

pygame.init()
pygame.key.set_repeat(1,10)

area = pygame.display.set_mode((x_max, y_max))
perso = False 
while not perso:
    
    area.fill((0,0,0))
    palla = pygame.draw.circle(area, (p_r, p_g, p_b), (p_x, p_y), p_raggio, 0)
    palla1 = None
    barra = pygame.draw.line(area, (255, 255, 255), (b_x, b_y), (b_x+b_l, b_y), b_spessore)
   

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit() # usciamo dal gioco
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
               b_x = b_x - 7
            if evento.key == pygame.K_RIGHT:
                b_x = b_x + 7
    if p_x > x_max - p_raggio:
        p_velx = -5 #random.randrange(-5, 0)
    elif p_x < p_raggio :
        p_velx = 5 #random.randrange(3, 10)
    elif p_y < p_raggio:
        p_vely = 5 #random.randrange(3, 10)
    elif p_y > y_max - p_raggio:
        p_vely = - 5    
    if palla.colliderect(barra):
        p_vely = -p_vely
        acc_1 = acc_1 +1
        print(acc_1)
    p_x += p_velx
    p_y += p_vely
    if acc_1 >= 2:
        print(acc_1)
        palla_1 = pygame.draw.circle(area, (p_r, p_g, p_b), (300, 400), p_raggio, 0)
        p_x += p_velx
        p_y += p_vely
        if p_x > x_max - p_raggio:
                p_velx = -5 #random.randrange(-5, 0)
        elif p_x < p_raggio :
                 p_velx = 5 #random.randrange(3, 10)
        elif p_y < p_raggio:
                p_vely = 5 #random.randrange(3, 10)
        elif p_y > y_max - p_raggio:
            pvel_y = -5
        if palla_1.colliderect(barra):
             p_vely = -p_vely
             acc_1 = acc_1 +1
             print(acc_1)
             pygame.time.wait(20)
##    if (acc_1 >= 10):
##        palla_2 = pygame.draw.circle(area, (p_r, p_g, p_b), (p_x+100, p_y+100), p_raggio, 0)
##        palla_3 = pygame.draw.circle(area, (p_r, p_g, p_b), (p_x+200, p_y+200), p_raggio, 0)
##        palla_6 = pygame.draw.circle(area, (p_r, p_g, p_b), (p_x, p_y), p_raggio, 0)
##        #pygame.display.update()
##        #print(acc_1)
##        if palla_2.colliderect(barra):
##           p_vely = -p_vely
##           acc_1 = acc_1 +1
##           print(acc_1)
##        if palla_3.colliderect(barra):
##             p_vely = -p_vely
##             acc_1 = acc_1 +1
##             print(acc_1)
##
##    if (acc_1 >= 15):
##        palla_4 = pygame.draw.circle(area, (p_r, p_g, p_b), (p_x+100, p_y+100), p_raggio, 0)
##        palla_5 = pygame.draw.circle(area, (p_r, p_g, p_b), (p_x+200, p_y+200), p_raggio, 0)
##        palla_6 = pygame.draw.circle(area, (p_r, p_g, p_b), (p_x, p_y), p_raggio, 0)
##        palla_7 = pygame.draw.circle(area, (p_r, p_g, p_b), (p_x+100, p_y+100), p_raggio, 0)
##
##        #pygame.display.update()
##        #print(acc_1)
##       




##
##
##    if palla_4.colliderect(barra):
##        p_vely = -p_vely
##        acc_1 = acc_1 +1
##        print(acc_1)
##    if palla_5.colliderect(barra):
##        p_vely = -p_vely
##        acc_1 = acc_1 +1
##        print(acc_1)
##    if palla_6.colliderect(barra):
##        p_vely = -p_vely
##        acc_1 = acc_1 +1
##        print(acc_1)
##    if palla_7.colliderect(barra):
##        p_vely = -p_vely
##        acc_1 = acc_1 +1
##        print(acc_1)
##    if palla_8.colliderect(barra):
##        p_vely = -p_vely
##        acc_1 = acc_1 +1
##        print(acc_1)
##    if palla_9.colliderect(barra):
##        p_vely = -p_vely
##        acc_1 = acc_1 +1
##        print(acc_1)
##    if palla_10.colliderect(barra):
##        p_vely = -p_vely
##        acc_1 = acc_1 +1
##        print(acc_1)


    if p_y + p_raggio > y_max:
        print("Hai perso !!")
        perso = True
        pygame.quit()

##    if acc_1 == 5:
##        
##        #palla_2 = pygame.draw.circle(area, (p_r, p_g, p_b), (p_x+100, p_y+100), p_raggio, 0)
##        # palla_3 = pygame.draw.circle(area, (p_r, p_g, p_b), (p_x, p_y), p_raggio, 0)
##        #pygame.display.update()
##        #print(acc_1)

    

    
    if acc_1 == 20:
        print("BRAVOOOOOOOOOO SEI THE CHAMPION OF THE WORLD")
       

    
    
    
        
    pygame.display.update()
    pygame.time.wait(20)

print("Hai perso !!")
pygame.quit()



