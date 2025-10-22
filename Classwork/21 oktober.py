# num = []
# for i in range(5):
#     num.append(int(input()))
# print(num)

# num = [int(input()) for i in range(5)]
# print(num)

# использование СПИСОЧНОГО ВЫРАЖЕНИЯ List comprehension
# ЛИШНИЕ ВЫЧЕСЛЕНИЯ выносить за цикл, чтобы не загружать оперативную память
# например avg = sum(num) // len(num) лучше вынести за цикл

# num = [int(input()) for i in range(5)]
# print(num)

# avg = sum(num) // len(num)
# num = [elem for elem in num if elem > avg]
# print(avg)
# print(num)

# ГЕНЕРАТОРЫ - экономят ресурсы, предоставляют данные только по запросу
# записываются в КРУГЛЫЕ скобки

# num = (int(input()) for i in range(5))
# print(num) # <generator object <genexpr> at 0x0000027DECB8C820>

# матрица

# matrix = [[int(x) for x in input().split()] for i in range(5)]
# print(matrix)

# #двумерный список из нулей
# zeros = [[0] * 5] * 5
# print(zeros)
# print([0][0])
# zeros[0][0] = 1

# zeros = [[0] * 5 for i in range(5)] 

# с for создаётся новый объект,
# поэтому и меняется каждый объект отдельно (например, заменяется значение только в [0][0]),
# а не во всём столбце

# print(zeros)
# zeros[0][0] = 1
# for i in zeros:
#     i[1] = 5
# print(zeros)
   

# coutries = {'Russia': ['russian'],
#             'Belarus': ['belorus','russian'],
#             'Belgia': ['doitch','franch','niderland']}
# mult_lang = [country for (country, lang) in coutries.items() if len(lang) > 1]
# print(mult_lang)

# countries = {country: capital for country, capital in [('Russia', 'Moscow'), ('Belarus', 'Minsk')]}
# print(countries)
# print(type(countries))

# СОБСТВЕННЫЕ ФУНКЦИИ - переиспользовать один и тот же код без копирования, 
# сделать программу более читаемой, структурированной за счет деления на блоки

# def имя_функции(аргументы):
    # тело функции

# def only_even(numbers):
#     result = True
#     for x in numbers:
#         if x % 2 != 0:
#             result = False
#             break
#     return result

# RETURN прекращает выполнение ф-ии в момент когда тело ф-ии до него дошло

# print(only_even([2,4,6]))
# print(only_even([2,4,6,3]))
# print(only_even([int(input()) for i in range(5)]))

# упрощенная версия без фрага result
# def only_even(numbers):
#     for x in numbers:
#         if x % 2 != 0:
#             return False
#     return True

# print(only_even([2,4,6]))
# print(only_even([2,4,6,3]))

# ОБЛАСТЬ ВИДИМОСТИ (ОВ) (локальная, глобальная)
# Локальные перем. - доступны только внутри этой функции, если обртиться снаружи, то = ошибка
# Глобальные перемен. - можно обращаться из любого места, и вутри ф-ии

# def only_even(numbers):
#     for i, x in enumerate(numbers):
#         if x % 2 != 0:
#             return False, i
#     return True

# print(only_even([2,4,6]))
# print(only_even([2,4,6,5]))
# print(numbers) # будет ошибка, поскольку переменная локальная

# def check_password(pwd): # локальная область видимости
#     return pwd == password # локальная область видимости
# password = 'Python' # глобальная область видимости
# print(check_password('Python')) # глобальная область видимости

# как безопасно изменять переменные, переданные в функцию, 
# можно ли изменить переменную из глобальной ОВ внутри ф-ии:
# зависит от типа данных этой переменной, 
# если изменяемый тип (список), то изменения происходят напрямую
# если неизменяемый тип (число, строка), 
# то попытка изменить создаёт локальную копию с тем же именем

# пример с изменяемым типом

# def list_modify():
#     del sample[-1]
# sample = [1, 2, 3]
# list_modify()
# print(sample)

# пример с неизменяемым типом

# def list_modify(): # нет переменной в скобках
#     sample = [4, 5, 6] # создалась локальная копия с тем же именем
# sample = [1, 2, 3]
# list_modify()
# print(sample) 
# # ничего не изменилось, осталось значение глобальной переменной, 
# # присвоить новое значение нельзя

# def list_mod_1(list_arg): # есть переменная в скобках
#     list_arg = [1, 2, 3, 4]

# def list_mod_2(list_arg): # есть переменная в скобках
#     list_arg += [4]

# sample_1 = [1,2,3]
# sample_2 = [1,2,3]

# list_mod_1(sample_1)
# list_mod_2(sample_2)
# print(sample_1)  # [1, 2, 3]
# print(sample_2)  # [1, 2, 3, 4]


# если нужно изменить глобальную переменную внутри функции, 
# то используется ключевое слово global - 
# использовать СУПЕР-ОСТОРОЖНО, т.к. код становится непредсказуемым
# любое изменение может произойти в любой части программы, что затрудняет отладку

# def inc():
#     global x
#     x += 1
#     print(f'Количество вызовов функции равно {x}')
# x = 0
# inc()
# inc()
# inc()
# inc() 


# ПОЗИЦИОННЫЕ аргументы - арг. передаются строго в том порядке, 
# в кот. заданы в определении ф-ии

# ИМЕНОВАННЫЕ аргументы - позволяют не соблюдать порядок

# позиционные

# def final_price(price, discount):
#     return price - price * discount / 100
# print(final_price(1000, 5))  

# можно установить значения ПО УМОЛЧАНИЮ
# значение присваивается один раз в момент объявления(появления во вне) ф-ии,
# если объект изменяемого типа(список), то может привести к неожиданному поведению

# def final_price(price, discount=1):
#     return price - price * discount / 100
# print(final_price(1000))  

# если объект изменяемого типа(список), то может привести к неожиданному поведению
# пример

# def add_value(x, list_arg=[]): # по умолчанию пустой список(list_arg=[]),
# # если не указывать этот объект в момент объявления ф-ии, 
# # то присваивается по умолчанию первое полученное значение (в примере ниже это "5")
#     list_arg += [x]
#     return list_arg
# print(add_value(5)) # [5]  - в пустой список добавился ноль
# print(add_value(0, [1,2,3])) # [1, 2, 3, 0] - ожидаемо в список добавлены те значения, 
# # кот. внесены как аргументы
# print(add_value(1)) # [5, 1] - добавлено число 5 из первого print, 
# # т.к. значение по умолчанию объявляется один раз в момент объявления ф-ии

# # чтобы избежать ошибки выше - нужно в ф-ии по умолчанию передать список = NONE
# def add_value(x, list_arg = None):
#     if list_arg is None:
#         list_arg = []
#     list_arg += [x]
#     return list_arg
# print(add_value(5)) # [5]  
# print(add_value(0, [1,2,3])) # [1, 2, 3, 0] 
# print(add_value(1)) # [1]

# # именованные

# def final_price(price, discount=1):
#     return price - price * discount / 100
# print(final_price(1000, discount=5))  
# print(final_price(discount=6, price=1000))  

# Ф-ИЯ может принимать произвольное кол-во арг. (args, kwargs),
# когда заранее неизвестно, сколько арг. нужно передать

# позиционные арг. args или * перед именем параметра, 
# внутри ф-ии такой параметр становится кортежем, содержащим все переданные значения
# пример такой ф-ии - print, она принимает произвольное кол-во аргументов

# def final_price(*prices, discount=1): # * то же что и args (*args, discount=1)
#     return [price - price * discount / 100 for price in prices] # обратить внимание,
#     # что разные наименования арг. (price, prices)
# print(final_price(1000, 500, 200, 50, 800, discount=5))  


# именованные арг. kwargs(keyword argument) или **, арг. представляет собой словарь,
# в кот. ключ - имена переданных арг., а значения - это их соответствующие значения

# def final_price(*prices, discount=1, ** kwargs):
#     low = kwargs.get('price_low', min(prices)) # метод get для словаря,возвращает значение ключа,
#                                                # если его нет,то возвращает альтернативу
#     high = kwargs.get('price_high', max(prices))
#     return [price - price * discount / 100 for price in prices if low <= price <= high]
# print(final_price(1000, 500, 200, 50, 800, discount=5)) # [950.0, 475.0, 190.0, 47.5, 760.0]
# print(final_price(1000, 500, 200, 50, 800, discount=5, price_low=200)) # [950.0, 475.0, 190.0, 760.0]
# print(final_price(1000, 500, 200, 50, 800, discount=5, price_high=500)) # [475.0, 190.0, 47.5]
# print(final_price(1000, 500, 200, 50, 800, discount=5, price_low=200, price_high=350)) # [190.0]