from model.dish import Dish
from model.day import Day

class DishController():
    menu = list()
    def __init__(self):
        #d1 = Dish("Tortilla", "Tortilla", "Patata, Huevos, Aceite")
        #print(d1)
        pass
    
    def add_dish(self, d: Dish):
        # Se añade el plato al menú
        self.menu.append(d)
    
    def search_dish(self, dish: str):
        pass
    
    def delete_dish(self, dish: str):
        pass
    
    def show_dish_collection(self):
        for dish in self.menu:
            print(dish)
    
    def load_file(self, filename):
        pass

    def load_test_data(self):
        self.add_dish(Dish("Tortilla de patatas", "Tortilla de patatas", "Patatas, Aceite, Huevo, Sal"))
        self.add_dish(Dish("Salmorejo", "Salmorejo", "Tomate, Ajo, Aceite, Sal"))
        self.add_dish(Dish("Ensalada de pimientos", "Ensalada de pimientos", "Pimientos, Aceite, Atún"))

        

