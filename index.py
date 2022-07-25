# print('hello')

# print(27//4) #вычисляет без дробной части
# print(27%4) #вычисляет остаток
# print(27**4) #возводит в степень

# Переменные

# hello = 234
# first = 43
# first = 'hello aziret'
# print(first+hello)  

# name = 'John'
# print(name)
# surname = 'Doe'
# print(surname)
# print(name + surname)
# print(name + ' ' + surname)
# name = 'Mark'
# surname = 'Twain'
# print(name + ' ' + surname)

# Типы данных
 
# integer это цифры
# float это дробные цифры
# string это строки
# bool это истина или ложь

# one = 1
# two = 1.435
# three = 'ghhidfui'
# four = True
# print(type(four))

# five, six = 5, 6
# print(five, six)

# """ - дают возможность делать отступы в данных

# surname = 'Sasha\'s a beautiful girl. \nShe is smart' 
# print(surname)
# \n дает возможность сделать отступ

# Форматирование строк

# 1 способ

# name = 'John'
# surname = 'Nash'
# company = 'Google'
# bio = '''{0} {1} is a talanted Python developer.
# He works at {2}.
# '''.format(name, surname, company)
# print(bio)

# 2 способ


# name = 'John'
# surname = 'Nash'
# company = 'Google'
# bio = f'{name} {surname} is a talanted Python developer.\nHe works at {company}.'
# print(bio)

# f-строки можно совмещать с тройными ковычками

# Срезы

# language = 'Python'

# print(language[start:stop])
# print(language[start:stop:step])
# print(language[start:])
# print(language[:stop])
# print(language[::step])

# print(language[2]) # терминал покажет символ, у которой индекс равен 2

# print(language[:2]) # терминал покажет символы, у которых индекс меньше 2
# print(language[3:]) # терминал покажет символы, у которых индекс равен 3 или больше

# print(language[-1]) # терминал покажет последний символ

# print(language[::2]) # терминал покажет каждый второй символ(у которых индекс 0, 2, 4 и т.д.)
# print(language[::3]) # # терминал покажет каждый третий символ(у которых индекс 0, 3, 6 и т.д.)

# a = 'method'
# print(a.upper()) # изменяется только здесь, строки неизменяемый тип данных
# print(a) 

# A = a.upper() # измененные данные мы поместили в новую переменную
# print(A)

# Условие

# age = int(input('Введите возраст'))
# if age <= 17:
#     print('Get ready')
# elif age >= 18 and age <40:
#     print('Join the army')
# elif age >= 40 and age <60:
#     print('you can be useful')
# elif age >=60 and age < 100:
#     print('Retired')
# else:
#     print('you are dead')

# digit = int(input('hi'))
# digit = digit%2
# if digit == 0:
#     print('четное число')
# elif digit != 0:
#     print('нечетное число')

# list - изменяемый тип данных

# a = [1,2,463,True,[43,7543,7],'ugaauhi']
# print(a)
# print(a[2]) # индекс
# print(a[0:4]) # срез

# print(a[4][2]) # обращение к значению списка в списке

# a[3] = False
# print(a[3])

# b = [57,96,76]

# a.extend(b)
# print(a)

# a.pop(1) # pop удаляет по индексу
# print(a)

# a.remove(1) # remove удаляет по значению
# print(a)

# contact_name = ['Aidana', 'Arsen', 'Bektur', 'Kumar', 'Dauren']

# name = input('Search ')
# name = name.title()
# if name in contact_name:
#     print('Yes')
# else:
#     print('No')

# Циклы

# for i in contact_name:
#     print(i + 'bek')

# b=[2,3,6,23,7,98]
# for i in b:
#     res = i * 2
#     c = [res]
#     for i2 in c:
#         print(i2 ** 2)

# append() добаавляет элемент в список
# insert() принимает в качестве первого аргумента позицию, на которую нужно вставить элемент, а вторым — сам элемент
# split() разбивает строки на слова

# fruits = ['Orange', 'Grape', 'Peach', 'Banan', 'Apple']
# fruits.sort()
# print(fruits) # 1
# fruits.sort(reverse=True)
# print(fruits) # 2

# переменные зависят друг от друга если они ссылаются на один объект, поэтому лучше использовать метод copy()

# set неизменяемый тип данных, который хранит в себе уникальные значения

# tuple изменяемый тип данных

# a = (1515) # это int
# print(type(a))

# a = (1515,) # это tuple. если в кортеже 1 значение, то после нее нужно поставить запятую
# print(type(a))

# b, c, d = ('dfs','affad','faef')
# print(type(b))

# dict изменяемый тип данных

# student = {'name': 'Ivan', 'age': 12} # эта и нижняя строка идентичны
# print(student['name'], student['age'])
# print(student['name'])
# student['name'] = 'Vasya'

# student = dict(name = 'Ivan', age = 12)
# print(student[1])

# student[1] = 'Radik'
# print(student[1])

# del student['age']
# print(student)

# Использование метода pop()

# sneakers = dict(brand='Adidas', price='9990 RUB', model='Nite Jogger')

# model = sneakers.pop('model')

# print(sneakers) # -> {'brand': 'Adidas', 'price': '9990 RUB'}
# print(model)    # -> Nite Jogger
# print(type(model))    

# else срабатывает только после завершения цикла

# contact_name = {
#     'Aidana':771404040,
#     'Arsen':771404043,
#     'Bektur':771404047,
#     'Kumar':771404045,
#     'Dauren':771404048
#     }
    
# act = int(input('''Выберите действие:
# 1. Добавление нового контакта
# 2. Удаление контакта
# 3. Поиск контакта
# 4. Просмотр контакта '''))

# if act == 1:
#     print('Добавить контакт')
#     name = input('Введите имя контакта ')
#     number = input('Введите номер контакта ')
#     contact = {name: number}
#     print(contact)
#     contact_name[name] = number
#     act = int(input('''Выберите действие:
#     1. Добавление нового контакта
#     2. Удаление контакта
#     3. Поиск контакта
#     4. Просмотр контакта '''))
# else:
#     print('Ошибка')
# if act == 2:
#     print('Удалить контакт')
#     delete = input('Имя контакта ')
#     delete = delete.title()
#     if delete in contact_name:
#         contact_name.pop(delete)
#     else:
#         print('Ошибка')

# while True: 
#     command = input("1 - add \n 2 - delete \n 3 - find \n 4 - look all \n") 
#     if command == '1': 
#         add_name = input("Name:") 
#         add_number = int(input("Num:")) 
#         contact_name.setdefault(add_name, add_number) 
#         print(f"Контакт {add_name} успешно добавлен") 
#     elif command == '2': 
#         delete_cont = input("Какой контакт хотите удалить:") 
#         if delete_cont in contact_name: 
#             contact_name.pop(delete_cont) 
#             print("Контакт успешно удалён") 
#         else: 
#             print("Такого контакта нет") 
#     elif command == '3': 
#         find_name = input("Какой контакт хотите найти? ") 
#         title_find = find_name.title() 
#         if title_find in contact_name: 
#             print("Контакт найден") 
#             print(contact_name[title_find]) 
#         else: 
#             print("Контакт не найден") 
#     elif command == '4': 
#         print(contact_name) 
#     else: 
#         print("Неверная команда")

# if act == 3:
# nameSearch = input('Search ')
# nameSearch = nameSearch.title()
# if nameSearch in contact_name:
#     print(nameSearch)
# else:
#     print('No')

# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне.
# Fruits = ['Яблоко', 'Банан', 'Киви', 'Арбуз', 'Манго', 'Груша', 'Помидор', 'Дыня']
# print(Fruits)


# Задача-2:
# Даны два произвольные списка. Удалите из первого списка элементы, присутствующие во втором списке.
# lst1 = [1, 3, 5, 7, 9]
# lst2 = [3, 8, 6, 5]

# for e in lst2:
#     if e in lst1:
#         lst1.remove(e)
#         print(lst1, lst2)

# # Задача-3:
# # Дан произвольный список из целых чисел. Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# # если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
# lst = [1, 4, 3, 42, 48, 34, 4, 5, 10, 7, 8, 9]

# for odd in lst:
#     if odd % 2 == 0:
#         nodd = str(odd / 4)
#     elif odd % 2 == 1:
#         nodd = str(odd * 2)

# lstnodd =list(nodd)
# print(lstnodd)

# # Задача-4: Дано произвольное целое число, вывести самую большую цифру этого числа.
# num = 3384456779
# print(num)

# num = str(num)
# print(num)

# num = list(num)
# print(num)

# print(max(num))

# for tbd in num:
#     ttbd = 0
#     while ttbd <= 9:
#         ttbd +=1
#     if tbd <= ttbd:
#         print(tbd)

# Задача-5: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
# Пусть дана дата 01.01.2000
# dana_data = '23.07.2021'

# lst = [23,5,6,7,2,78,25,24]

# i = 0

# while True:
#     if lst[i] == 24:
#         print('Я нашел 24')
#         break
#     i +=1

# Задача №1 - нужно объединить два списка, а повторяющиеся элементы выкинуть
# list_names = ['Aza', 'Kuma', 'Bama', 'Anna', 'Vika']
# get_names = ['Kuma', 'Anna', 'Adilet', 'Sasha']

# # Задача №2 - в строке нужно найти все числа и составить их в список "frg5gth57ubdfh9sbf4dsbdr0dxbf2"
# my_str = "frg5gth57ubdfh67 sbf4dsbdr0dxbf 2"

# # list_names = list_names+get_names
# # list_names = set(list_names)
# # print(list_names) 

# # 3

# for i in list_names:
#     if i in get_names:
#         print(i)

# # 1 
# new = list(set(list_names + get_names))
# # 2
# new_lst = list(set(list_names) - set(get_names))
# # 3
# new_lst = list(set(list_names) ^ set(get_names))
# # 4
# new_lst = list(set(list_names) & set(get_names))

# У вас есть словарь студентов  IT Academy:
students = [
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'John', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Andrew', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Marcus', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Agnes', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Doe', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Michael', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Jennifer', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Angela', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Eniston', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Albert', 'age': 33, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nash', 'age': 28, 'course': 'python', 'gender': 'Male'},
    {'name': 'Nicolas', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Alex', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Martin', 'age': 22, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Mikkel', 'age': 24, 'course': 'python', 'gender': 'Male'},
    {'name': 'Susann', 'age': 25, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Steve', 'age': 26, 'course': 'python', 'gender': 'Male'},
    {'name': 'Mark', 'age': 18, 'course': 'java', 'gender': 'Male'},
    {'name': 'Johnathan', 'age': 15, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aidin', 'age': 20, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Mirbek', 'age': 25, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aidana', 'age': 40, 'course': 'python', 'gender': 'Female'},
    {'name': 'Atay', 'age': 42, 'course': 'java', 'gender': 'Male'},
    {'name': 'Chyngyz', 'age': 17, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Aigerim', 'age': 16, 'course': 'java', 'gender': 'Female'},
    {'name': 'Jyldyz', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Emir', 'age': 34, 'course': 'java', 'gender': 'Male'},
    {'name': 'Emirlan', 'age': 12, 'course': 'javascript', 'gender': 'Male'},
    {'name': 'Nursultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
    {'name': 'Aliaskar', 'age': 19, 'course': 'java', 'gender': 'Male'},
    {'name': 'Aktan', 'age': 21, 'course': 'java', 'gender': 'Male'},
    {'name': 'Adyl', 'age': 14, 'course': 'python', 'gender': 'Male'},
    {'name': 'Gloria', 'age': 23, 'course': 'java', 'gender': 'Female'},
    {'name': 'Janyl', 'age': 16, 'course': 'python', 'gender': 'Female'},
    {'name': 'Meerim', 'age': 12, 'course': 'javascript', 'gender': 'Female'},
    {'name': 'Sultan', 'age': 13, 'course': 'python', 'gender': 'Male'},
]
print(len(students))

i = -1

while i < 37:
    i += 1
# #1) высните процентное соотношение мужского пола и женского.
# print(len(students[i]['gender'])/len(students[i]['gender']))

# if students[i]['gender'] != 'Male':
#     print(len(students[i]['gender']))
    print(students[i].get('gender'))
    # gender = []
    # for g in students[i]['gender']:
    #     gender.append(g)
    # print(gender)
    gender = list(students[i].get('gender'))
    print(gender)

    # print(len('Male')/len('Famale'))
    # if (students[i].get('gender')) != 'Male':
    #     print(students[i]['gender'])

# print(len(students[i].get('gender')))
#2) выведите всех студентов с курса python

#3) уберите дубликаты

#4) выведите студентов, которые старше 30 и найдите процент их количества относительно других

#5) отсортируйте студентов по:
        # имени
        # курсу
        # полу
        # возрасту

#6) все студенты курса  javascript  перешли на курс  python.  Как вы поменяете это в словаре ?
# Напишите код

#7) Добавьте по 5 новых студентов на курсы  java  и  python

#8) Отчислите всех студентов младше 15 лет

