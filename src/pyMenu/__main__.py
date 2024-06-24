from model.dish import Dish
from controller.dish_controller import DishController

def main():
    print("pyMenu 1.0")
    d1 = Dish("aaa", "bbb", "ccc") 
    print(d1)
    dc = DishController()
    
if __name__ == "__main__":
    main()
    