"""
Clase abstracta para muebles de almacenamiento.
Esta clase agrupa las características comunes de armarios, cajoneras, etc.
"""

from abc import ABC, abstractmethod
from .mueble import Mueble


class Almacenamiento(Mueble):
    """
    Clase abstracta para todos los muebles de almacenamiento.
    
    Hereda de Mueble y añade características específicas del almacenamiento
    como número de puertas, cajones, capacidad, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Agrupa características comunes de muebles de almacenamiento
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 num_puertas: int = 0, num_cajones: int = 0, tiene_espejos: bool = False):
        """
        Constructor para muebles de almacenamiento.
        
        Args:
            num_puertas: Número de puertas (0 para muebles sin puertas)
            num_cajones: Número de cajones
            tiene_espejos: Si tiene espejos incorporados
            Otros argumentos heredados de Mueble
        """
        super().__init__(nombre, material, color, precio_base)
        
        if num_puertas < 0:
            raise ValueError("El número de puertas no puede ser negativo")
        if num_cajones < 0:
            raise ValueError("El número de cajones no puede ser negativo")
        
        self._num_puertas = num_puertas
        self._num_cajones = num_cajones
        self._tiene_espejos = tiene_espejos
    
    @property
    def num_puertas(self) -> int:
        """Getter para el número de puertas."""
        return self._num_puertas
    
    @num_puertas.setter
    def num_puertas(self, value: int) -> None:
        """Setter para el número de puertas con validación."""
        if value < 0:
            raise ValueError("El número de puertas no puede ser negativo")
        self._num_puertas = value
    
    @property
    def num_cajones(self) -> int:
        """Getter para el número de cajones."""
        return self._num_cajones
    
    @num_cajones.setter
    def num_cajones(self, value: int) -> None:
        """Setter para el número de cajones con validación."""
        if value < 0:
            raise ValueError("El número de cajones no puede ser negativo")
        self._num_cajones = value
    
    @property
    def tiene_espejos(self) -> bool:
        """Getter para si tiene espejos."""
        return self._tiene_espejos
    
    @tiene_espejos.setter
    def tiene_espejos(self, value: bool) -> None:
        """Setter para si tiene espejos."""
        self._tiene_espejos = value
    
    def calcular_capacidad_almacenamiento(self) -> int:
        """
        Calcula la capacidad de almacenamiento basada en puertas y cajones.
        
        Returns:
            int: Capacidad de almacenamiento (unidades arbitrarias)
        """
        capacidad = 0
        
        # Cada puerta aporta capacidad base
        capacidad += self.num_puertas * 10
        
        # Cada cajón aporta capacidad adicional
        capacidad += self.num_cajones * 5
        
        # Espejos pueden añadir valor estético pero no capacidad
        if self.tiene_espejos:
            capacidad += 2
        
        return capacidad
    
    @abstractmethod
    def calcular_precio(self) -> float:
        """
        Calcula el precio final del mueble de almacenamiento.
        Debe ser implementado por las clases concretas.
        
        Returns:
            float: Precio final calculado
        """
        pass
    
    @abstractmethod
    def obtener_descripcion(self) -> str:
        """
        Obtiene una descripción detallada del mueble de almacenamiento.
        Debe ser implementado por las clases concretas.
        
        Returns:
            str: Descripción completa del mueble
        """
        pass
