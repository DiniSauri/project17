# Inizializzazione del motore grafico PyGame
import pygame
pygame.init()
clock = pygame.time.Clock()

# Definizione costanti
NERO = (0, 0, 0)
VERDE = (0, 255, 0)
ROSSO = (255, 0, 0)
BIANCO = (255, 255, 255)
BLU = (64,131,239)
GRIGIO = (100, 100, 100)
GIALLO = (239,223,64)
MARRONE = (155,101,0)
ROSA = (244,66,215)
SPESSORE_LINEA = 20
SPESSORE_PUNTO = 15
ALTEZZA = 600
LARGHEZZA = 800
rettangolo = False
cerchio = False

# Creazione della finestra di pygame
pygame.display.set_caption("Paint Me")
area = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
area.fill(GRIGIO)

# Aggiungere qui la creazione della lavagna dove scrivere
lavagna = pygame.Surface((LARGHEZZA-30, ALTEZZA-30))
lavagna.fill(BIANCO)

# Inizializzazione cursore del mouse
mouse = pygame.mouse
mouse.set_visible(False)
colore_penna = NERO

# Ripeti fino a quando l'untente non esce e ad ogni iterazione
while True:
    # Gestore delle azioni dell'utente
    for evento in pygame.event.get():
        # Se l'utente clicca il bottone chiudi sulla finestra
        if evento.type == pygame.QUIT:
            exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if red_rect.collidepoint(evento.pos):
                colore_penna = ROSSO
            if green_rect.collidepoint(evento.pos):
                colore_penna = VERDE
            if black_rect.collidepoint(evento.pos):
                colore_penna = NERO
            if blue_rect.collidepoint(evento.pos):
                colore_penna = BLU
            if brown_rect.collidepoint(evento.pos):
                rettangolo = True
                print("sto pigiando marrone")
            if pink_rect.collidepoint(evento.pos):
                cerchio = True
                
            if yellow_rect.collidepoint(evento.pos):
                lavagna.fill(BIANCO)
    sinistro, centrale, destro = mouse.get_pressed()
    # Se l'utente clicca con il mouse all'interno della finestra di gioco
    if sinistro:
        mouse_pos = mouse.get_pos()  # mouse_pos = (x,y)  # x = mouse_pos[0] y = mouse_pos[1]  
        print(mouse_pos)
        xa = mouse_pos[0]
        ya = mouse_pos[1]
        xb = xa + 200
        yb = ya + 200
        
        if rettangolo == True:
            cerchio = False
            pygame.draw.rect(lavagna,MARRONE, (xa,ya,xb,yb),22)
            print("sto disegnando un rettangolo")
        if cerchio == True:
            rettangolo = False
            pygame.draw.circle(lavagna,(ROSA),(mouse_pos),50,10)
            
        else:# L'utente ha cliccato il bottone sinistro del mouse
            pygame.draw.circle(lavagna,colore_penna,mouse_pos,SPESSORE_PUNTO)
            if mouse_pos_vecchia is not None:
                 pygame.draw.line(lavagna,colore_penna,mouse_pos_vecchia, mouse_pos,SPESSORE_LINEA)
            mouse_pos_vecchia = mouse_pos
    elif destro:
        mouse_pos = mouse.get_pos()
        colore_penna = BIANCO
        if mouse_pos_vecchia is not None:
            pygame.draw.line(lavagna,colore_penna,mouse_pos_vecchia, mouse_pos,SPESSORE_LINEA)
        mouse_pos_vecchia = mouse_pos
    else:
        mouse_pos_vecchia = None
    area.fill(GRIGIO)
    red_rect = pygame.draw.rect(area,ROSSO, ((LARGHEZZA-30, 0), (30,30)))
    green_rect = pygame.draw.rect(area,VERDE, ((LARGHEZZA-30, 30), (30,30)))
    black_rect = pygame.draw.rect(area,NERO, ((LARGHEZZA-30, 60), (30,30)))
    blue_rect = pygame.draw.rect(area,BLU, ((LARGHEZZA-30,90), (30,30)))
    yellow_rect = pygame.draw.rect(area,GIALLO, ((LARGHEZZA-30,120), (30,30)))
    brown_rect = pygame.draw.rect(area,MARRONE, ((LARGHEZZA-30,150), (30,30)))
    pink_rect = pygame.draw.rect(area,ROSA, ((LARGHEZZA-30,180), (30,30)))
    # Disegno la lavagna all'interno dell'area
    area.blit(lavagna,(0,0))
        

    # Disegno il puntatore del mouse con il colore selezionato
    pygame.draw.circle(area, colore_penna, (mouse.get_pos()), SPESSORE_PUNTO)

    # Aggiorna lo schermo con tutto quello che è stato disegnato
    pygame.display.flip()
    clock.tick(60)
