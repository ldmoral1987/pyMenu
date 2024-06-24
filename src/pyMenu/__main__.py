from model.dish import Dish
from model.day import Day
from controller.dish_controller import DishController
from view.main_view import MainView
from view.new_dish_view import NewDishView

def main():
    print("pyMenu 1.0")
    #lunch = Dish("Tortilla", "bbb", "ccc") 
    #supper = Dish("Atun", "bbb", "ccc") 
    #day = Day(lunch, supper)
    #print(day)
    dish_controller = DishController()
    MainView(dish_controller)
    dish_controller.show_dish_collection()
    
# Punto de entrada de la aplicación    
if __name__ == "__main__":
    main()
    