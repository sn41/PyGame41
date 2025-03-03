#---Импортируем библиотеку pygame----------
import pygame
from pygame.draw import circle

#---Инциализация---------------------------
pygame.init()

#---Создание окна--------------------------
windowsSize = (1280, 720) # первое значение - ширина, второе - высота
# создаём объект окна screen
screen = pygame.display.set_mode(size = windowsSize, flags = pygame.RESIZABLE)

#---Главный игровой цикл-------------------
# создаём объект таймера clock
clock = pygame.time.Clock()
# позиция для вывода окружности
circle_pos = pygame.Vector2(100, 100)
circle_radius = 40
circle_color = "gray"

running = True

while running:
# --- 1. Обработка списка всех событий, произошедших с последнего кадра.
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for e in pygame.event.get():    # get() возвращает список событий.
        if e.type == pygame.QUIT:   # Это событие закрытие окна (pygame.QUIT)
            running = False             # да - выход из основного цикла

# --- 2. Обновление состояния.

# --- 3. Отрисовка
    # заполнить экран цветом, чтобы стереть все, что осталось от последнего кадра
    screen.fill("purple")

    # РИСУЙТЕ СВОЮ ИГРУ ЗДЕСЬ
    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)

    # переверните flip() дисплей, чтобы вывести свою работу на экран
    # (есть слой памяти, который сейчас отображается, и тот на котором вы рисовали)
    # flip() меняети их местами
    pygame.display.flip()

    clock.tick(60) # ограничивает FPS до 60
#-------------------------------------------
# Освобождение всех ресурсов, связанных с библиотекой
pygame.quit()
#-------------------------------------------