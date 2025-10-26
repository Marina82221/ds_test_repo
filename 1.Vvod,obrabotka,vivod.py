# # 1. прогноз продаж
# plan = float(input())
# pribil = plan*0.23
# print(f'{pribil:,.2f}')

# # 14. Сложный процент

# p = float(input(f'сколько внесли в начале: '))
# r = float(input(f'какая годовая ставка в %: '))
# n = float(input(f'частота начислений в год (1 раз в месяц = 12, один раз в квартал = 4): '))
# t = float(input(f'количество лет: '))

# dohod = p*(1 + ((r/100)/n))**t
# print(f'{dohod: .2f}')

# # 18. Условные операторы - Селектор ресторанов

# veget = input(f'вы вегетарианец?'
#               f'да/нет ').lower()
# vegan = input(f'вы веган?' 
#               f'да/нет ').lower()
# no_gluten = input(f'вы безглютенщик?' 
#               f'да/нет ').lower()




# if veget == 'да'and vegan == 'нет' and no_gluten == 'нет':
#     print('Пицца', 'Шеф', 'За углом', 'Итальянский')
# elif veget == 'да' and vegan == 'да' and no_gluten == 'нет':
#     print('За углом', 'Шеф')
# elif veget == 'да' and vegan == 'да' and no_gluten == 'да':
#     print('За углом', 'Шеф')
# elif veget == 'нет' and vegan == 'да' and no_gluten == 'да':
#     print('За углом', 'Шеф')
# elif veget == 'нет'and vegan == 'да' and no_gluten == 'нет': 
#     print('За углом', 'Шеф')
# elif veget == 'нет'and vegan == 'нет' and no_gluten == 'да':
#     print('Пицца', 'За углом', 'Шеф')
# elif veget == 'да' and vegan == 'нет' and no_gluten == 'да':
#     print('Пицца','За углом', 'Шеф')
# else:
#     print('Джо', 'Пицца', 'За углом', 'Итальянский', 'Шеф')

# # другой вариант
# vet = input('Будет ли на ужине вегетарианец?: ')
# van = input('Будет ли на ужене веганец?:  ')
# glu = input('Будет ли на ужене приверженец глютеновой диеты?: ')
# a1 = 'Изысканные гамбургеры'
# a2 = 'Центральная пиццерия'
# a3 = 'Кафе за углом'
# a4 = 'Бюда итальянской мамы'
# a5 = 'Кухня шеф-повара'
# if vet == 'нет' and van == 'нет' and glu == 'нет':
#     print(a1,a2,a3,a4,a5,sep='\n')
# elif vet == 'да' and van == 'да' and glu == 'да':
#     print(a3,a5,sep='\n')
# elif vet == 'да' and van == 'нет' and glu == 'нет':
#     print(a2,a3,a4,a5,sep='\n')
# elif vet == 'да' and van == 'нет' or van =='да' and glu == 'да':
#     print(a2,a3,a5,sep='\n')

