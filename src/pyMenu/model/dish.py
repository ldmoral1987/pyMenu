class Dish():
    """Clase Dish, representa una comida de la planificación (almuerzo o cena)."""
    def __init__(self, name: str, description: str, ingredients: str, isLunch:bool, isSuper:bool):
        """Constructor de la clase"""
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.isLunch = isLunch
        self.isSuper = isSuper
        
    def __str__(self):
        """Serializa la comida

        Returns:
            str: Serialización del objeto Dish
        """
        return f"{self.name}"
        