"""
Clase concreta Sillón.
"""
from ..categorias.asientos import Asiento
class Sillon(Asiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool, material_tapizado: str, altura_regulable: bool, tiene_ruedas: bool):
        """
        Inicializa un nuevo sillón con sus características específicas.
        Args:
            nombre: Nombre del sillón
            material: Material del sillón
            color: Color del sillón
            precio_base: Precio base del sillón
            tiene_respaldo: Si el sillón tiene respaldo
            material_tapizado: Material del tapizado (si lo tiene)
            altura_regulable: Si el sillón tiene altura regulable
            tiene_ruedas: Si el sillón tiene ruedas
        """
        super().__init__(nombre, material, color, precio_base, capacidad=1)
        self._tiene_respaldo = tiene_respaldo
        self._material_tapizado = material_tapizado
        self._altura_regulable = altura_regulable
        self._tiene_ruedas = tiene_ruedas
        pass

    def calcular_precio(self) -> float:
        """
        Calcula el precio final del sillón considerando sus características.
        Returns:
            float: Precio final del sillón
        """
        precio_final = self.precio_base
        if self._tiene_respaldo:
            precio_final += 50.0  # Costo adicional por respaldo
        if self._material_tapizado:
            precio_final += 30.0  # Costo adicional por tapizado
        if self._altura_regulable:
            precio_final += 20.0  # Costo adicional por altura regulable
        if self._tiene_ruedas:
            precio_final += 15.0  # Costo adicional por ruedas
        return round(precio_final, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Obtiene una descripción detallada del sillón.
        Returns:
            str: Descripción completa del sillón
        """
        descripcion = f"Sillón '{self.nombre}' de material {self.material}, color {self.color}."
        descripcion += f" Respaldo: {'Sí' if self._tiene_respaldo else 'No'}."
        if self._material_tapizado:
            descripcion += f" Tapizado: {self._material_tapizado}."
        descripcion += f" Altura regulable: {'Sí' if self._altura_regulable else 'No'}."
        descripcion += f" Ruedas: {'Sí' if self._tiene_ruedas else 'No'}."
        return descripcion
    
    def regular_altura(self, nueva_altura: float) -> str:
        """
        Regula la altura del sillón si es posible.
        Args:
            nueva_altura: Nueva altura deseada para el sillón
        Returns:
            str: Mensaje indicando el resultado de la operación
        """
        if not self._altura_regulable:
            return "Este sillón no tiene altura regulable."
        # Aquí podríamos agregar lógica para validar la nueva altura, etc.
        return f"Altura del sillón regulada a {nueva_altura} cm."
    