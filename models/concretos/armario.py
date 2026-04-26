"""
Clase concreta Armario.
Implementa un mueble de almacenamiento con puertas.
"""

from ..categorias.almacenamiento import Almacenamiento


class Armario(Almacenamiento):
    """
    Clase concreta que representa un armario.
    
    Un armario es un mueble de almacenamiento con puertas.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Almacenamiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos del armario
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 num_puertas: int, num_cajones: int = 0, tiene_espejos: bool = False):
        """
        Constructor del armario.
        
        Args:
            num_puertas: Número de puertas
            num_cajones: Número de cajones
            tiene_espejos: Si tiene espejos
            Otros argumentos heredados de Almacenamiento
        """
        super().__init__(nombre, material, color, precio_base,
                        num_puertas=num_puertas, num_cajones=num_cajones,
                        tiene_espejos=tiene_espejos)
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para armarios.
        
        Returns:
            float: Precio final del armario
        """
        precio_final = self.precio_base
        
        # Factor por capacidad de almacenamiento
        capacidad = self.calcular_capacidad_almacenamiento()
        precio_final *= (1 + capacidad * 0.01)
        
        # Factor por material
        if self.material.lower() == "madera":
            precio_final *= 1.2
        
        # Espejos aumentan precio
        if self.tiene_espejos:
            precio_final += 100.0
        
        return round(precio_final, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica del armario.
        
        Returns:
            str: Descripción completa del armario
        """
        descripcion = f"Armario '{self.nombre}' de {self.material} en color {self.color}."
        descripcion += f" {self.num_puertas} puertas"
        if self.num_cajones > 0:
            descripcion += f", {self.num_cajones} cajones"
        if self.tiene_espejos:
            descripcion += ", con espejo"
        descripcion += "."
        return descripcion
    