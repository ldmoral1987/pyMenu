from model.dish import Dish
from model.day import Day
from tkinter import filedialog

class DishController():
    menu = list()
    def __init__(self):
        #d1 = Dish("Tortilla", "Tortilla", "Patata, Huevos, Aceite")
        #print(d1)
        pass
    
    def add_dish(self, d: Dish):
        # Se añade el plato al menú
        self.menu.append(d)
    
    def show_dish_collection(self):
        for dish in self.menu:
            print(dish)
    
    def load_dish_collection_from_file(self):
        file_path = filedialog.askopenfilename()
        f = open(file_path, "r")
        for x in f:
            print(x)
        

