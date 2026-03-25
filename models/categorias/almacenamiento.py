"""
Clase abstracta para muebles de almacenamiento.
"""
from ..mueble import Mueble
from abc import ABC, abstractclassmethod

class Almacenamiento(Mueble):
    """
    Clase abstracta para muebles de almacenamiento.
    
    Hereda de Mueble y añade características específicas de almacenamiento
    como capacidad de volumen, tipo de puertas, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Agrupa características comunes de almacenamiento
    - Polimorfismo: Permite diferentes implementaciones del cálculo de capacidad
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_volumen: float, tipo_puertas: str):
        """
        Constructor para muebles de almacenamiento.
        
        Args:
            capacidad_volumen: Volumen de almacenamiento en litros
            tipo_puertas: Tipo de puertas del mueble de almacenamiento
        """
        super().__init__(nombre, material, color, precio_base)
        self._capacidad_volumen = capacidad_volumen
        self._tipo_puertas = tipo_puertas
        pass

    @property
    def capacidad_volumen(self) -> float:
        """Getter para la capacidad de volumen."""
        return self._capacidad_volumen

    @property
    def tipo_puertas(self) -> str:
        """Getter para el tipo de puertas."""
        return self._tipo_puertas
    
    def calcular_factor_capacidad(self) -> float:
        """
        Método para calcular un factor multiplicador basado en la capacidad de volumen.
        Este factor puede ser utilizado para ajustar el precio base del mueble.
        """
        factor = 1.0
        
        # Ejemplo de lógica: si la capacidad es mayor a 100 litros, aumentar el factor
        if self.capacidad_volumen > 100:
            factor += 0.2
        elif self.capacidad_volumen > 50:
            factor += 0.1
        
        return factor
    
    @abstractclassmethod
    def obtener_descripcion(self) -> str:
        """
        Método abstracto para obtener una descripción detallada del mueble de almacenamiento.
        Las clases concretas deben proporcionar su propia descripción específica.
        """
        pass

    