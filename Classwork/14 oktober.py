#in
# text = input()
# if 'добр' in text:
#     print('есть слово')
# else:
#     print('нет слова')

# m = 12
# n = 19
# k = 25

# print(max(m,n,k))
# print(min(m,n,k))
# print(len('привет'))
# print(len(str(2 ** 3)))

# цикл

# saved_pwd = 'right'
# pwd = input('Введите свой пароль: ')

# while pwd != saved_pwd:
#     pwd = input('Введите свой пароль: ')
# print('Пароль верный')

# saved_pwd = 'right'

# while input('Введите свой пароль: ') != saved_pwd:
#     pass
# print('Пароль верный')

# range(n) - от 0 до n-1
# range(4) = 0,1,2,3

# range(k,n) - от k до n-1
# range(1,5) = 1,2,3,4

# range(k,n,s) - от k до n-1 с шагом s
# k - start
# n - stop
# s - step
# range(1,10,2) = 1,3,5,7,9

# n = int(input("Введите количество чисел: "))
# for i in range(n):
#     print(i)

# n = int(input("Введите количество чисел: "))
# for i in range(0,n,2):
#     print(i)

# n = int(input("Введите количество чисел: "))
# for i in range(n, -1, -1): # второе число - минус 1,потому что нужно до 0, 
# число -1 не входит в диапазон
#     print(i)

# Вложенные циклы

# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f'{i} x {j} = {j*i}')

# сумма элементов в таблице
# rows, cols = 3, 4
# for r in range(rows):
#     row_sum = 0
#     for c in range(cols):
#         value = r + c
#         row_sum += value # row_sum = row_sum + value
#         #print(value)
#     print(f'Сумма строки: {row_sum}')

# досрочное завершение цикла - break, использовать только там, где это необходимо, много раз не использовать

# saved_pwd = 'right'
# while True:
#     if input('Введите свой пароль: ') == saved_pwd:
#         print('Пароль принят')
#         break

# можно использовать флаги
# for i in range(1, 6):
#     for j in range(1, 6):
#         val = i * j
#         if val == 16:
#             print('Ого 16!')
#         print(f'{i} x {j} = {val}')

# flag = False
# for i in range(1, 6):
#     for j in range(1, 6):
#         val = i * j
#         if val == 12:
#             print('Ого 12!')
#             flag = True
#             break
#         print(f'{i} x {j} = {val}')
#     if flag == True: # можно записать 'if flag:', тк условный оператор по умолчанию равен True
#         break
        

# бесконечный цикл
# x =0
# while True:
#     print(x+1)

# оператор continue


# for i in range(1, 6):
#     for j in range(1, 6):
#         val = i * j
#         if i == j:
#             continue
#         print(f'{i} x {j} = {val}')

# esle в циклах используется, если цикл завершился ЕСТЕСТВЕННО
# для while - если нарушилось условие продолжения
# для for - когда закончились переменные в последовательности

# while input('Введите строку (СТОП для завершения)') != 'СТОП':
#     pass
# else:
#     print('Цикл завершен')

# # ":=" моржовый оператор
# # break - НЕЕСТЕСТВЕННОЕ завершение цикла, после него else НЕ выполняется
# while (text:= input('Введите строку (СТОП для завершения)')) != 'СТОП':
#     if text == 'ignore_else':
#         break
# else:
#     print('Цикл завершен')

# # условие для ограничения кол-ва вводов
# tries = 0
# while (text:= input('Введите строку (СТОП для завершения)')) != 'СТОП':
#     tries += 1
#     if tries == 3:
#         break
# else:
#     print('Цикл завершен')

# УПОРЯДОЧЕННЫЕ коллекции (последовательность символов, упорядоченная последовательность)

# text = input('Введите строку: ')
# i = int(input('Введите индекс символа: '))
# if i < len(text):
#     print(text[i])
# else:
#     print('Индекс не входит')

# text = input()
# # print(text[len(text)-1]) # сложная запись
# print(text[-1])            # простая запись
          
# пройти по коллекции можно: по индексам(for + range), по значениям, по индексам и значениям одновременно

# text = input()
# for i in range(len(text)):
#     print(text[i])

# # по индексам
# text = input()
# for i in range(len(text)):
#     print(text[i].upper())

# # по значениям
# text = input()
# for letter in text:
#     print(letter.upper())

# # по значениям и индексам - enumerate
# text = 'Marina'
# for i, letter in enumerate(text):
#     print(i, letter)


