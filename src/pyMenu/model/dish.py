# Clase Plato, representa un plato de comida en la planificación
class Dish():
    def __init__(self, nombre, descripcion, ingredientes):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ingredientes = ingredientes
        
    def __str__(self):
        return f"{self.nombre}"
        