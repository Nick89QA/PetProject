num_1 = 10
num_2 = 200022
result = num_1 + num_2
print(result)

num_1 = 1000
num_2 = 2000
result = num_1 + num_2
print(result)


# пишем функцию чтобы сократить код
def summ(num_3, num_4):  # функция принимает аргументы
    result = num_3 + num_4
    print("Hello")
    print(result)


summ(333, 443434)  # задаем аргументам значение int
summ(323232, 313333)

summ(num_3="Hello ", num_4="World")  # задаем аргументы типа str и определяем порядок


def hi(name="Alex"):  # задаем параметр аргументу
    print("Hello " + name)


hi("Alex")
# еще одна реализация функции
surname = "Nick" # обьявляем переменную и работаем с ней в функции


def sur(surname):


    print("Hi " + surname)

sur(surname)
