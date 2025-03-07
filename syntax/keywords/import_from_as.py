import pygame
pygame.init()

# Импортирую функции display, init, quit из библиотеки pygame
from pygame import display, init, quit
init()

# Могу использовать псевдоним pg вместо pygame
import pygame as pg
pg.init()

# Их можно использовать смешанно
import pygame as pg
from pygame import display, init, quit