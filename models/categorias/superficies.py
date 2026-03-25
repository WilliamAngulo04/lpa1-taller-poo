"""
Clase abstracta para muebles para superficios de trabajo o del hogar .
"""

from ..mueble import Mueble
from abc import ABC, abstractclassmethod

class Superficie(Mueble):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                    largo: float, ancho: float, altura: float):
            super().__init__(nombre, material, color, precio_base)
            self._largo = largo
            self._ancho = ancho
            self._altura = altura
            pass
    @property
    def largo(self) -> float:
        """Getter para el largo de la superficie."""
        return self._largo

    @property
    def ancho(self) -> float:
        """Getter para el ancho de la superficie."""
        return self._ancho

    @property
    def altura(self) -> float:
        """Getter para la altura de la superficie."""
        return self._altura
    
    def calcular_factor_tamaño(self) -> float:
        """
        Método para calcular un factor multiplicador basado en el tamaño de la superficie.
        Este factor puede ser utilizado para ajustar el precio base del mueble.
        """
        factor = 1.0
        
        # Ejemplo de lógica: si el área es mayor a 1 metro cuadrado, aumentar el factor
        area = self.largo * self.ancho
        if area > 1.0:
            factor += 0.2
        elif area > 0.5:
            factor += 0.1
        
        return factor
    
    @abstractclassmethod
    def obtener_descripcion(self) -> str:
        """
        Método abstracto para obtener una descripción detallada de la superficie.
        Las clases concretas deben proporcionar su propia descripción específica.
        """
    