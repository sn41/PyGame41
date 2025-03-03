### Лямбда-выражения

Это небольшие анонимные функции, которые определяются с помощью оператора lambda.

```python
message = lambda: print("hello")
square = lambda n: n * n
sum = lambda a, b: a + b

message()           # hello 
print(square(4))    # 16
print(sum(4, 5))    # 9
# -------------------------------------------------
# передача лямбда-выражения в качестве параметра
def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")

do_operation(5, 4, lambda a, b: a * b)  # result = 20
# ------------------------------------------------- 
# возвращение лямбда-выражений из функций:
def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b

operation = select_operation(1)  # operation = sum
print(operation(10, 6))  # 16
```