import tkinter as tk
from controller.dish_controller import DishController
from view.new_dish_view import NewDishView

class MainView(tk.Frame):
    dish_controller: DishController
    
    def __init__(self, dish_controller: DishController):
        self.dish_controller = dish_controller
        window=tk.Tk()
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
    
    def configure_menu(self, window):
        barra_menus = tk.Menu()
        menu_archivo = tk.Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(
            label="Nuevo plato",
            accelerator="Ctrl+N",
            command=self.archivo_nuevo_presionado
        )
        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
        window.config(menu=barra_menus)
