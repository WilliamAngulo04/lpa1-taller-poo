"""
Clase concreta Cama.
Implementa un mueble para dormir.
"""

from ..categorias.superficies import Superficies


class Cama(Superficies):
    """
    Clase concreta que representa una cama.
    
    Una cama es una superficie para dormir.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Superficies
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos de la cama
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tamaño: str, incluye_colchon: bool = True, tiene_cabecera: bool = False):
        """
        Constructor de la cama.
        
        Args:
            tamaño: Tamaño de la cama (individual, matrimonial, king, etc.)
            incluye_colchon: Si incluye colchón
            tiene_cabecera: Si tiene cabecera
            Otros argumentos heredados de Superficies
        """
        # Determinar capacidad de personas basada en tamaño
        capacidad = 1 if tamaño.lower() in ["individual", "single"] else 2
        
        super().__init__(nombre, material, color, precio_base,
                        forma=tamaño, capacidad_personas=capacidad,
                        tiene_cajones=False)
        
        self._tamaño = tamaño
        self._incluye_colchon = incluye_colchon
        self._tiene_cabecera = tiene_cabecera
    
    @property
    def tamaño(self) -> str:
        """Getter para el tamaño."""
        return self._tamaño
    
    @tamaño.setter
    def tamaño(self, value: str) -> None:
        """Setter para el tamaño."""
        self._tamaño = value
    
    @property
    def incluye_colchon(self) -> bool:
        """Getter para si incluye colchón."""
        return self._incluye_colchon
    
    @incluye_colchon.setter
    def incluye_colchon(self, value: bool) -> None:
        """Setter para si incluye colchón."""
        self._incluye_colchon = value
    
    @property
    def tiene_cabecera(self) -> bool:
        """Getter para si tiene cabecera."""
        return self._tiene_cabecera
    
    @tiene_cabecera.setter
    def tiene_cabecera(self, value: bool) -> None:
        """Setter para si tiene cabecera."""
        self._tiene_cabecera = value
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para camas.
        
        Returns:
            float: Precio final de la cama
        """
        precio_final = self.precio_base
        
        # Factor por tamaño
        if self.tamaño.lower() in ["matrimonial", "queen"]:
            precio_final *= 1.3
        elif self.tamaño.lower() in ["king"]:
            precio_final *= 1.5
        
        # Cabecera aumenta precio
        if self.tiene_cabecera:
            precio_final += 80.0
        
        # Colchón incluido aumenta precio
        if self.incluye_colchon:
            precio_final += 150.0
        
        return round(precio_final, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica de la cama.
        
        Returns:
            str: Descripción completa de la cama
        """
        descripcion = f"Cama '{self.nombre}' tamaño {self.tamaño} de {self.material} en color {self.color}."
        if self.incluye_colchon:
            descripcion += " Incluye colchón."
        if self.tiene_cabecera:
            descripcion += " Con cabecera."
        return descripcion