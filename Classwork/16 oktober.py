# # коллекция [начало:конец:шаг] конец не включается
# text = 'Privet mir!'
# print(text[:5])
# print(text[::2])
# print(text[::-1])
# print(text[:-2])
# print(text[:-2:-1])
# print(text[8:11])
# print(text[8:])
# print(text[:])
# print(text[0::1])

# word = 'mir' 
# #word - ссылка на переменную, 'mir' - данные,записанные в памяти компьютера
# word[0] = 'p' # возникает ошибка TypeError: 
# 'str' object does not support item assignment

# # СПИСКИ
# numbers = [10, 20, 30, 40, 50]
# mixed_lists = [10, 20.55, 'mama']

# print(numbers[0])
# print(numbers[-1])
# print(numbers[1:3])
# print(numbers[::-1])

# # изменение и удаление элементов
# numbers[2] = 100
# print(numbers)

# numbers = []
# for i in range(10):
#     numbers.append(int(input()))
# print(numbers)

# # удаление через оператор del
# numbers = [10, 20, 30, 40, 50]
# del numbers[-1]
# print(numbers)

# numbers = [10, 20, 30, 40, 50]
# del numbers[::2]
# print(numbers)

# проверка наличия элемента, отсортировать, удаление, добавление

# # возвращает тру если в списке есть х
# print(1 in [1, 2, 3])
# print(1 not in [1, 2, 3])

# print([1, 2] + [3,4,5])

# print([1, 2, 6] * 5)

# numbers = [10, 20, 30, 40, 50]
# print(len(numbers))

# print(min([5, 955, -1]))
# print(max([5, 955, -1]))

# # метод index
# print([1,2,3,4,5,6,2].index(2)) # на каком индексе стоит искомое число, 
# найдётся только первое найденное число

# # метод count
# print([1,2,3,4,5,6,2].count(2)) # сколько элементов в списке

# # метод clear
# list_name = [1,2,3,4,5,6,2]
# list_name.clear()
# print(list_name) # удаление всех элементов


# # метод copy
# list_name = [1,2,3,4,5,6,2]
# list_copy = list_name.copy() # копирование списка
# list_copy_2 = list_name
# list_name.append(100)
# print(list_copy) 
# print(list_name)
# print(list_copy_2)

# # метод extend
# s = [1,2,3]
# t = [4,5]
# s.extend(t) # сложение списков s += t
# print(s)

# # метод insert
# s = [1,2,3]
# s.insert(1,2) # на индекс 1 мы ставим число 2
# print(s)

# # метод pop возвращает и удаляет последний элемент
# s = [1,2,3]

# print(s.pop())
# print(s)

# # # метод удаления указанного элемента
# # удалить только первый встреченный элемент
# s =[1,2,3,45,6,4,8,9, 2,1,2]
# s.remove(2) # удалить элемент "2"
# print(s)

# # обратный порядок элементов
# s =[1,2,3,45,6,4,8,9]
# s.reverse() # s = s[::-1]
# print(s)

# # сортировка, меняет список!!!
# s = [654,43,2,56,896]
# s.sort()
# print(s)

# s = [654,43,2,56,896]
# s.sort(reverse = True)
# print(s)

# # сортировка, НЕ меняет список!!! 
# # нужна новая переменная
# s = [654,43,2,56,896]
# s = sorted(s)
# new_s = sorted(s, reverse = True)
# print(s)
# print(new_s)

# # удалить все одинаковые элементы, 
# преобразовать во множество(удалятся дубликаты), 
# потом вернуть в лист

# s = [1,5,2,3,2,6,7,8,9]
# while 2 in s:
#     s.remove(2)
# print(s)

# # КОРТЕЖ - НЕИЗМеняемый список, но упорядоченный, 
# срезы индекс, лен каунт индекс, не работают изменения(ремув и т.д.)

# numbers = (1,2,3,4,5)
# one_number = (1, ) # запятая ОБЯЗАТЕЛЬНА

# print(numbers)
# print(one_number)
# print(type(numbers))

# a = 1
# b = 2
# (a, b) = (b, a)
# print(f'a = {a}, b = {b}')

# # преобразование между коллекциями

# text = "Hello world"
# list_symbols = list(text)
# tuple_symbols = tuple(text)
# text_from_list = str(list_symbols)
# print(list_symbols)
# print(tuple_symbols)
# print(text_from_list)

# # множества - SET 
# 1.удаляются повторяющиеся элементы, 
# 2.порядка внутри НЕТ, нет индексов 
# и словари

# vowels = {'a', 'e', 'i', 'o', 'y', 'u', 'o', 'o'}
# print(vowels)
# print(type(vowels))

# # превратить во множество:
# empty_set = set()

# word = 'collection'
# letters = set(word)
# print(letters)

# vowels = {'a', 'e', 'i', 'o', 'y', 'u', 'o', 'o'}
# letter = input()
# if letter.lower() in vowels:
#     print('Vowel')
# else:
#     print('Not vowel')

# # объединить множества,повторы удаляться
# s_1 = {1,2,3}
# s_2 = {3,4,5}
# s_union = s_1.union(s_2) # s_1 | s_2
# print(s_union)

# # пересечение множеств
# s_1 = {1,2,3}
# s_2 = {3,4,5}
# s_intersection = s_1.intersection(s_2) #s_1 & s_2
# print(s_intersection)

# # разность множеств,вернет что есть в первом и нет во втором
# s_1 = {1,2,3}
# s_2 = {3,4,5}
# s_dif = s_1.difference(s_2) # s_1 - s_2 или s_2 - s_1
# print(s_dif)

# # вернет что есть в первом и что есть во втором, кроме повторов
# s_1 = {1,2,3}
# s_2 = {3,4,5}
# s_sym_dif = s_1.symmetric_difference(s_2) # s_1 ^ s_2

# # пример
# vowels = {'a', 'e', 'i', 'o', 'y', 'u', 'o', 'o'}
# letters = set("collection")
# print(', '.join(letters & vowels))

# СРАВНЕНИЕ множеств

# s_1 = {1,2,3}
# s_2 = {3,2,1}
# print(s_1 == s_2)

# s_1 = {1,2,3}
# s_2 = {1,2,3,4}
# print(s_1 <= s_2) # входит ли мн. 1 во мн. 2?

# # метод add
# s = set()
# s.add(1)
# print(s)

# s_1 = {1,2,3}
# s_1.remove(2)
# print(s_1)

# s = {1,2,3,4,2}
# s.discard(s) # работает как remove, но не возвращает ошибку ключа
# print(s)

#СЛОВАРИ(быстро работают) -неупорядоченная коллекция, 
# к которому к каждому слову проставляется 
# ключ (уникальный идентификатор)

# countries_and_capitols = [('Russia', 'Moscow'), ('USA', 'Vashington')]
# for country in countries_and_capitols:
#     #print(country) 
#     # можно в середине цикла прописать print,чтобы проверить данные
#     if country[0] == 'USA':
#         print(country[1])
#         break

# countries_and_capitols = {'Russia': 'Moscow', 
#                           'USA': 'Vashington',
#                           'France': 'Paris'}
# print(countries_and_capitols['USA'])

# countries_and_capitols = {'Russia': 'Moscow', 
#                           'USA': 'Vashington',
#                           'France': 'Paris'}
# countries_and_capitols['Georgia'] = 'Tbilisi'
# print(countries_and_capitols['Georgia'])
# if 'Serbia' in countries_and_capitols:
#     print(countries_and_capitols['Serbia'])
# else:
#     print('No Serbia')

# for country in countries_and_capitols:
#     print(country, countries_and_capitols[country])

# for key in countries_and_capitols.keys():
#     print(key)

# for values in countries_and_capitols.values():
#     print(values)

# for key, values in countries_and_capitols.items():
#     print(key, values)

# # str

# s = ('jfhbdshgvhtbybhdjfvb')
# d = s.partition('bd')
# print(d)
# print(type(d))