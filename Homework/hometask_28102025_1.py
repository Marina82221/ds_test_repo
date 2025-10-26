class Drink:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume
     
    def __str__(self):
        return f'Напиток {self.name} с объемом {self.volume} мл.'

class HotDrink(Drink):
    def __init__(self, name, volume, temperature=75):
        super().__init__(name, volume)
        self.temperature = temperature
    
    def __str__(self):
        return f'Напиток {self.name} объемом {self.volume} мл. и температурой {self.temperature} °С'

class ColdDrink(Drink):
    def __init__(self, name, volume, ice_cubes=3):
        super().__init__(name, volume)
        self.ice_cubes = ice_cubes

    def display_info(self):
        return f'Напиток {self.name} объемом {self.volume} мл. и {self.ice_cubes} кубиками льда'
    
    def __str__(self):
        return f'Напиток {self.name} объемом {self.volume} мл. и {self.ice_cubes} кубиками льда'

class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def order_drink(self, drink):
       self.orders.append(drink) 
    
    def show_orders(self):
        for i, drink in enumerate(self.orders,1):
            print(f'Клиент {self.name} заказал(а): {i}. {str(drink)}')
    
class DrinkMenu:
    def __init__(self):
        self.drinks = []

    def add_drink(self, drink):
        self.drinks.append(drink)
        return self.drinks

    def show_all_drinks(self):
        for i, drink in enumerate(self.drinks,1):
            print(f'Меню: {i}. {str(drink)}')
    
mulled_wine = HotDrink(name='Глинтвейн', volume=250, temperature=55)
tea = HotDrink(name='Жасминовый чай', volume=200, temperature=65)
cappuccino = HotDrink(name='Капучино', volume=300, temperature=70)

juice = ColdDrink(name='Апельсиновый сок', volume=500, ice_cubes=4)
beer = ColdDrink(name='Балтика 10', volume=473, ice_cubes=4)
frappe = ColdDrink(name='Фраппе', volume=350)

menu = DrinkMenu()
menu.add_drink(mulled_wine) 
menu.add_drink(cappuccino) 
menu.add_drink(juice) 
menu.add_drink(frappe) 

menu.show_all_drinks()

customer = Customer("Марина")
customer.order_drink(mulled_wine)
customer.order_drink(frappe)

customer.show_orders()