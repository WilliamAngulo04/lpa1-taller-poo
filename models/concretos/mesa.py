"""
Clase concreta Mesa.
"""
from ..categorias.superficies import Superficie
class Mesa(Superficie):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 largo: float, ancho: float, altura: float, tipo_mesa: str):
        super().__init__(nombre, material, color, precio_base, largo, ancho, altura)
        self._tipo_mesa = tipo_mesa
        pass
    
    @property
    def tipo_mesa(self) -> str:
        """Getter para el tipo de mesa."""
        return self._tipo_mesa
    
    def obtener_descripcion(self) -> str:
        """
        Implementación concreta del método abstracto para obtener una descripción detallada de la mesa.
        Returns:
            str: Descripción de la mesa
        """        
        descripcion = f"Mesa '{self.nombre}' de material {self.material}, color {self.color}."
        descripcion += f" Tamaño: {self.largo}x{self.ancho}x{self.altura} metros."
        descripcion += f" Tipo de mesa: {self.tipo_mesa}."
        return descripcion