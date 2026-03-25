"""
Clase concreta Cama.
"""
from ..categorias.superficies import Superficie
class Cama(Superficie):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 largo: float, ancho: float, altura: float, tipo_cama: str):
        super().__init__(nombre, material, color, precio_base, largo, ancho, altura)
        self._tipo_cama = tipo_cama
        pass
    
    @property
    def tipo_cama(self) -> str:
        """Getter para el tipo de cama."""
        return self._tipo_cama
    
    def obtener_descripcion(self) -> str:
        """
        Implementación concreta del método abstracto para obtener una descripción detallada de la cama.
        Returns:
            str: Descripción de la cama
        """        
        descripcion = f"Cama '{self.nombre}' de material {self.material}, color {self.color}."
        descripcion += f" Tamaño: {self.largo}x{self.ancho}x{self.altura} metros."
        descripcion += f" Tipo de cama: {self.tipo_cama}."
        return descripcion