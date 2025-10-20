# 1. Срезы строки


# text = "Питон — это круто!"
# print(text[:6])
# print(text[:-2:])
# print(text[::-1])
# print(text[::2])


# 2. Фильтрация списка по индексу

# numbers = [10, 25, 30, 45, 50, 65, 70]
# new_numbers = numbers[::2]
# print(new_numbers)

# 3. Замена элементов списка

# shopping = ["молоко", "хлеб", "сыр", "яблоки"]
# shopping[shopping.index("хлеб")] = "батон"
# shopping.remove("сыр")
# shopping.append("йогурт")
# print(shopping)

# 4. Объединение списков

# a = [1, 3, 5]
# b = [2, 4, 6]
# a.extend(b)
# a.reverse()

# print(a, len(a))

# 5. Удаление всех повторов

# data = [1, 2, 2, 3, 4, 4, 5, 1]
# s_data = set(data)
# print(s_data)

# 6. Работа со словарём стран

# countries = {
#     "Россия": "Москва",
#     "Италия": "Рим",
#     "Испания": "Мадрид"
# }
# countries["Германия"] = "Берлин"
# countries["Испания"] = "Барселона"
# for k, v in countries.items():
#     print(f'Столица {v} находится в стране {k}')

# 7. Подсчёт букв

# word = "программирование"
# vowels = {'а', 'о', 'у', 'э', 'и', 'ы', 'е', 'ё', 'ю', 'я'}
# s_word = set(word)

# print(f'Уникальных букв в слове "Программирование" =  {len(s_word)}')
# print(s_word & vowels)

# 8. Обратный словарь

# countries_and_capitals = {"Россия": "Москва", "Франция": "Париж", "Япония": "Токио"}
# new_countries_and_capitals = {}

# for k, v in countries_and_capitals.items():
#     new_countries_and_capitals[v] = k
   
# print(new_countries_and_capitals)

# 9. Список фильмов

# films = ['Волк с Уолл-стрит', 'Платформа', 'Дневник памяти', 'Великая красота', 'Меланхолия']

# films.sort()
# films.insert(0, 'Интерстеллар')
# films.pop()

# print(films)

# 10. Анализ числового списка

# nums = [15, 2, 30, 4, 50, 6, 75, 8]
# new_nums = []
# num_middle = 0
# for i in range(len(nums)):
#     num_middle += nums[i]
# num_middle /= len(nums)

# for i in range(len(nums)):
#     if nums[i] < num_middle:
#         new_nums.append(nums[i])
# new_nums.sort()

# print(f'Минимальное число в списке = {min(nums)}')
# print(f'Максимальное число в списке = {max(nums)}')
# print(f'Среднее арифметическое = {num_middle}')
# print(f'Числа меньше среднего арифметического по возрастанию = {new_nums}')

# вариант Антона
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

