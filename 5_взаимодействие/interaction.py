#---Импортируем библиотеку pygame----------
import pygame
from pygame.draw import circle
from pygame.examples.moveit import HEIGHT

#---Инциализация---------------------------
pygame.init()

#---Создание окна--------------------------
HEIGHT = 720
WIDTH = 1280
windowsSize = (WIDTH, HEIGHT) # первое значение - ширина, второе - высота
# создаём объект окна screen
screen = pygame.display.set_mode(size = windowsSize)

#---Главный игровой цикл-------------------
# создаём объект таймера clock
clock = pygame.time.Clock()
# позиция для вывода окружности

# + 1. Будем использовать отдельные переменные для хранения координат
# Данные окружности
# circle_pos = pygame.Vector2(0, 0)
x_circle = 0
y_circle = 0

circle_radius = 40
circle_color = "gray"

# дельта - изменение позиции между кадрами
delta_pos = pygame.Vector2(10, 10)


running = True

while running:
# --- 1. Обработка списка всех событий, произошедших с последнего кадра.
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for e in pygame.event.get():    # get() возвращает список событий.
        if e.type == pygame.QUIT:   # Это событие закрытие окна (pygame.QUIT)
            running = False             # да - выход из основного цикла

# --- 2. Обновление состояния.

    # Изменяем позицию
    # + 2 Считаем каждую координату отдельно
    # circle_pos = circle_pos + DELTA_POS
    x_circle += delta_pos.x
    y_circle += delta_pos.y

    if y_circle > HEIGHT:
        dy = y_circle - HEIGHT             # на какое расстояние по оси y вылетел за границу
        y_circle = y_circle - dy                  # куда должен прилететь, если отразиться
        delta_pos.y = - delta_pos.y # изменяем направление движения по оси y
    if x_circle > WIDTH:
        dx = x_circle - WIDTH
        x_circle = x_circle - dx
        delta_pos.x = - delta_pos.x

    # ***** 1. Добавьте отражение от стен здесь
    # ***** 2. Мячик отражается от стен своим центром, сделайте так, чтобы он отражался границей

# --- 3. Отрисовка
    # заполнить экран цветом, чтобы стереть все, что осталось от последнего кадра
    screen.fill("purple")


    # РИСУЙТЕ СВОЮ ИГРУ ЗДЕСЬ

    # Рисуем окружность
    # + 3 используем наши координаты
    circle_pos = pygame.Vector2(x_circle, y_circle)
    pygame.draw.circle(screen, circle_color, circle_pos, circle_radius)

    # Рисуем ракетку
    pygame.draw.rect(screen, circle_color, rect = (circle_pos.x, circle_pos.y, 60, 200))



    # переверните flip() дисплей, чтобы вывести свою работу на экран
    # (есть слой памяти, который сейчас отображается, и тот на котором вы рисовали)
    # flip() меняети их местами
    pygame.display.flip()   # update the screen

    # Задержка между кадрами пририсовки
    pygame.time.delay(10)   # introduce a delay

    clock.tick(60) # ограничивает FPS до 60


#-------------------------------------------
# Освобождение всех ресурсов, связанных с библиотекой
pygame.quit()
#-------------------------------------------