# Проверка приветствия

# word = input('Введите слово: ')
# if "привет" in word:
#     print("И тебе привет!")
# elif "пока" in word:
#     print("Уже уходишь? 😢")
# else:
#     print("Ты молчалив сегодня...")

# Таблица степеней

# n = int(input('Введите конечное число n: '))
# for i in range(1, n + 1):
#     print(f'{i} ^ 2 = {i ** 2}, {i} ^ 3 = {i ** 3}')

# Секретное число

# nummer = 7
# my_nummer = int(input())
# while True:
#     if my_nummer == nummer:
#         print("Верно!")
#         break
#     elif my_nummer > nummer:
#         print("Много!")
#         my_nummer = int(input())
#     elif my_nummer < nummer:
#         print("Мало!")
#         my_nummer = int(input())

# # вариант проще от Антона
# nummer = 7
# while True:
#     my_nummer = int(input('Введите число: '))
#     if my_nummer == nummer:
#         print("Верно!")
#         break
#     elif my_nummer > nummer:
#         print("Много!")
#     else:
#         print("Мало!")
 
    
# Гласные под прицелом

# word = input('Введите своё слово: ')
# vowels = "аеёиоуыэюя"
# for i, letter in enumerate(word):
#     for j in range(0,len(vowels)):
#         if word[i] == vowels[j]:
#             print(i, letter)

# вариант проще от Антона

# word = input('Введите своё слово: ')
# vowels = "аеёиоуыэюя"
# for i, letter in enumerate(word):
#     if letter in vowels:
#         print(i, letter)

# Квакушки на болоте, прыгают

# frog = 'Лягушка'
# for i in range(1,4):
#     for j in range(1,4):
#         if i == j:
#             continue
#         else:
#             print(f'{frog} {i} прыгает на кочку {j}')