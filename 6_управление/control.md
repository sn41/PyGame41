
### Управляю

Чтобы добавить движение ракетки
1) Добавим данные ракетки
2) Блок отслеживания нажатий клавиш, для управления координатами ракетки
3) Рисование ракетки



```
# Данные ракетки
x_rect = 0
y_rect = 0

h_rect = 100    # высота ракетки
w_rect = 100    # ширина ракетки


# +2 Управление ракеткой
elif e.type == pygame.KEYDOWN:
    # при нажатии клавиши вверх, изменяем координаты ракетки
    if e.key == pygame.K_UP or e.key == pygame.K_w:
    y_rect += 33
    
# 3+ Рисуем ракетку
pygame.draw.rect(screen, circle_color, rect = (x_rect, y_rect, w_rect, h_rect))    
```
### Задание: Допишите управление ракеткой и отражение мяча от ракетки
