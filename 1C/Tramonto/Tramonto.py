import pygame
pygame.init()
l = 1600
h = 900
vel_x = 2
vel_y = -3
s_x = 0
s_y = 500
a = True
t= 8
r1=255
g1=255
b1=0





# sfondo
area = pygame.display.set_mode((l, h))
area.fill((193, 230, 255))

# mare
#pygame.draw.line(area,(0, 89, 255),(0,h),(l,h), 600)
#pygame.display.update()


# sole 
pygame.draw.circle(area, (255, 119, 0), (s_x, s_y), 70, 0)
pygame.display.update()



# evento sole
for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit() # usciamo dal gioco
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT: #pressione freccia SX
                b_x -= 10
            if evento.key == pygame.K_RIGHT:# pression freccia DX
                b_x += 10
                
# movimento sole
while a == True:
        s_x = s_x + vel_x
        s_y = s_y + vel_y
        # Sole
        pygame.draw.circle(area, (r1, g1, b1), (s_x, s_y), 70, 0)
        # sfumature mare 1 ALBA
        # sfumature mare 1
        pygame.draw.line(area,(0, 55, 50),(0, 520),(l, 520), 20)
        pygame.display.update()
        # sfumature mare 2
        pygame.draw.line(area,(0, 60, 60),(0, 540),(l, 540), 20)
        pygame.display.update()
        # sfumature mare 3
        pygame.draw.line(area,(1, 65, 70),(0, 560),(l, 560), 20)
        pygame.display.update()
        # sfumature mare 4
        pygame.draw.line(area,(1, 70, 80),(0, 580),(l, 580), 20)
        pygame.display.update()
        # sfumature mare 5
        pygame.draw.line(area,(2, 75, 90),(0, 600),(l, 600), 20)
        pygame.display.update()
        # sfumature mare 6
        pygame.draw.line(area,(2, 80, 100),(0, 620),(l, 620), 20)
        pygame.display.update()
        # sfumature mare 7
        pygame.draw.line(area,(3, 85, 110),(0, 640),(l, 640), 20)
        pygame.display.update()
        # sfumature mare 8
        pygame.draw.line(area,(3, 90, 120),(0, 660),(l, 660), 20)
        pygame.display.update()
        # sfumature mare 9
        pygame.draw.line(area,(4, 95, 130),(0, 680),(l, 680), 20)
        pygame.display.update()
        # sfumature mare 10
        pygame.draw.line(area,(4, 100, 140),(0, 700),(l, 700), 20)
        pygame.display.update()
        # sfumature mare 11
        pygame.draw.line(area,(5, 105, 150),(0, 720),(l, 720), 20)
        pygame.display.update()
        # sfumature mare 12
        pygame.draw.line(area,(5, 110, 160),(0, 740),(l, 740), 20)
        pygame.display.update()
        # sfumature mare 13
        pygame.draw.line(area,(6, 115, 170),(0, 760),(l, 760), 20)
        pygame.display.update()
        # sfumature mare 14
        pygame.draw.line(area,(6, 120, 180),(0, 780),(l, 780), 20)
        pygame.display.update()
        # sfumature mare 15
        pygame.draw.line(area,(7, 125, 190),(0, 800),(l, 800), 20)
        pygame.display.update()
        # sfumature mare 16
        pygame.draw.line(area,(7, 130, 200),(0, 820),(l, 820), 20)
        pygame.display.update()
        # sfumature mare 17
        pygame.draw.line(area,(8, 135, 210),(0, 840),(l, 840), 20)
        pygame.display.update()
        # sfumature mare 18
        pygame.draw.line(area,(8, 140, 220),(0, 860),(l, 860), 20)
        pygame.display.update()
        # sfumature mare 19
        pygame.draw.line(area,(9, 145, 230),(0, 880),(l, 880), 20)
        pygame.display.update()
        # sfumature mare 20
        pygame.draw.line(area,(9, 150, 240),(0, 890),(l, 890), 20)
        pygame.display.update()
        pygame.display.update()
        # copri sole
        pygame.draw.circle(area, (193, 230, 255), (s_x,s_y), 70, 0)                   
        if s_x >= 50 and s_y >= 425:  
                vel_x = 4
                vel_y = -3
                t = 10
                r1 =255
                g1 =229
                b1 =0
        if s_x >= 100 and s_y >= 350:   
            vel_x = 4
            vel_y = -2
            r1 =255
            g1 =212
            b1 =0
        if s_x >= 200 and s_y >= 300:   
            vel_x = 4
            vel_y = -2
            r1 =255
            g1 =182
            b1 =0
        if s_x >= 300 and s_y >= 250:
            vel_x = 4
            vel_y = -1
            r1 =255
            g1 =170
            b1 =0
        if s_x >= 500 and s_y >= 200:
                    vel_x = 4
                    vel_y = 0
                    r1 =255
                    g1 =157
                    b1 =0
                    # sfumature mare 1
                    pygame.draw.line(area,(0, 50, 155),(0, 520),(l, 520), 20)
                    # sfumature mare 2
                    pygame.draw.line(area,(3, 60, 157),(0, 540),(l, 540), 20)
                    # sfumature mare 3
                    pygame.draw.line(area,(6, 70, 159),(0, 560),(l, 560), 20)
                    # sfumature mare 4
                    pygame.draw.line(area,(9, 80, 161),(0, 580),(l, 580), 20)
                    # sfumature mare 5
                    pygame.draw.line(area,(12, 90, 163),(0, 600),(l, 600), 20)
                    # sfumature mare 6
                    pygame.draw.line(area,(15, 100, 165),(0, 620),(l, 620), 20)
                    # sfumature mare 7
                    pygame.draw.line(area,(18, 110, 167),(0, 640),(l, 640), 20)
                    # sfumature mare 8
                    pygame.draw.line(area,(21, 120, 169),(0, 660),(l, 660), 20)
                    # sfumature mare 9
                    pygame.draw.line(area,(24, 130, 171),(0, 680),(l, 680), 20)
                    # sfumature mare 10
                    pygame.draw.line(area,(27, 140, 173),(0, 700),(l, 700), 20)
                    # sfumature mare 11
                    pygame.draw.line(area,(30, 150, 175),(0, 720),(l, 720), 20)
                    # sfumature mare 12
                    pygame.draw.line(area,(33, 160, 177),(0, 740),(l, 740), 20)
                    # sfumature mare 13
                    pygame.draw.line(area,(36, 170, 179),(0, 760),(l, 760), 20)
                    # sfumature mare 14
                    pygame.draw.line(area,(39, 180, 181),(0, 780),(l, 780), 20)
                    # sfumature mare 15
                    pygame.draw.line(area,(42, 190, 183),(0, 800),(l, 800), 20)
                    # sfumature mare 16
                    pygame.draw.line(area,(45, 200, 185),(0, 820),(l, 820), 20)
                    # sfumature mare 17
                    pygame.draw.line(area,(48, 210, 187),(0, 840),(l, 840), 20)
                    # sfumature mare 18
                    pygame.draw.line(area,(51, 220, 189),(0, 860),(l, 860), 20)
                    # sfumature mare 19
                    pygame.draw.line(area,(54, 230, 191),(0, 880),(l, 880), 20)
                    # sfumature mare 20
                    pygame.draw.line(area,(57, 240, 193),(0, 890),(l, 890), 20)
        if s_x >= 1100 and s_y >= 200:   
         vel_x = 4
         vel_y = 1
         r1 =255
         g1 =140
         b1 =0  
        if s_x >= 1300 and s_y >= 250:  
         vel_x = 4
         vel_y = 2
         r1 =255
         g1 =119
         b1 =0
        if s_x >= 1400 and s_y >= 300:
         vel_x = 4
         vel_y = 2
         r1 =255
         g1 =89
         b1 =0
        if s_x >= 1500 and s_y >= 350:
         vel_x = 4
         vel_y = 3
         r1 =255
         g1 = 45
         b1 =0
        if s_x >= 1550 and s_y >= 426:  
         vel_x = 2
         vel_y = 3
         r1 =255
         g1 =0
         b1 =0
        pygame.time.wait(t)




# colore red green blue

