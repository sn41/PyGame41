[**< типы и переменные**](variables_and_types.md)

### Строка, тип str  

```python
# Строка представляет последовательность символов (в кодировке UnicodePython 3.x), 
# заключенную в одинарные или двойные кавычки.
str1="hello"
str2='hello'

# Длинную строку можно разделить на несколько строк, заключив её в скобки.
str3=('Длинную строку можно разделить '
      'на несколько строк, заключив её в скобки')

# Многострочный текст, заключается в тройные двойные или одинарные кавычки:
text='''О сколько нам открытий чудных
      Готовят просвещенья дух
      И Опыт, сын ошибок трудных,
      И Гений, парадоксов друг,
      И Случай, бог изобретатель.
      '1829 г.'''

'''
А это многострочный 
комментарий
'''

# Управляющие последовательности в строке
# \\: позволяет добавить внутрь строки слеш
# \': позволяет добавить внутрь строки одинарную кавычку
# \": позволяет добавить внутрь строки двойную кавычку
# \n: переход на новую строку
# \t: табуляция (4 отступа)
# \b: забой - удаление предудущего символа

string = "Message:\n\"Hello World\""

wrong_path = "C:\python\name.txt"   # ошибка, следует экринировать символ \
path = "C:\python\\name.txt"        # правильно
```
[**Форматированные строковые литералы s-string**](fstring.md)

[**< Типы и переменные**](variables_and_types.md)