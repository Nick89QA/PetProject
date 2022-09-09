str_1 = "hello"
str_2 = "WORLD"
print(str_1)
# применяем функцию dir
print(dir(str_1))

# применяем функцию upper она переводит в верхний регистр строку
print(str_1.upper())

# применяем функцию title она переводит первую букву слова в верхний регистр
print(str_1.title())

# применяем функцию low она переводит слова в нижний регистр
print(str_2.lower())

# код выполняется сверху вниз теперь будет в переменной name "alex"
name = "Ivan"
name = "Alex"
a = "Hello {}"
result = a.format(name)
print(result)

# функция format в которую помещяем две переменные
first_name = "Ivan"
last_name = "Ivanov"
a = '{} {}'
result = a.format(first_name, last_name)
print(result)
print("Меня зовут : " + result)

result = f'{first_name} {last_name}'
print(result)
