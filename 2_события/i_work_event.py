#---Импортируем библиотеку pygame----------
import pygame
from pygame.key import key_code

#---Инциализация---------------------------
pygame.init()

#---Создание окна--------------------------
windowsSize = (800, 600) # первое значение - ширина, второе - высота
# flags= pygame.FULLSCREEN | pygame.RESIZABLE
flags= pygame.RESIZABLE
# установим режим для display - для окна вывода
pygame.display.set_mode(size = windowsSize, flags = flags)

#---Главный игровой цикл-------------------
run = True
while run:
# --- 1. Обработка событий ----------------
    for e in pygame.event.get():    # get() возвращает список событий.
        if e.type == pygame.QUIT:   # Это событие закрытие окна (pygame.QUIT) ?
            run = False # да - выход из основного цикла

    #+1 добавляю
        if e.type == pygame.KEYDOWN:  # Клавиши клавиатуры?
            my_key = e.key          # код клавиши -> в переменную my_key
            my_mod = e.mod          # модификатор -> в переменную my_mod
            # прописываю реакцию - вывод сообщения в консоль
            # реагирует на стрелочки вправо-влево-вверх-вниз
            keyCode = pygame.key.name(my_key)
            #     использую  formatted string literal or f-string
            # print(f"Нажата клавиша: {keyCode}")
            print(f"Нажата клавиша: {pygame.key.name(my_key)}")
            print(f"Модификатор: {my_mod}")

        if e.type == pygame.MOUSEBUTTONDOWN:    # Кнопка мыши?
            my_pos = e.pos          # позиция курсора -> в переменную my_pos
            my_button = e.button    # номер кнопки мыши -> в my_button
            # прописываю реакцию - вывод сообщения в консоль
            print(f"Позиция мыши: {my_pos}")
            print(f"Идентификатор кнопки мыши: {my_button}")
#~1

# --- 2. Обновление состояния. Логика игры--
# --- 3. Отрисовка -------------------------
#-------------------------------------------
# Освобождение всех ресурсов, связанных с библиотекой
pygame.quit()
#-------------------------------------------