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
# for i in range(n, -1, -1): # второе число - минут 1,потому что нужно до 0, 
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

# досрочное завершение цикла - break

# saved_pwd = 'right'
# while True:
#     if input('Введите свой пароль: ') == saved_pwd:
#         print('Пароль принят')
#         break

# бесконечный цикл
# x =0
# while True:
#     print(x+1)

