from model.dish import Dish
from model.day import Day
from controller.dish_controller import DishController
from view.main_view import MainView

def main():
    print("pyMenu 1.0")
    #lunch = Dish("Tortilla", "bbb", "ccc") 
    #supper = Dish("Atun", "bbb", "ccc") 
    #day = Day(lunch, supper)
    #print(day)
    dish_controller = DishController()
    dish_controller.load_test_data()
    dish_controller.show_dish_collection()
    
    MainView()
    
# Punto de entrada de la aplicación    
if __name__ == "__main__":
    main()
    