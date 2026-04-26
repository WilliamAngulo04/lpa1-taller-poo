"""
Clase abstracta para muebles de asiento.
Esta clase agrupa las características comunes de sillas, sillones y sofás.
"""

from abc import ABC, abstractmethod
from ..mueble import Mueble


class Asiento(Mueble):
    """
    Clase abstracta para todos los muebles donde las personas se sientan.
    
    Hereda de Mueble y añade características específicas de los asientos
    como capacidad de personas, tipo de respaldo, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Extiende la clase Mueble
    - Abstracción: Agrupa características comunes de asientos
    - Polimorfismo: Permite diferentes implementaciones del cálculo de comodidad
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int, tiene_respaldo: bool, material_tapizado: str = None):
        """
        Constructor para muebles de asiento.
        
        Args:
            capacidad_personas: Número de personas que pueden sentarse
            tiene_respaldo: Si el asiento tiene respaldo o no
            material_tapizado: Material del tapizado (opcional)
            Otros argumentos heredados de Mueble
        """
        super().__init__(nombre, material, color, precio_base)
        
        if capacidad_personas < 1:
            raise ValueError("La capacidad de personas debe ser al menos 1")
        self._capacidad_personas = capacidad_personas
        self._tiene_respaldo = tiene_respaldo
        self._material_tapizado = material_tapizado
    
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
    def tiene_respaldo(self) -> bool:
        """Getter para si tiene respaldo."""
        return self._tiene_respaldo
    
    @tiene_respaldo.setter
    def tiene_respaldo(self, value: bool) -> None:
        """Setter para si tiene respaldo."""
        self._tiene_respaldo = value
    
    @property
    def material_tapizado(self) -> str:
        """Getter para el material del tapizado."""
        return self._material_tapizado
    
    @material_tapizado.setter
    def material_tapizado(self, value: str) -> None:
        """Setter para el material del tapizado."""
        self._material_tapizado = value
    
    def calcular_factor_comodidad(self) -> float:
        """
        Calcula un factor de comodidad basado en las características del asiento.
        
        Returns:
            float: Factor de comodidad entre 0.8 y 2.0
        """
        factor = 1.0
        
        if self.tiene_respaldo:
            factor += 0.2
        
        if self.material_tapizado:
            if self.material_tapizado.lower() == "cuero":
                factor += 0.3
            elif self.material_tapizado.lower() == "tela":
                factor += 0.1
        
        # Limitar el factor entre 0.8 y 2.0
        return max(0.8, min(2.0, factor))
    
    @abstractmethod
    def calcular_precio(self) -> float:
        """
        Calcula el precio final del asiento.
        Debe ser implementado por las clases concretas.
        
        Returns:
            float: Precio final calculado
        """
        pass
    
    @abstractmethod
    def obtener_descripcion(self) -> str:
        """
        Obtiene una descripción detallada del asiento.
        Debe ser implementado por las clases concretas.
        
        Returns:
            str: Descripción completa del asiento
        """
        pass
    
    def obtener_info_asiento(self) -> str:
        """
        Obtiene información específica del asiento.
        Método concreto auxiliar para las clases hijas.

        Returns:
            str: Información detallada del asiento
        """
        info = f"Capacidad: {self.capacidad_personas} personas"
        info += f", Respaldo: {'Sí' if self.tiene_respaldo else 'No'}"
        if self.material_tapizado:
            info += f", Tapizado: {self.material_tapizado}"
        return info
    

