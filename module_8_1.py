# Задание "Программистам всё можно":
def add_everything_up(a, b):
    try:
        return a + b  # Когда нам поступают два числа, пробуем  выполнить сложение
    except TypeError:  # Обработка случаев, когда типы разные и сложение невозможно
        return str(a) + str(b)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

