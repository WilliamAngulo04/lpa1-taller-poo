"""
Clase abstracta para muebles con superficies de trabajo o del hogar.
Esta clase agrupa las características comunes de mesas, escritorios, etc.
"""

from abc import ABC, abstractmethod
from .mueble import Mueble


class Superficies(Mueble):
    """
    Clase abstracta para todos los muebles con superficies de trabajo.
    
    Hereda de Mueble y añade características específicas de las superficies
    como forma, capacidad de personas, cajones, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Agrupa características comunes de muebles con superficies
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str, capacidad_personas: int, tiene_cajones: bool = False):
        """
        Constructor para muebles con superficies.
        
        Args:
            forma: Forma de la superficie (rectangular, redonda, L, etc.)
            capacidad_personas: Número máximo de personas que pueden usar la superficie
            tiene_cajones: Si tiene cajones incorporados
            Otros argumentos heredados de Mueble
        """
        super().__init__(nombre, material, color, precio_base)
        
        if capacidad_personas < 1:
            raise ValueError("La capacidad de personas debe ser al menos 1")
        
        self._forma = forma
        self._capacidad_personas = capacidad_personas
        self._tiene_cajones = tiene_cajones
    
    @property
    def forma(self) -> str:
        """Getter para la forma de la superficie."""
        return self._forma
    
    @forma.setter
    def forma(self, value: str) -> None:
        """Setter para la forma con validación."""
        if not value or not value.strip():
            raise ValueError("La forma no puede estar vacía")
        self._forma = value.strip()
    
    @property
    def capacidad_personas(self) -> int:
        """Getter para la capacidad de personas."""
        return self._capacidad_personas
    
    @capacidad_personas.setter
    def capacidad_personas(self, value: int) -> None:
        """Setter para la capacidad de personas con validación."""
        if value < 1:
            raise ValueError("La capacidad de personas debe ser al menos 1")
        self._capacidad_personas = value
    
    @property
    def tiene_cajones(self) -> bool:
        """Getter para si tiene cajones."""
        return self._tiene_cajones
    
    @tiene_cajones.setter
    def tiene_cajones(self, value: bool) -> None:
        """Setter para si tiene cajones."""
        self._tiene_cajones = value
    
    def calcular_area_util(self) -> float:
        """
        Calcula el área útil aproximada de la superficie.
        Este es un cálculo simplificado basado en la capacidad de personas.
        
        Returns:
            float: Área útil en metros cuadrados aproximados
        """
        # Estimación simple: cada persona necesita aproximadamente 1.5 m²
        area_base = self.capacidad_personas * 1.5
        
        # Ajustes por forma
        if self.forma.lower() == "redonda":
            # Las mesas redondas son más eficientes en espacio
            area_base *= 0.9
        elif self.forma.lower() == "l":
            # Las formas L pueden ser más grandes
            area_base *= 1.2
        
        # Cajones pueden reducir ligeramente el área útil
        if self.tiene_cajones:
            area_base *= 0.95
        
        return round(area_base, 2)
    
    @abstractmethod
    def calcular_precio(self) -> float:
        """
        Calcula el precio final del mueble con superficie.
        Debe ser implementado por las clases concretas.
        
        Returns:
            float: Precio final calculado
        """
        pass
    
    @abstractmethod
    def obtener_descripcion(self) -> str:
        """
        Obtiene una descripción detallada del mueble con superficie.
        Debe ser implementado por las clases concretas.
        
        Returns:
            str: Descripción completa del mueble
        """
        pass
