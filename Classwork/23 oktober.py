# ПРОЦЕДУРНОЕ ПРОГРАММИРОВАНИЕ

# # color, gazolin umenshartsa, probeg, zapusk, ostanovka

# def create_car(color,consumption, tank_volume, mileage=0):
#     return {
#         'color': color,
#         'consumption': consumption,
#         'reserve': tank_volume,
#         'mileage': mileage,
#         'engine_on': False
#     }

# def start_engine(car):
#     if car['reserve'] > 0 and not car['engine_on']:
#         car['engine_on'] = True
#         return 'Двигатель запущен'
#     return 'Двигатель уже запущен!'

# def stop_engine(car):
#     if car['engine_on']:
#         car['engine_on'] = False
#         return 'Двигатель остановлен'
#     return 'Двигатель уже был остановлен'

# def drive(car, distance):
#     if not car['engine_on']:
#         return 'Двигатель не заведен'
#     if car['reserve'] / car['consumption'] * 100 < distance:
#         return 'Малый запас топлива'
#     car['mileage'] += distance
#     car['reserve'] -= distance / 100 * car['consumption']
#     return f'Проехали {distance} км. Остаток топлива: {car['reserve']} л.'

# def refuel(car):
#     car['reserve'] = car['tank_volume']

# def get_mileage(car):
#     return f'Пробег {car['mileage']} км.'

# def get_reserve(car):
#     return f'Запас топлива {car['reserve']} л.'

# car_1 = create_car(color='black', consumption=10, tank_volume=55)

# print(start_engine(car_1))
# print(drive(car_1, 100))
# print(drive(car_1, 100))
# print(drive(car_1, 100))
# print(drive(car_1, 300))
# print(get_mileage(car_1))
# print(get_reserve(car_1))
# print(start_engine(car_1))
# print(drive(car_1, 100))


# ОБЪЕКТНО-ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ (ООП)
# описание всех явлений, кот. окружают человека.
# объединять данные и связанные с ними действия
# в единую структуру, кот. называется КЛАСС.
# КЛАСС - шаблон(описание), по кот. создаются объекты,
# задаются св-ва, характ.(АТРИБУТЫ-цвет,пробег,объем бака) и 
# действия (МЕТОДЫ-поехать,завести,заглушить)

# ОБЪЕКТ(числа,строки,функ-ии,списки,модули) - 
# конкретный экземпляр класса,кот.обладает своими атрибутами, 
# может выполнять описанные в нем действия 

# class <ИмяКласса>: 
#     <описание класса>
# по стандарту PEP8 имя записывается в CamelCase 
# CarElectric UserProfil

# атрибуты:
# <имя_объекта>.<имя_атрибута> = <значение>
# car_1.color = 'black'

# метод, SELF - ссылка на конкретный объект,для кот. вызывается метод,
# не вызывается явно, а автом. подставляется,
# с пом. self метод может обращаться к др. методам и атрибутам объекта,
# методу нужно дать взглянуть на самого себя, чтобы понять св-ва,
# помогает объекту понять свои уникальные атрибуты

# def start_engine(self):
    #  ....

# <имя_объекта> = <ИмяКласса> (<аргументы метода __init__()>)
# car_1 = Car(color='black', consumpion=10, tank_volume=55)

# метод __init__ -автомат. вызывается при созд. нового объекта,
# не возвращает, а хранит настройки объекта,
# и отвечает за начальн. инициализацию его атрибутов

# ИНКАПСУЛЯЦИЯ - внутр. состояние объекта скрыто от внеш. кода,
# доступно ТОЛЬКО через МЕТОДЫ,
# помогает избежать случайных ошибок при прямом изменении данных,
# сохранить корректность логики внутри класса,
# упростить отладку и поддержку программы

# class Car:
#     pass

#     def __init__(self, color, consumption, tank_volume, mileage=0):
#         self.color = color
#         self.consumption = consumption
#         self.tank_volume = tank_volume
#         self.reserve = tank_volume
#         self.mileage = mileage
#         self.engine_on = False

#     def start_engine(self):
#         if self.reserve > 0 and not self.engine_on:
#             self.engine_on = True
#             return 'Двигатель запущен'
#         return 'Двигатель уже запущен!'

#     def stop_engine(self):
#         if self.engine_on:
#             self.engine_on = False
#             return 'Двигатель остановлен'
#         return 'Двигатель уже был остановлен'

#     def drive(self, distance):
#         if not self.engine_on:
#             return 'Двигатель не заведен'
#         if self.reserve / self.consumption * 100 < distance:
#             return 'Малый запас топлива'
#         self.mileage += distance
#         self.reserve -= distance / 100 * self.consumption
#         return f'Проехали {distance} км. Остаток топлива: {self.reserve} л.'

#     def refuel(self):
#         self.reserve = self.tank_volume

#     def get_mileage(self):
#         return self.mileage

#     def get_reserve(self):
#         return self.reserve 

#     def get_consumption(self):
#         return self.consumption

# car_1 = Car(color='black', consumption=10, tank_volume=55)
# print(car_1.start_engine())
# print(car_1.drive(100))
# print(car_1.drive(100))
# print(car_1.drive(100))
# print(car_1.drive(300))
# print(f'Пробег {car_1.get_mileage()} км.')
# print(f'Запас топлива {car_1.get_reserve()} л.')
# print(car_1.stop_engine())
# print(car_1.drive(100))

# # что будет если напрямую изменить атрибуты (будут недостоверные данные):

# car_1.mileage = 1000

# print(f'Пробег {car_1.get_mileage()} км.') 
# # Пробег 1000 км. НО двигатель не запускался,топливо не расходовалось,
# # ДАННЫЕ НЕДОСТОВЕРНЫ

# print(f'Запас топлива {car_1.get_reserve()} л.') 
# # Запас топлива 55 л.


# # ПОЛИМОРФИЗМ - один и тот же интерфейс раюотает с объектами разных типов:
# # и с Car и с ElectricCar,
# # должны быть методы с одинаковыми именами и сигнатурами
# # DuckTypisation - утиная типизация: 
# # если объект умеет делать всё,что от него ожидается, то можно с ним работать, не проверяя класс
# # пример: def range_reserve(car)


# class CarElectric:
#     pass

#     def __init__(self, color, consumption, bat_capacity, mileage=0):
#         self.color = color
#         self.consumption = consumption
#         self.bat_capacity = bat_capacity
#         self.reserve = bat_capacity
#         self.mileage = mileage
#         self.engine_on = False

#     def start_engine(self):
#         if self.reserve > 0 and not self.engine_on:
#             self.engine_on = True
#             return 'Двигатель запущен'
#         return 'Двигатель уже запущен!'

#     def stop_engine(self):
#         if self.engine_on:
#             self.engine_on = False
#             return 'Двигатель остановлен'
#         return 'Двигатель уже был остановлен'

#     def drive(self, distance):
#         if not self.engine_on:
#             return 'Двигатель не заведен'
#         if self.reserve / self.consumption * 100 < distance:
#             return 'Малый запас заряда батареи'
#         self.mileage += distance
#         self.reserve -= distance / 100 * self.consumption
#         return f'Проехали {distance} км. Остаток заряда батареи: {self.reserve} кВт/ч.'

#     def recharge(self):
#         self.reserve = self.bat_capacity

#     def get_mileage(self):
#         return self.mileage

#     def get_reserve(self):
#         return self.reserve 
    
#     def get_consumption(self):
#         return self.consumption
    
# def range_reserve(car):
#     return car.get_reserve() / car.get_consumption() *100

# car_1 = Car(color='black', consumption=10, tank_volume=55)
# car_2 = CarElectric(color='black', consumption=15, bat_capacity=90)

# print(f'Запас хода: {range_reserve(car_1)} км.')
# print(f'Запас хода: {range_reserve(car_2)} км.')



# # НАСЛЕДОВАНИЕ КЛАССОВ
# # Пример с ракетами

# # import math

# from math import sqrt

# class Rocket:

#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y

#     def move_rocket(self, x_increment=0, y_increment=1):
#         self.x += x_increment
#         self.y += y_increment

#     def get_distance(self, other_rocket):
#         distance = sqrt((self.x - other_rocket.x)**2 + (self.y - other_rocket.y)**2)
#         return distance
    
# rocket_0 = Rocket()
# rocket_1 = Rocket(10, 5) 

# distance = rocket_0.get_distance(rocket_1)
# print(f'Ракеты на расстоянии {distance}')

    

# # наследование позволяет создавать стабильный 
# # и многократно используемый код
# # новый класс создается на основе предыдущего,наследуя атрибуты и поведение
# # новый класс может переопределить старые и создать новые атрибуты,поведение
# # исходный класс - РОДИТЕЛЬСКИЙ (parent class или super class), 
# # - ему не доступны дочерние атрибуты
# # новый класс - ДОЧЕРНИЙ (child class или sub class), 
# # - может переопределить поведение родит.:метод, кот. есть в родит.,будут использовать новое поведение


# class Shuttle(Rocket):

#     def __init__(self, x=0, y=0, flights_completed=0):
#         super().__init__(x, y) # альтернатива: Rocket.__init(self, x, y)
#         # функция SUPER наследует все параметры из родит.класса Rocket
#         self.flights_completed = flights_completed

# shuttle = Shuttle(10, 0, 3)
# # print(shuttle)

# from random import randint 
# # randint генерирует случайные целые числа
# # print(randint(0, 100))

# shuttles = []
# for i in range(3):
#     x = randint(0, 100)
#     y = randint(0, 100)
#     flights_completed = randint(0, 10)
#     shuttles.append(Shuttle(x,y,flights_completed))

# rockets = []
# for i in range(3):
#     x = randint(0, 100)
#     y = randint(0, 100)
#     rockets.append(Rocket(x,y))

# for index, shuttle in enumerate(shuttles):
#     print(f'Шаттл {index} выполнил {shuttle.flights_completed} полетов')

# first_shuttle = shuttles[0]
# for index, shuttle in enumerate(shuttles):
#     distance = first_shuttle.get_distance(shuttle)
#     print(f'Шаттл номер 1 на расстоянии в {distance} от шаттла номер {index}')


