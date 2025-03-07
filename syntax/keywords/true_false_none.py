import keyword
print(keyword.kwlist)

# True и False в Python — это то же самое, что 1 и 0
print(True == 1)    # True
print(True == 2)    # False
print(False == 0)   # True
# ---------------------------------
# None — это специальная константа в Python, которая представляет отсутствие значения или нулевое значение.
# Функции, которые ничего не возвращают, автоматически возвращают объект None. Также функции, которые не находят в конце оператор return, возвращают None
print(False == None)   # False


def a_void_function():
    a = 1
    b = 2
    c = a + b
    # неявно возвращается None


x = a_void_function()   # x == None
print(x)                # None


def improper_return_function(a):
    if (a % 2) == 0:
        return True
    # в случае, если условие не выполняется, неявно возвращается None


x = improper_return_function(3)     # None
print(x)                            # None