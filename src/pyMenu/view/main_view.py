import PIL.Image, PIL.ImageTk
from tkinter import *
from controller.dish_controller import DishController
from view.new_dish_view import NewDishView

class MainView(Frame):
    dish_controller: DishController
    
    def __init__(self, dish_controller: DishController):
        self.dish_controller = dish_controller
        window=Tk()
        window.title('pyMenu 1.0')
        self.configure_menu(window)
        self.center_window(window, 800, 600)
        window.mainloop()
    
    def archivo_nuevo_presionado(self):
        NewDishView(self.dish_controller)

    def center_window(self, window, width=300, height=200):
        # get screen width and height
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    def p(self):
        print("You Clicked")
    
    def configure_menu(self, window):
        
        toolbar = Frame(window, background="lightgray")

        new_dish_img = PIL.ImageTk.PhotoImage(PIL.Image.open("res/food.png"))
        new_dish_button = Button(toolbar, image=new_dish_img, relief=FLAT,command=self.p)
        new_dish_button.image = new_dish_img
        new_dish_button.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
