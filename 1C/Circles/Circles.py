import pygame
import random
pygame.init ()
pygame.key.set_repeat(1, 100)
area = pygame.display.set_mode ([1000,1000])
n = int(input ("scegli un numero(<100): "))
r = input ("colore rosso?(si/no) ")
v = input ("colore verde?(si/no) ")
b = input ("colore blu?(si/no) ")
d = int(input ("scegli la lunghezza del raggio(>10): "))


for m in range (n):
    if r == 'si':
        r = 255
        v = 0
        b = 0
        x = random.randrange (1, 900)
        y = random.randrange (1, 900)
        for z in range (10):
            pygame.draw.circle (area, (r, v, b),(x, y), d, 10)
            r = r-15
            v = v+10
            d = d+10
        d = d-90
        r = 'si'

    elif v == 'si':
        v = 255
        r = 0
        b = 0
        x = random.randrange (1, 900)
        y = random.randrange (1, 900)
        for z in range (10):
            pygame.draw.circle (area, (r, v, b),(x, y), d, 10)
            v = v-15
            b = b+10
            d = d+10
        d = d-90
        v = 'si'
        
    elif b == 'si':
        b = 255
        v = 0
        r = 0
        x = random.randrange (1, 900)
        y = random.randrange (1, 900)
        for z in range (10):
            pygame.draw.circle (area, (r, v, b),(x, y), d, 10)
            b = b-15
            r = r+10
            d = d+10
        d = d-90
        b = 'si'


pygame.display.update ()
