from tkinter import *
from controller.dish_controller import DishController
from model.dish import Dish

class NewDishView(Frame):
    def __init__(self, dish_controller: DishController):
        # Se guarda la referencia al controlador
        self.dish_controller = dish_controller
        
        self.window=Tk()
        self.window.title('pyMenu 1.0 --- Nuevo plato')
        self.center_window(self.window, 400, 300)
        self.configure_widgets(self.window)
        self.window.mainloop()

    def center_window(self, window, width=300, height=200):
        # get screen width and height
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
    def configure_widgets(self, window):
        # Se configura el ancho del gird
        window.grid_columnconfigure(tuple(range(4)), weight=1)
        
        # Se configura el título
        info = Label(window, text="Nuevo plato", font=("Helvetica", 16, "bold"))
        info.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Se configuran los widgets de los atributos de la clase Dish
        Label(window, text="Nombre").grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self.name = Entry(window, bd=3)
        self.name.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        Label(window, text="Descripción").grid(row=2, column=0, padx=5, pady=5, sticky=E)
        self.description = Entry(window, bd=3)
        self.description.grid(row=2, column=1, columnspan=3, padx=5, pady=5)        
        
        Label(window, text="Ingredientes").grid(row=3, column=0, padx=5, pady=5, sticky=E)
        self.ingredients = Entry(window, bd=3)
        self.ingredients.grid(row=3, column=1, columnspan=3, padx=5, pady=5)
        
        Label(window, text="¿Almuerzo?").grid(row=4, column=0, padx=5, pady=5, sticky=E)
        self.is_lunch = IntVar()
        isLunch = Checkbutton(window, bd=3, variable=self.is_lunch)
        isLunch.grid(row=4, column=1, columnspan=3, padx=5, pady=5)
        
        Label(window, text="¿Cena?").grid(row=5, column=0, padx=5, pady=5, sticky=E)
        self.is_super = IntVar()
        isSuper = Checkbutton(window, bd=3, variable=self.is_super)
        isSuper.grid(row=5, column=1, columnspan=3, padx=5, pady=5)     
        
        action = Button(window, bd=3, text="Aceptar", command=self.add_dish)
        action.grid(row=6, column=0, columnspan=4, padx=5, pady=5)
        
    def add_dish(self):
        dish = Dish(self.name.get(), self.description.get(), self.ingredients.get(), self.is_lunch.get(), self.is_super.get())
        self.dish_controller.add_dish(dish)
        self.window.destroy()
    