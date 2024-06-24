from .dish import Dish

class Day():
    """Clase Day, representa un día de la planificación."""
    def __init__(self, lunch: Dish, supper: Dish):
        """Constructor de la clase"""
        self.lunch = lunch
        self.supper = supper
        
    def __str__(self):
        """Serializa el día

        Returns:
            str: Serialización del objeto Day
        """
        return f"A:{self.lunch}\nC:{self.supper}"     