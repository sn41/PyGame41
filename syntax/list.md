from typing import Anyfrom typing import Any[python documentation **list** ](https://www.w3schools.com/python/python_lists.asp)
## Списки (list)

Списки представляют собой изменяемый (mutable) тип. Вы можете добавить, удалить, изменить значение элементов списка.  

Списки - это один из типов коллекций Python Collections, другие:
- **Tuple**, **кортежи** — это упорядоченная и неизменяемая коллекция. Допускает дублирующиеся элементы.
- **Set**, **наборы** - это неупорядоченная, неизменяемая и неиндексированная коллекция. Нет дублирующихся элементов.
- **Dictionary**, **отображения** — это упорядоченная и изменяемая коллекция. Нет дублирующихся элемент


### Объявление списка

```python
# список квадратов чисел
squares  = [1, 4, 9, 16, 25] # здесь:  squares:list[int]
var = squares + [36, 49, 64, 81, 100] # добавим элементы в конец списка
# теперь в списке squares содержатся элементы: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# список имён
people = ["Tom", "Sam", "Bob"] # здесь: people: list[str]

# пустые списки
numbers1 = []
numbers2 = list()

# Список разнородных объектов	
objects = [1, 2.6, "Hello", True] # здесь: list[int | float | str | bool] 

# print выводит содержимое списка в удобочитаемом виде:
print(people)  # ["Tom", "Sam", "Bob"]

# Конструктор list может принимать набор значений, на основе которых создается список:
numbers3: list[int] = [1, 2, 3, 4, 5]
numbers4 = list(numbers1)
letters = list("Hello")
print(letters)      # ['H', 'e', 'l', 'l', 'o']

# Можно использовать символ звездочки *, то есть применить операцию умножения к уже существующему списку:
numbers6: list[int] = [5] * 6   # 6 раз повторяем 5 
# в numbers6 хранятся [5, 5, 5, 5, 5, 5]

booleans = [True, False, False]
```

####  Списки списков

```python
# Объявляем список people в который входят списки ["Tom", 29], ["Alice", 33], ["Bob", 27]
people = [
    ["Tom", 29],
    ["Alice", 33],
    ["Bob", 27]
]
# Первый индекс указывает на вложенный список, второй,- на элемент в этом списке. 
print(people[0])         # ["Tom", 29]
print(people[0][0])      # Tom
print(people[0][1])      # 29
```

##### Тип списка type()

```python
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # <class 'list'>
```

### Обращение к элементам списка

##### Получение
```python
people = ["Tom", "Sam", "Bob"]
print(people[0])   # получение элементов с начала списка # Tom 
print(people[-2])   # # получение элементов с конца списка # Sam
```

##### Изменение

Для изменения элемента списка достаточно присвоить ему новое значение:

```python
people = ["Tom", "Sam", "Bob"]
people[1] = "Mike"  # изменение второго элемента
```
##### Разложение списка

```python
people = ["Tom", "Bob", "Sam"]
# Переменным tom, bob и sam последовательно присваиваются элементы из списка people. 
# Количество переменных должно быть равно числу элементов присваиваемого списка.
tom, bob, sam = people
print(tom)      # Tom
print(bob)      # Bob
print(sam)      # Sam
```
##### Перебор элементов

```python
# Перебор: 
#   С помощью цикла for:
people = ["Tom", "Sam", "Bob"]
for person in people:
    print(person)

#   C помощью цикла while:    
i = 0                   # переменная i для индекса
length = len(people)    # значение - длины списка
while i < length:
    print(people[i])    # применяем индекс для получения элемента
    i += 1
```

### Сравнение списков

```python
# Два списка считаются равными, если они содержат один и тот же набор элементов:
numbers1 = [1, 2, 3, 4, 5]
numbers2 = list([1, 2, 3, 4, 5]) # используем конструктор list
if numbers1 == numbers2:
    print("numbers1 equal to numbers2")
else:
    print("numbers1 is not equal to numbers2")
# В данном случае оба списка будут равны.
```

### Получение части списка - среза (slice)

```python
people = ["Tom", "Bob", "Alice", "Sam", "Tim", "Bill"]
 
slice_people1 = people[:3]   # с 0 по 3 # ["Tom", "Bob", "Alice"]
slice_people2 = people[1:3]   # с 1 по 3 # ["Bob", "Alice"]
slice_people3 = people[1:6:2]   # с 1 по 6 с шагом 2  # ["Bob", "Sam", "Bill"]
slice_people4 = people[:-1]   # с предпоследнего по нулевой # ["Tom", "Bob", "Alice", "Sam", "Tim"]
slice_people5 = people[-3:-1]   # с третьего с конца по предпоследний # ["Sam", "Tim"]
```


## Работа со списками
### Методы

Некоторые **Методы**:  
**добавить**
- _append(item)_:  **элемент** item **в конец списка**
- _insert(index, item)_: **элемент** item в список **по индексу index**
- _extend(items)_: **набор** элементов items **в конец списка**

**удалить**
- _remove(item)_: **элемент** item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError
- _clear()_: **все элементы** списка
- _pop([index])_: удаляет и возвращает **элемент по индексу** index. Если индекс не передан, то просто удаляет **последний элемент**.

**вернуть**
- _index(item)_: возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError
- _count(item)_: возвращает количество вхождений элемента item в список

**сортировать**
- _sort([key])_: сортирует **элементы**. По умолчанию сортирует **по возрастанию**. Но с помощью параметра key мы **можем передать функцию сортировки**.

**Изменение порядка элементов**
- _reverse()_: расставляет все элементы в списке **в обратном порядке** 

**копировать**
- _copy()_: копирует список

### Функции
- _len(list)_: возвращает длину списка
- _sorted(list, [key])_: возвращает отсортированный список
- _min(list)_: возвращает наименьший элемент списка
- _max(list)_: возвращает наибольший элемент списка



#### Добавление и удаление: append(), extend(), insert(), remove(), pop() и clear().

```python
people = ["Tom", "Bob"]
people.append("Alice")          # добавляем в конец списка # ["Tom", "Bob", "Alice"]
people.insert(1, "Bill")        # добавляем на вторую позицию # ["Tom", "Bill", "Bob", "Alice"]
people.extend(["Mike", "Sam"])  # добавляем набор элементов ["Mike", "Sam"] # ["Tom", "Bill", "Bob", "Alice", "Mike", "Sam"]


people.remove("Alice")                  # удаляем первый попавшийся элемент "Alice"   # ["Bill", "Bob", "Mike"]

index_of_tom: int = people.index("Tom")      # получаем индекс элемента
removed_item = people.pop(index_of_tom) # удаляем по этому индексу # ["Bill", "Bob", "Alice", "Mike", "Sam"]

last_item = people.pop()                # удаляем последний элемент # ["Bill", "Bob", "Alice", "Mike"]

people.clear()                          # удаляем все элементы

print(people)                           # []
```
#### Проверка наличия элемента, ключевое слово, оператора in

Если определенный элемент не найден, то методы remove и index генерируют исключение.  
Чтобы избежать подобной ситуации, перед операцией с элементом можно проверять его наличие с помощью ключевого слова in:

```python
people = ["Tom", "Bob", "Alice", "Sam"]
 
if "Alice" in people:           # Проверим наличие элемента "Alice, чтобы избежать возникновения исключения.  
    people.remove("Alice")      # Элемент "Alice присутствует в списке, удалим элемент "Alice
    
print(people)       # ["Tom", "Bob", "Sam"]
```
#### Удаление: ключевое слово, оператора del

```python
people = ["Tom", "Bob", "Alice", "Sam", "Bill", "Kate", "Mike"]
# В качестве параметра оператору del передается удаляемый элемент или набор элементов:
del people[1]   # удаляем второй элемент  # ["Tom", "Alice", "Sam", "Bill", "Kate", "Mike"]
del people[:3]   # удаляем по четвертый элемент не включая # ["Bill", "Kate", "Mike"]
del people[1:]   # удаляем со второго элемента # ["Bill"]
```

#### Изменение списка
```python
nums: list[int] = [10, 20, 30, 40, 50]
nums[1:4]=[11, 22] # замена элементов с индекса 1 по 3 на список [11, 22], получим # [10, 11, 22, 50]
```

#### Подсчет вхождений

```python
people = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]
people_count: int = people.count("Tom") # результат 3
```

#### Сортировка

```python
people = ["Tom", "Bob", "Alice", "Sam", "bill"]
people.sort()  # по возрастанию # ["Alice", "Bill", "Bob", "Sam", "Tom"]

# Чтобы отсортировать данные в обратном порядке, необходимо после сортировки применить метод reverse():
people.sort()
people.reverse()  # по убыванию # ["Tom", "Sam", "Bob", "Bill", "Alice"]


# При сортировке сравниваются два объекта, и тот, который "меньше", ставится перед тем, который "больше".
# И чтобы установить правило сортировки, мы передаём в метод sort() функцию сортировка, в качестве параметра:
# определяем функцию сравнения
def comparable(number): return str.lower


people.sort(key=comparable)  # сортировка по правилу, заданному функцией key (здесь без учета регистра)

# Используем функцию sorted
sorted_people1 = sorted(list)  # сортирует список list
sorted_people2 = sorted(list, key=str.lower)  # сортирует список list по правилу, заданному функцией key
```
#### Фильтрация, filter()

Для фильтрации списка применяется функция filter().
Функция принимает два параметра:
- fun: функция-условие, она получает каждый элемент коллекции и возвращает:
  - True, если элемент соответствует условию,  
  - False, если элемент не соответствует условию
- iter: фильтруемая коллекция

```python
numbers: list[int] = [-5, -4, -3 ,-2, -1, 0, 1, 2, 3, 4, 5]

# определяем функцию фильтрации: True, если число больше 0
def condition(number): 
  return number > 0

# вызываем функцию filter и передаём ей параметры:
#   condition - функция сравнения
#   numbers - список, который следует отфильтровать 
result = filter(condition, numbers)

# Или можно использовать лямбда-выражения:
result = filter(lambda n: n > 1, numbers)
 
for n in result: print(n, end=" ")      # 1 2 3 4 5

```

Пример с более сложными объектами

```python
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
         
cats = [ Cat("Tom", 1.2), Cat("Oliver", 2.8), Cat("Leo", 2.2), Cat("Max", 0.1)]
 
# фильтрация элементов, у которых age > 1
cats_view = filter(lambda p: p.age > 1, cats)
  
for cat in cats_view:
    print(f"Name: {cat.name} Age: {cat.age}")
```

#### Проекция списка

Здесь не используется структура Map, которая описывает отображение одного множества на другое, 
а используется функция преобразования.

```python
# Исходный список
numbers = [ 1, 2, 3, 4, 5]
# Функция преобразования, здесь преобразуем число в его квадрат
def square(number): return number * number
# Теперь преобразуем список, используем функцию map, 
# которой передаём:
#   первым параметром функцию преобразования square
#   вторым параметром - преобразуемый список
result = map(square, numbers)   # result будет равен 1 4 9 16 25

# Как вариант, используем лямбда-выражение
result = map(lambda n: n * n, numbers)
```

Пример преобразования списков более сложных объектов
```python
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
         
cats = [ Cat("Tom", 1.2), Cat("Oliver", 2.8), Cat("Leo", 2.2), Cat("Max", 0.1)]
 
# Получаем список имён, лямбда - преобразует объект в его имя
cats_view = map(lambda p: p.name, cats)
  
for name in cats_view:
    print(f"Name: {name}", end=", ") # Name: Tom, Name: Oliver, Name: Leo, Name: Max,
```

#### Минимальное и максимальное значения

```python
numbers = [9, 21, 12, 1, 3, 15, 18]
print(min(numbers))     # 1
print(max(numbers))     # 21
```

#### Копирование списков

Если обе переменных будут указывать на один и тот же список, то изменение одной переменной, затронет и другую переменную:
```python
people1 = ["Tom", "Bob", "Alice"]
people2 = people1
people2.append("Sam")   # добавляем элемент во второй список
# people1 и people2 указывают на один и тот же список
print(people1)   # ["Tom", "Bob", "Alice", "Sam"]
print(people2)   # ["Tom", "Bob", "Alice", "Sam"]
```
Метод copy() позволяет сделать копию списка.

```python
people1 = ["Tom", "Bob", "Alice"]
people2 = people1.copy()        # копируем элементы из people1 в people2
# people1 и people2 указывают на разные списки
people2.append("Sam")           # добавляем элемент ТОЛЬКО во второй список
print(people1)   # ["Tom", "Bob", "Alice"]
print(people2)   # ["Tom", "Bob", "Alice", "Sam"]
```

#### Соединение списков
```python
people1 = ["Tom", "Bob", "Sam"]
people2 = ["Tom", "Bob", "Tim", "Bill"]
people3 = people1 + people2
print(people3)   # ["Tom", "Bob", "Sam", "Tom", "Bob", "Tim", "Bill"]
```
