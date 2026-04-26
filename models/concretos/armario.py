"""
Clase concreta Armario.
"""
from ..categorias.almacenamiento import Almacenamiento
class Armario(Almacenamiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_volumen: float, tipo_puertas: str, tiene_espejo: bool):
        super().__init__(nombre, material, color, precio_base, capacidad_volumen, tipo_puertas)
        self._tiene_espejo = tiene_espejo
        pass
    
    @property
    def tiene_espejo(self) -> bool:
        """Getter para saber si el armario tiene espejo."""
        return self._tiene_espejo
    
    def obtener_descripcion(self) -> str:
        """
        Implementación concreta del método abstracto para obtener una descripción detallada del armario.
        Returns:
            str: Descripción del armario
        """        
        descripcion = f"Armario '{self.nombre}' de material {self.material}, color {self.color}."
        descripcion += f" Capacidad: {self.capacidad_volumen} litros, Puertas: {self.tipo_puertas}."
        descripcion += f" Espejo: {'Sí' if self.tiene_espejo else 'No'}."
        return descripcion
    