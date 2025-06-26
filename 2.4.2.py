class Drink:
    def __init__(self, name, alcohol_content, ingredients, price):
        self.name = name
        self.alcohol_content = alcohol_content 
        self.ingredients = ingredients  
        self.price = price

    def display_info(self):
        print(f"Название: {self.name}")
        print(f"Крепость: {self.alcohol_content}%")
        print(f"Ингредиенты: {', '.join(self.ingredients)}")
        print(f"Цена: {self.price}")

class Cocktail(Drink): 
    def __init__(self, name, ingredients, price):
        alcohol_content = 0 
        super().__init__(name, alcohol_content, ingredients, price)

drinks = []

def add_drink():
    name = input("Название напитка: ")
    alcohol_content = float(input("Крепость (в %): "))
    ingredients = input("Ингредиенты (через запятую): ").split(",")
    price = float(input("Цена: "))
    drink = Drink(name, alcohol_content, ingredients, price)
    drinks.append(drink)
    print("Напиток добавлен!")

def sell_drink(drink_name):
    for drink in drinks:
        if drink.name == drink_name:
            print(f"Продан напиток: {drink_name}")
            
            return
    print("Такой напиток не найден.")

def replenish_stock(drink_name, quantity):
    print(f"Пополнены запасы напитка {drink_name} на {quantity} единиц")

add_drink()
