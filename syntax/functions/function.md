[content.md](../content.md)

### Функции

- Функции представляют собой блок кода, выполняющий определенную задачу.
- Функцию можно повторно использовать в других частях программы.
- Функция может иметь параметры вызова
- Функция может вернуть результат с помощью оператора return
- Функции, которые не находят в конце оператор return, возвращают None

Список методов можно посмотреть в документации:   
[Например, методы для работы со строкой.](https://docs.python.org/3/library/stdtypes.html#string-methods)

Формальное определение функции:
```
def имя_функции ([параметры]):  
    инструкции
```
```python
# определение функции say_hello() без параметров и не возвращающую результата
def say_hello():
    print("Hello")

print("Bye")  # этот вызов функции print уже не входит в определение функции say_hello()
say_hello()  # вызов функции say_hello()
# -------------------------------------------
# определение функции get_message() без параметров и возвращающую результат типа string
def get_message():
    return "result"

message = get_message()  # вызов get_message(), message получает строку "result"
print(message)  # result,

# прямая передача результата вызова функции get_message в параметр другой функции
print(get_message())
# -------------------------------------------
# функция get_result() с вычислением в вызове оператора return
def get_message():
    return 2*2+4
# -------------------------------------------
# функция demo() с использованием оператора return для выхода из фунции
def demo(a, b):
    if a>b: return 
    else: print(" a> b ")
# -------------------------------------------
# Функция с одним необязательным параметром
def print_age(name, age=18):  # объявление функции с параметрами name и age
    # тело функции, здесь параметры используются, как переменные
    print("name=  " + name + ", age = " + str(age), end=", ")
    name = "!!"  # параметру можно присвоить новое значение
    print(name)

# Вызов функции с использованием передачи параметров по позиции
print_age("Tom", 12)  # вызов функции say_hello с параметрами "Tom", 12
# name=  Tom, age = 12, !!
print_age("Tom")
# name=  Tom, age = 18, !!
# -------------------------------------------
# Функция с одним необязательным параметром
def print_person(name, age=18):
    print(f"Name: {name}  Age: {age}")

# Вызов функции с использованием именования параметров
print_person(age=22, name="Tom")
print_person(name="Tom", age=22)
print_person(name="Tom")
# -------------------------------------------
# Правее символа '*,' все параметры должны быть именованные.

def print_1(name, *, age, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")

print_1("John", age=18, company="Super startup!")  # Name: John  Age: 18  company: Super startup!
# -------------------------------------------
# Все параметры, левее символа '/,' будут позиционными.
def print_2(name, /, age, company = 'MS'):
    print(f"Name: {name}  Age: {age}  Company: {company}")

print_2("Tom", company="JetBrains", age = 24)  # Name: Tom  Age: 24  company: JetBrains
print_2("Bob", age = 41)  # Name: Bob  Age: 41  company: MS
# -------------------------------------------
# Допускается использовать оба символа '*,' и '/,' одновременно.
def print_3(name, /, age = 18, *, company):
    print(f"Name: {name}  Age: {age}  Company: {company}")

print_3("Sam", company ="Google")               # Name: Sam  Age: 18  company: Google
print_3("Tom", 37, company ="JetBrains")        # Name: Tom  Age: 37  company: JetBrains
print_3("Bob", company ="Microsoft", age = 42)  # Name: Bob  Age: 42  company: Microsoft

def a_void_function():
    a = 1
    b = 2
    c = a + b 
    # неявно возвращается None
 
x = a_void_function()   # None
print(x)                # None

def improper_return_function(a):
    if (a % 2) == 0:
        return True
    # в случае, если условие не выполняется, неявно возвращается None
 
x = improper_return_function(3) # None
print(x)                        # None
```

### Локальные функции

Функции могут быть определены внутри других функций - такие функции называют локальными.  
Они могут использоваться только внутри той функции, в которой они определены. 
```python
# внешняя функция
def print_messages():
    # определение локальных функций
    def say_hello(): print("Hello")
    def say_goodbye(): print("Good Bye")
    # вызов локальных функций
    say_hello()
    say_goodbye()
 
# Вызов внешней функции
print_messages()
 
#say_hello() # функция say_hello недоступна вне функции print_messages 
```

### Параметры

- Функции используют позиционные и именованные параметры.  
- Внутри функции параметр можно использовать, как переменную.

#### Значения по умолчанию

Для параметров можем использовать значения по умолчанию.  
Если для этих параметров значения не указаны, будут использованы значения по умолчанию.
Необязательные параметры должны идти после обязательных
```python
def say_hello(name="Tom"):
    print(f"Hello, {name}")

say_hello()         # будет выведено "Tom"
say_hello("Bob")    # будет выведено "Bob"

# Необязательные параметры должны идти после обязательных
def print_person(name, age = 18):
    print("Name:"+ name + ", Age:" + str(age))

print_person("Tom") # Используется значение age по-умолчанию age = 18.

# Мы можем сделать все параметры необязательными:
def print_a_b(name="Tom", age = 18):
    print("Name:"+ name + ", Age:" + str(age))
```

#### Неопределенное количество параметров

Можно передавать неопределенное количество значений, фактически задавая кортеж значений, как параметр функции, используя символ *

```python
def sum(*numbers):      # numbers - это кортеж
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")
 
 
sum(1, 2, 3, 4, 5)      # sum = 15
sum(3, 4, 5, 6)         # sum = 18
```

### Функция main

Удобно иметь главную функцию, в которой вызываются все остальные. Обычно её называют main()

```python
def main():
    say_hello()
    say_goodbye()
 
def say_hello():    print("Hello")
def say_goodbye():  print("Good Bye")
 
# Вызов функции main
main()
```

### Функция как тип

В Python функция фактически представляет отдельный тип.  
Мы можем функцию присвоить переменной.
А затем, используя эту переменную, вызывать данную функцию.

```python
# Определяем функции say_hello() и say_goodbye()
def say_hello(): print("Hello")
def sum(a, b): return a + b
def multiply(a, b): return a * b

message = say_hello # присваиваем переменной message функцию say_hello
message()           # вызываем функцию say_hello, используя переменную message, обратите внимание на синтаксис вызова
# Hello
operation = sum
result = operation(5, 6) # 11
operation = multiply
result = operation(5, 6) # 30
```

#### Функция как параметр функции

Мы можем передать функцию в качестве параметра в другую функцию. 

```python
def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
 
def sum(a, b): return a + b
def multiply(a, b): return a * b
 
do_operation(5, 4, sum)         # result = 9
do_operation(5, 4, multiply)   # result = 20
```
#### Функция как результат функции

Одна функция может возвращать другую функцию

```python
def sum(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
  
def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply
```
[content.md](../content.md)




