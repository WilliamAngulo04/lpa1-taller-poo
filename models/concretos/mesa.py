"""
Clase concreta Mesa.
Implementa un mueble de superficie para comer o trabajar.
"""

from ..categorias.superficies import Superficies


class Mesa(Superficies):
    """
    Clase concreta que representa una mesa.
    
    Una mesa es una superficie horizontal para comer, trabajar, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Superficies
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos de la mesa
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str, capacidad_personas: int, tiene_cajones: bool = False):
        """
        Constructor de la mesa.
        
        Args:
            forma: Forma de la mesa (rectangular, redonda, etc.)
            capacidad_personas: Número de personas que pueden usar la mesa
            tiene_cajones: Si la mesa tiene cajones
            Otros argumentos heredados de Superficies
        """
        super().__init__(nombre, material, color, precio_base, forma=forma,
                        capacidad_personas=capacidad_personas, tiene_cajones=tiene_cajones)
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para mesas.
        
        Returns:
            float: Precio final de la mesa
        """
        precio_final = self.precio_base
        
        # Factor por capacidad de personas
        precio_final *= (1 + (self.capacidad_personas - 1) * 0.1)
        
        # Factor por material
        if self.material.lower() == "madera":
            precio_final *= 1.2
        elif self.material.lower() == "vidrio":
            precio_final *= 1.3
        elif self.material.lower() == "metal":
            precio_final *= 1.1
        
        # Factor por forma
        if self.forma.lower() == "redonda":
            precio_final *= 1.05
        
        # Cajones aumentan el precio
        if self.tiene_cajones:
            precio_final += 50.0
        
        return round(precio_final, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica de la mesa.
        
        Returns:
            str: Descripción completa de la mesa
        """
        descripcion = f"Mesa '{self.nombre}' de {self.material} en color {self.color}."
        descripcion += f" Forma: {self.forma}, capacidad para {self.capacidad_personas} personas."
        if self.tiene_cajones:
            descripcion += " Incluye cajones."
        return descripcion