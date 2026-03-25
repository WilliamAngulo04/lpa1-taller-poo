"""
Clase concreta Sofa.
"""
from ..categorias.superficies import Superficie
class Sofa(Superficie):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 largo: float, ancho: float, altura: float, capacidad_asientos: int):
        super().__init__(nombre, material, color, precio_base, largo, ancho, altura)
        self._capacidad_asientos = capacidad_asientos
        pass
    
    @property
    def capacidad_asientos(self) -> int:
        """Getter para la capacidad de asientos del sofá."""
        return self._capacidad_asientos
    
    def obtener_descripcion(self) -> str:
        """
        Implementación concreta del método abstracto para obtener una descripción detallada del sofá.
        Returns:
            str: Descripción del sofá
        """        
        descripcion = f"Sofá '{self.nombre}' de material {self.material}, color {self.color}."
        descripcion += f" Tamaño: {self.largo}x{self.ancho}x{self.altura} metros."
        descripcion += f" Capacidad de asientos: {self.capacidad_asientos} personas."
        return descripcion
    
    def es_sofa_esquinero(self) -> bool:
        """
        Método específico para determinar si el sofá es esquinero.
         Returns:
             bool: True si el sofá es esquinero, False en caso contrario
         """
        # Un sofá es esquinero si su largo es mayor que su ancho
        return self.largo > self.ancho
    