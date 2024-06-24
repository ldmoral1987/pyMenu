class Dish():
    """Clase Dish, representa una comida de la planificación (almuerzo o cena)."""
    def __init__(self, name: str, description: str, ingredients: list):
        """Constructor de la clase"""
        self.name = name
        self.description = description
        self.ingredients = ingredients
        
    def __str__(self):
        """Serializa la comida

        Returns:
            str: Serialización del objeto Dish
        """
        return f"{self.name}"
        