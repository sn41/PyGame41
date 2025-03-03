class SuperClass:
    def super_method(self):
        print("Super Class method called")


# Определяем класс, который наследует SuperClass
class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")


# Определяем класс, который наследует DerivedClass1
class DerivedClass2(DerivedClass1):
    def derived2_method(self):
        print("Derived class 2 method called")


# Создаем объект класса DerivedClass2
d2 = DerivedClass2()

# Вызываем методы
d2.super_method()
d2.derived1_method()
d2.derived2_method()