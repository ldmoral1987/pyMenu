from tkinter import *

def archivo_nuevo_presionado():
    print("¡Has presionado para crear un nuevo archivo!")

def center_window(window, width=300, height=200):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    
def configure_menu(window):
    barra_menus = Menu()
    menu_archivo = Menu(barra_menus, tearoff=False)
    menu_archivo.add_command(
        label="Nuevo",
        accelerator="Ctrl+N",
        command=archivo_nuevo_presionado
    )
    barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
    window.config(menu=barra_menus)
    
window=Tk()
# add widgets here

window.title('pyMenu 1.0')
configure_menu(window)
center_window(window, 800, 600)
window.mainloop()
