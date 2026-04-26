"""
Clase concreta Escritorio.
"""
from ..categorias.superficies import Superficie
class Escritorio(Superficie):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 largo: float, ancho: float, altura: float, tiene_gavetas: bool):
        super().__init__(nombre, material, color, precio_base, largo, ancho, altura)
        self._tiene_gavetas = tiene_gavetas
        pass
    
    @property
    def tiene_gavetas(self) -> bool:
        """Getter para saber si el escritorio tiene gavetas."""
        return self._tiene_gavetas
    
    def obtener_descripcion(self) -> str:
        """
        Implementación concreta del método abstracto para obtener una descripción detallada del escritorio.
        Returns:
            str: Descripción del escritorio
        """        
        descripcion = f"Escritorio '{self.nombre}' de material {self.material}, color {self.color}."
        descripcion += f" Tamaño: {self.largo}x{self.ancho}x{self.altura} metros."
        descripcion += f" Gavetas: {'Sí' if self.tiene_gavetas else 'No'}."
        return descripcion
    