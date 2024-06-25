from model import *
from controller.dish_controller import DishController
from view.main_view import MainView

def main():
    print("pyMenu 1.0")
    dish_controller = DishController()
    #dish_controller.load_dish_collection_from_file()
    MainView(dish_controller)
    dish_controller.show_dish_collection()
    
# Punto de entrada de la aplicación    
if __name__ == "__main__":
    main()
    