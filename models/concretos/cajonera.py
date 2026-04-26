"""
Clase concreta Cajonera.
Implementa un mueble de almacenamiento con cajones.
"""

from ..categorias.almacenamiento import Almacenamiento


class Cajonera(Almacenamiento):
    """
    Clase concreta que representa una cajonera.
    
    Una cajonera es un mueble de almacenamiento con cajones.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Almacenamiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos de la cajonera
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 num_cajones: int, tiene_ruedas: bool = False):
        """
        Constructor de la cajonera.
        
        Args:
            num_cajones: Número de cajones
            tiene_ruedas: Si tiene ruedas
            Otros argumentos heredados de Almacenamiento
        """
        super().__init__(nombre, material, color, precio_base,
                        num_puertas=0, num_cajones=num_cajones,
                        tiene_espejos=False)
        
        self._tiene_ruedas = tiene_ruedas
    
    @property
    def tiene_ruedas(self) -> bool:
        """Getter para si tiene ruedas."""
        return self._tiene_ruedas
    
    @tiene_ruedas.setter
    def tiene_ruedas(self, value: bool) -> None:
        """Setter para si tiene ruedas."""
        self._tiene_ruedas = value
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para cajoneras.
        
        Returns:
            float: Precio final de la cajonera
        """
        precio_final = self.precio_base
        
        # Factor por número de cajones
        precio_final *= (1 + self.num_cajones * 0.1)
        
        # Ruedas aumentan precio
        if self.tiene_ruedas:
            precio_final += 25.0
        
        # Factor por material
        if self.material.lower() == "madera":
            precio_final *= 1.1
        
        return round(precio_final, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica de la cajonera.
        
        Returns:
            str: Descripción completa de la cajonera
        """
        descripcion = f"Cajonera '{self.nombre}' de {self.material} en color {self.color}."
        descripcion += f" {self.num_cajones} cajones"
        if self.tiene_ruedas:
            descripcion += ", con ruedas"
        descripcion += "."
        return descripcion