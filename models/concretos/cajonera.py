"""
Clase concreta Cajonera.
"""
from ..categorias.almacenamiento import Almacenamiento
class Cajonera(Almacenamiento):
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_volumen: float, tipo_puertas: str, numero_cajones: int):
        super().__init__(nombre, material, color, precio_base, capacidad_volumen, tipo_puertas)
        self._numero_cajones = numero_cajones
        pass
    
    @property
    def numero_cajones(self) -> int:
        """Getter para el número de cajones."""
        return self._numero_cajones
    
    def obtener_descripcion(self) -> str:
        """
        Implementación concreta del método abstracto para obtener una descripción detallada de la cajonera.
        Returns:
            str: Descripción de la cajonera
        """        
        descripcion = f"Cajonera '{self.nombre}' de material {self.material}, color {self.color}."
        descripcion += f" Capacidad: {self.capacidad_volumen} litros, Puertas: {self.tipo_puertas}."
        descripcion += f" Número de cajones: {self.numero_cajones}."
        return descripcion
    
    def calcular_precio_final(self) -> float:
        """
        Implementación concreta del método abstracto para calcular el precio final de la cajonera.
            Returns:
                float: Precio final de la cajonera
            """
        # Implementar cálculo de precio para cajonera
        # 1. Comenzar con el precio base
        precio_final = self.precio_base
        # 2. Aplicar factor de almacenamiento heredado
        precio_final *= self.calcular_factor_almacenamiento()
        # 3. Agregar costos por características especiales
        precio_final += self.numero_cajones * 10.0  # Costo adicional por cada cajón
        # 4. Retornar precio redondeado a 2 decimales
        return round(precio_final, 2)