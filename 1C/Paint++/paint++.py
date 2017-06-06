#Inizializzazione del motore grafico PyGame
import pygame
pygame.init()
clock = pygame.time.Clock()

# Definizione costanti
MARRONE = (58, 0, 0)
BORDEAUX = (150, 33, 33)
ROSSO = (255, 0, 0)
ROSSOFOO = (242, 73, 7)
ARANCIONE = (255, 144, 0)
ORO = (255, 187, 0)
GIALLO = (245, 255, 56)
VERDE = (0, 255, 0)
VERDEB = (4, 79, 13)
TURCHESE = (0, 255, 212)
BLU = (13, 0, 163)
VIOLA = (124, 4, 135)
FUFFIA = (160, 11, 73)
ROSA = (255, 0, 216)
ROSAP = (231, 197, 234)
LILLA = (150, 137, 175)
GRIGIOC = (183, 183, 183)
GRIGIO = (100, 100, 100)
NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
SPESSORE_LINEA = 20
SPESSORE_PUNTO = 8
ALTEZZA = 400
LARGHEZZA = 800
CERCHIO = 0

show_circle = False # If true it draws a circle (choosing the dimensions)


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
            if rose_rect.collidepoint(evento.pos):
                colore_penna = ROSA
            if blue_rect.collidepoint(evento.pos):
                colore_penna = TURCHESE
            if purple_rect.collidepoint(evento.pos):
                colore_penna = VIOLA
            if pink_rect.collidepoint(evento.pos):
                colore_penna = ROSAP
            if yellow_rect.collidepoint(evento.pos):
                colore_penna = GIALLO
            if orange_rect.collidepoint(evento.pos):
                colore_penna = ARANCIONE
            if blub_rect.collidepoint(evento.pos):
                colore_penna = BLU
            if white_rect.collidepoint(evento.pos):
                lavagna.fill(BIANCO)
            if lilac_rect.collidepoint(evento.pos):
                colore_penna = LILLA
            if fuxia_rect.collidepoint(evento.pos):
                colore_penna = FUFFIA
            if emerald_rect.collidepoint(evento.pos):
                colore_penna = VERDEB
            if bordeaux_rect.collidepoint(evento.pos):
                colore_penna = BORDEAUX
            if brown_rect.collidepoint(evento.pos):
                colore_penna = MARRONE
            if fire_rect.collidepoint(evento.pos):
                colore_penna = ROSSOFOO
            if gold_rect.collidepoint(evento.pos):
                colore_penna = ORO
            if grey_rect.collidepoint(evento.pos):
                colore_penna = GRIGIO
            if lightgrey_rect.collidepoint(evento.pos):
                colore_penna = GRIGIOC
            if spess1.collidepoint(evento.pos):
                SPESSORE_PUNTO = 4
                SPESSORE_LINEA = 9
            if spess2.collidepoint(evento.pos):
                SPESSORE_PUNTO = 8
                SPESSORE_LINEA = 20
            if spess3.collidepoint(evento.pos):
                SPESSORE_PUNTO = 12
                SPESSORE_LINEA = 30
            if cerchio.collidepoint(evento.pos):
                rett1 = pygame.draw.rect(lavagna, GRIGIOC,((95, 125),(30, 30)))
                rett2 = pygame.draw.rect(lavagna, GRIGIOC,((95, 155),(30, 30)))
                rett3 = pygame.draw.rect(lavagna, GRIGIOC,((95, 185),(30, 30)))
                rett4 = pygame.draw.rect(lavagna, GRIGIOC,((95, 215),(30, 30)))

                myfont = pygame.font.SysFont("monospace", 15)
                # render text
                label = myfont.render("Dimensione raggio", 1, (100,100,0))
                label1 = myfont.render("30", 1, (100,100,0))
                label2 = myfont.render("60", 1, (100,100,0))
                label3 = myfont.render("90", 1, (100,100,0))
                label4 = myfont.render("120", 1, (100,100,0))
                lavagna.blit(label, (100, 100))
                lavagna.blit(label1, (100, 130))
                lavagna.blit(label2, (100, 160))
                lavagna.blit(label3, (100, 190))
                lavagna.blit(label4, (100, 220))
                show_circle = True


    sinistro, centrale, destro = mouse.get_pressed()
    # Se l'utente clicca con il mouse all'interno della finestra di gioco
    if sinistro:
        # L'utente ha cliccato il bottone sinistro del mouse
        mouse_pos = mouse.get_pos()
        #print(mouse_pos)
        #print(CERCHIO)
        #pygame.draw.circle(lavagna, colore_penna, mouse_pos, CERCHIO, SPESSORE_PUNTO)
        #CERCHIO = 14
        if show_circle == True:
            if rett1.collidepoint(mouse_pos):
                    print("clicj")
                    CERCHIO = 30
                    draw_circle = True
            if rett2.collidepoint(mouse_pos):
                    print("clicj")
                    CERCHIO = 60
                    draw_circle = True
            if rett3.collidepoint(mouse_pos):
                    print("clicj")
                    CERCHIO = 90
                    draw_circle = True
            if rett4.collidepoint(mouse_pos):
                    print("clicj")
                    CERCHIO = 120
                    draw_circle = True
  
        if mouse_pos_vecchia is not None:
            pygame.draw.line(lavagna, colore_penna, mouse_pos_vecchia, mouse_pos, SPESSORE_LINEA)
        mouse_pos_vecchia = mouse_pos
    elif destro:
        mouse_pos = mouse.get_pos()
        pygame.draw.circle(lavagna, BIANCO, mouse_pos, SPESSORE_PUNTO)

        if CERCHIO > 0 :
               pygame.draw.circle(lavagna, colore_penna, mouse.get_pos(), CERCHIO, SPESSORE_PUNTO)
               CERCHIO = 0

        if mouse_pos_vecchia is not None:
            pygame.draw.line(lavagna, BIANCO, mouse_pos_vecchia, mouse_pos, SPESSORE_LINEA)
        mouse_pos_vecchia = mouse_pos
        
    else:
        mouse_pos_vecchia = None

    area.fill(GRIGIO)
    red_rect = pygame.draw.rect(area, ROSSO,((LARGHEZZA-30, 60),(30, 30)))
    green_rect = pygame.draw.rect(area, VERDE,((LARGHEZZA-30, 210),(30, 30)))
    black_rect = pygame.draw.rect(area, NERO,((LARGHEZZA-30, 540),(30, 30)))
    rose_rect = pygame.draw.rect(area, ROSA,((LARGHEZZA-30, 390),(30, 30)))
    blue_rect = pygame.draw.rect(area, TURCHESE,((LARGHEZZA-30, 240),(30, 30)))
    purple_rect = pygame.draw.rect(area, VIOLA,((LARGHEZZA-30, 330),(30, 30)))
    pink_rect = pygame.draw.rect(area, ROSAP,((LARGHEZZA-30, 420),(30, 30)))
    yellow_rect = pygame.draw.rect(area, GIALLO,((LARGHEZZA-30, 180),(30, 30)))
    orange_rect = pygame.draw.rect(area, ARANCIONE,((LARGHEZZA-30, 120),(30, 30)))
    blub_rect = pygame.draw.rect(area, BLU,((LARGHEZZA-30, 300),(30, 30)))
    white_rect = pygame.draw.rect(area, BIANCO,((LARGHEZZA-30, ALTEZZA-30),(30, 30)))
    lilac_rect = pygame.draw.rect(area, LILLA,((LARGHEZZA-30, 450),(30, 30)))
    fuxia_rect = pygame.draw.rect(area, FUFFIA,((LARGHEZZA-30, 360),(30, 30)))
    emerald_rect = pygame.draw.rect(area, VERDEB,((LARGHEZZA-30, 270),(30, 30)))
    bordeaux_rect = pygame.draw.rect(area, BORDEAUX,((LARGHEZZA-30, 30),(30, 30)))
    fire_rect = pygame.draw.rect(area, ROSSOFOO,((LARGHEZZA-30, 90),(30, 30)))
    gold_rect = pygame.draw.rect(area, ORO,((LARGHEZZA-30, 150),(30, 30)))
    grey_rect = pygame.draw.rect(area, GRIGIO,((LARGHEZZA-30, 510),(30, 30)))
    brown_rect = pygame.draw.rect(area, MARRONE,((LARGHEZZA-30, 0),(30, 30)))
    lightgrey_rect = pygame.draw.rect(area, GRIGIOC,((LARGHEZZA-30, 480),(30, 30)))
    spess1 = pygame.draw.rect(area, BIANCO,((0, ALTEZZA-29),(30, 30)))
    spess2 = pygame.draw.rect(area, BIANCO,((31, ALTEZZA-29),(30, 30)))
    spess3 = pygame.draw.rect(area, BIANCO,((62, ALTEZZA-29),(30, 30)))
    cerc1 = pygame.draw.circle(area, NERO, (15, ALTEZZA-15),4, 0)
    cerc2 = pygame.draw.circle(area, NERO, (45, ALTEZZA-15),8, 0)
    cerc3 = pygame.draw.circle(area, NERO, (77, ALTEZZA-15),12, 0)
    cerchio = pygame.draw.circle(area, NERO, (LARGHEZZA-50, ALTEZZA-15),15, 0)
    
    # Disegno la lavagna all'interno dell'area
    area.blit(lavagna, (0,0))

    # Disegno il puntatore del mouse con il colore selezionato
    pygame.draw.circle(area, colore_penna, (mouse.get_pos()), SPESSORE_PUNTO)

    # Aggiorna lo schermo con tutto quello che è stato disegnato
    pygame.display.flip()
    clock.tick(60)
