# 1. Срезы строки

# OLD
# text = "Питон — это круто!"
# print(text[:6])
# print(text[:-2:])
# print(text[::-1])
# print(text[::2])

# # NEW
# def slice(text):
#     print(text[:6])
#     print(text[:-2])
#     print(text[::-1])
#     print(text[::2])

# slice("Питон — это круто!")


# 2. Фильтрация списка по индексу

# # OLD
# numbers = [10, 25, 30, 45, 50, 65, 70]
# new_numbers = numbers[::2]
# print(new_numbers)

# # NEW
# def only_even(numbers):
#     new_numbers = numbers[::2]
#     print(new_numbers)

# only_even([10, 25, 30, 45, 50, 65, 70])

# 3. Замена элементов списка


# # OLD
# shopping = ["молоко", "хлеб", "сыр", "яблоки"]
# shopping[shopping.index("хлеб")] = "батон"
# shopping.remove("сыр")
# shopping.append("йогурт")
# print(shopping)


# # NEW_1

# def change_shopping(shopping):
#     shopping[shopping.index("хлеб")] = "батон"
#     shopping.remove("сыр")
#     shopping.append("йогурт")
    
#     print(shopping)

# change_shopping(["молоко", "хлеб", "сыр", "яблоки"])


# # NEW_2

# def change_shopping(shopping, old_shop_chang, new_shop_chang, shop_remove, shop_app):
#     shopping[shopping.index(old_shop_chang)] = new_shop_chang
#     shopping.remove(shop_remove)
#     shopping.append(shop_app)
    
#     print(shopping)


# old_shop_chang = input('Заменить в списке: ')
# new_shop_chang = input(f'Заменить {old_shop_chang} в списке на: ')
# shop_remove = input('Удалить из списка: ')
# shop_app = input('Добавить в список: ')

# shopping = ["молоко", "хлеб", "сыр", "яблоки"]

# change_shopping(shopping, old_shop_chang, new_shop_chang, shop_remove, shop_app)

# 4. Объединение списков

# # OLD 
# a = [1, 3, 5]
# b = [2, 4, 6]
# a.extend(b)
# a.reverse()

# print(a, len(a))

# # NEW

# def unite(a, b):
#     a.extend(b)
#     a.reverse()
#     print(a, len(a))

# unite([1, 3, 5], [2, 4, 6])


# 5. Удаление всех повторов


# # OLD
# data = [1, 2, 2, 3, 4, 4, 5, 1]
# s_data = set(data)
# print(s_data)


# # NEW

# def del_repeat(s):
#     s = set(s)
#     print(s)


# del_repeat([1, 2, 2, 3, 4, 4, 5, 1])


# 6. Работа со словарём стран

# # OLD
# countries = {
#     "Россия": "Москва",
#     "Италия": "Рим",
#     "Испания": "Мадрид"
# }
# countries["Германия"] = "Берлин"
# countries["Испания"] = "Барселона"
# for k, v in countries.items():
#     print(f'Столица {v} находится в стране {k}')


# # NEW
# countries = {
#     "Россия": "Москва",
#     "Италия": "Рим",
#     "Испания": "Мадрид"
# }

# def dictionary(countries):
#     countries["Германия"] = "Берлин"
#     countries["Испания"] = "Барселона"
#     for country, city in countries.items():
#         print(f'Столица {city} находится в стране {country}')


# dictionary(countries)


# 7. Подсчёт букв


# # OLD
# word = "программирование"
# vowels = {'а', 'о', 'у', 'э', 'и', 'ы', 'е', 'ё', 'ю', 'я'}
# s_word = set(word)

# print(f'Уникальных букв в слове "Программирование" =  {len(s_word)}')
# print(s_word & vowels)

# # NEW

# vowels = {'а', 'о', 'у', 'э', 'и', 'ы', 'е', 'ё', 'ю', 'я'}
# def how_many_vowels(word):
#     word = set(word)
#     print(f'Уникальных букв в слове "Программирование" =  {len(word)}')
#     print(word & vowels)

# how_many_vowels("программирование")

# 8. Обратный словарь


# # OLD

# countries_and_capitals = {"Россия": "Москва", "Франция": "Париж", "Япония": "Токио"}
# new_countries_and_capitals = {}

# for k, v in countries_and_capitals.items():
#     new_countries_and_capitals[v] = k
   
# print(new_countries_and_capitals)


# # NEW

# def another_dict(dict):
#     new_dict = {}
#     for k, v in dict.items():
#         new_dict[v] = k
#     print(new_dict)

# another_dict({"Россия": "Москва", "Франция": "Париж", "Япония": "Токио"})

# 9. Список фильмов_

# # OLD

# films = ['Волк с Уолл-стрит', 'Платформа', 'Дневник памяти', 'Великая красота', 'Меланхолия']

# films.sort()
# films.insert(0, 'Интерстеллар')
# films.pop()

# print(films)


# # NEW

# def changes_films(films, new_film):
#     films.sort()
#     films.insert(0, new_film)
#     films.pop()

#     print(films)

# changes_films(['Волк с Уолл-стрит', 'Платформа', 'Дневник памяти', 'Великая красота', 'Меланхолия'], 'Интерстеллар')

# 10. Анализ числового списка

# # OLD

# nums = [15, 2, 30, 4, 50, 6, 75, 8]
# new_nums = []

# for i in range(len(nums)):
#     if nums[i] < (sum(nums) / len(nums)):
#         new_nums.append(nums[i])
# new_nums.sort()

# print(f'Минимальное число в списке = {min(nums)}')
# print(f'Максимальное число в списке = {max(nums)}')
# print(f'Среднее арифметическое = {sum(nums) / len(nums)}')
# print(f'Числа меньше среднего арифметического по возрастанию = {new_nums}')


# # NEW 

# def analiz_num(nums):
#     new_nums = [nums[i] for i in range(len(nums)) if nums[i] < (sum(nums) / len(nums))]
#     new_nums.sort()

#     print(f'Минимальное число в списке = {min(nums)}')
#     print(f'Максимальное число в списке = {max(nums)}')
#     print(f'Среднее арифметическое = {sum(nums) / len(nums)}')
#     print(f'Числа меньше среднего арифметического по возрастанию = {new_nums}')

# analiz_num([15, 2, 30, 4, 50, 6, 75, 8])


