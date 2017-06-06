#Inizializzazione
import pygame
pygame.init()
area = pygame.display.set_mode((800, 800))
area.fill((0, 0, 0))

#Variabili
BIANCO = (255, 255, 255)
NERO = (0, 0, 0)
ROSSO = (255, 0, 0)
BLU = (51, 195, 224)
VERDE = (0, 255, 0)
GIALLO = (241, 244, 66)

#Height
h_1 = 120
h_2 = 240
h_3 = 360
#Lenght
l_1 = 133
l_2 = 400
l_3 = 666



turno = "X"

grid = [["", "", ""], ["", "", ""], ["", "", ""]]


casella_0_0 = pygame.draw.rect(area, BIANCO, ((l_1, h_1), (100, 100)))
casella_0_1 = pygame.draw.rect(area, BIANCO, ((l_2, h_1), (100, 100)))
casella_0_2 = pygame.draw.rect(area, BIANCO, ((l_3, h_1), (100, 100)))

casella_1_0 = pygame.draw.rect(area, BIANCO, ((l_1, h_2), (100, 100)))
casella_1_1 = pygame.draw.rect(area, BIANCO, ((l_2, h_2), (100, 100)))
casella_1_2 = pygame.draw.rect(area, BIANCO, ((l_3, h_2), (100, 100)))

casella_2_0 = pygame.draw.rect(area, BIANCO, ((l_1, h_3), (100, 100)))
casella_2_1 = pygame.draw.rect(area, BIANCO, ((l_2, h_3), (100, 100)))
casella_2_2 = pygame.draw.rect(area, BIANCO, ((l_3, h_3), (100, 100)))

pygame.display.update()


#Impostazione while
complete = False
while complete == False:
    if grid[0][0] != "":
        symbol = grid[0][0]
        if grid[0][1] == symbol:
            if grid[0][2] == symbol:
                print("Il vincitore è ", symbol)
                complete = True
        elif grid[1][0] == symbol:
            if grid[2][0] == symbol:
                print("Il vincitore è ", symbol)
                complete = True
        elif grid[1][1] == symbol:
            if grid[2][2] == symbol:
                print("Il vincitore è ", symbol)
                complete = True
    elif grid[1][0] != "":
        symbol = grid[1][0]
        if grid[1][1] == symbol:
            if grid[1][2] == symbol:
                print("Il vincitore è ", symbol)
                complete = True
    elif grid[0][2] != "":
        symbol = grid[0][2]
        if grid[1][2] == symbol:
            if grid[2][2] == symbol:
                print("Il vincitore è ", symbol)
                complete = True
        elif grid[1][1] == symbol:
            if grid[2][0] == symbol:
                print("Il vincitore è ", symbol)
                complete = True
        elif grid[1][1] == symbol:
            if grid[2][0] == symbol:
                print("Il vincitore è ", symbol)
                complete = True
    elif grid[0][1] != "":
        symbol = grid[0][1]
        if grid[1][1] == symbol:
            if grid[2][1] == symbol:
                print("Il vincitore è ", symbol)
                complete = True
    elif grid[0][0] != "" and grid[0][1] != "" and grid[0][2] != "" and grid[1][0] != "" and grid[1][1] != "" and grid[1][2] != "" and grid[2][0] != "" and grid[2][1] != "" and grid[2][2] != "":
        print("Non ha vinto nessuno!")
        complete = True



    for evento in pygame.event.get():
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if casella_0_0.collidepoint(evento.pos):
                if grid[0][0] == "":
                    if turno == "X":
                        pygame.draw.rect(area, ROSSO, ((l_1, h_1), (100, 100)))
                        pygame.display.update()
                        grid[0][0] = turno
                        turno = "0"
                    elif turno == "0":
                        pygame.draw.circle(area, BLU, (l_1 + 50, h_1 + 50), 50, 10)
                        pygame.display.update()
                        grid[0][0] = turno
                        turno = "X"
                elif grid[0][0] != "":
                    pass
            elif casella_0_1.collidepoint(evento.pos):
                if grid[0][1] == "":
                    if turno == "X":
                        pygame.draw.rect(area, ROSSO, ((l_2, h_1), (100, 100)))
                        pygame.display.update()
                        grid[0][1] = turno
                        turno = "0"
                    elif turno == "0":
                        pygame.draw.circle(area, BLU, (l_2 + 50, h_1 + 50), 50, 10)
                        pygame.display.update()
                        grid[0][1] = turno
                        turno = "X"
                elif grid[0][1] != "":
                    pass
            elif casella_0_2.collidepoint(evento.pos):
                if grid[0][2] == "":
                    if turno == "X":
                        pygame.draw.rect(area, ROSSO, ((l_3, h_1), (100, 100)))
                        pygame.display.update()
                        grid[0][2] = turno
                        turno = "0"
                    elif turno == "0":
                        pygame.draw.circle(area, BLU, (l_3+50, h_1+50), 50, 10)
                        pygame.display.update()
                        grid[0][2] = turno
                        turno = "X"
                elif grid[0][2] != "":
                    pass

            elif casella_1_0.collidepoint(evento.pos):
                if grid[1][0] == "":
                    if turno == "X":
                        pygame.draw.rect(area, ROSSO, ((l_1, h_2), (100, 100)))
                        pygame.display.update()
                        grid[1][0] = turno
                        turno = "0"
                    elif turno == "0":
                        pygame.draw.circle(area, BLU, (l_1+50, h_2+50), 50, 10)
                        pygame.display.update()
                        grid[1][0] = turno
                        turno == "X"
                elif grid[1][0] != "":
                    pass
            elif casella_1_1.collidepoint(evento.pos):
                if grid[1][1] == "":
                    if turno == "X":
                        pygame.draw.rect(area, ROSSO, ((l_2, h_2), (100, 100)))
                        pygame.display.update()
                        grid[1][1] = turno
                        turno = "0"
                    elif turno == "0":
                        pygame.draw.circle(area, BLU, (l_2+50, h_2+50), 50, 10)
                        pygame.display.update()
                        grid[1][1] = turno
                        turno = "X"
                elif grid[1][1] != "":
                    pass
            elif casella_1_2.collidepoint(evento.pos):
                if grid[1][2] == "":
                    if turno == "X":
                        pygame.draw.rect(area, ROSSO, ((l_3, h_2), (100, 100)))
                        pygame.display.update()
                        grid[1][2] = turno
                        turno = "0"
                    elif turno == "0":
                        pygame.draw.circle(area, BLU, (l_3+50, h_2+50), 50, 10)
                        pygame.display.update()
                        grid[1][2] = turno
                        turno = "X"
                elif grid[1][2] != "":
                    pass

            elif casella_2_0.collidepoint(evento.pos):
                if grid[2][0] == "":
                    if turno == "X":
                        pygame.draw.rect(area, ROSSO, ((l_1, h_3), (100, 100)))
                        pygame.display.update()
                        grid[2][0] = turno
                        turno = "0"
                    elif turno == "0":
                        pygame.draw.circle(area, BLU, (l_1+50, h_3+50), 50, 10)
                        pygame.display.update()
                        grid[2][0] = turno
                        turno = "X"
                elif grid[2][0] != "":
                    pass
            elif casella_2_1.collidepoint(evento.pos):
                if grid[2][1] == "":
                    if turno == "X":
                        pygame.draw.rect(area, ROSSO, ((l_2, h_3), (100, 100)))
                        pygame.display.update()
                        grid[2][1] = turno
                        turno = "0"
                    elif turno == "0":
                        pygame.draw.circle(area, BLU, (l_2+50, h_3+50), 50, 10)
                        pygame.display.update()
                        grid[2][1] = turno
                        turno = "X"
                elif grid[2][1] != "":
                    pass
            elif casella_2_2.collidepoint(evento.pos):
                if grid[2][2] == "":
                    if turno == "X":
                        pygame.draw.rect(area, ROSSO, ((l_3, h_3), (100, 100)))
                        pygame.display.update()
                        grid[2][2] = turno
                        turno = "0"
                    elif turno == "0":
                        pygame.draw.circle(area, BLU, (l_3+50, h_3+50), 50, 10)
                        pygame.display.update()
                        grid[2][2] = turno
                        turno = "X"
                elif grid[2][2] != "":
                    pass

            





pygame.quit()                    
                    
                                
                            
                    
                    
                       
    

    
