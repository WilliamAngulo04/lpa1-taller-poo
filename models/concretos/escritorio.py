"""
Clase concreta Escritorio.
Implementa un mueble de superficie para trabajar.
"""

from ..categorias.superficies import Superficies


class Escritorio(Superficies):
    """
    Clase concreta que representa un escritorio.
    
    Un escritorio es una superficie para trabajar.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Superficies
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos del escritorio
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 forma: str, tiene_cajones: bool = False, num_cajones: int = 0,
                 tiene_iluminacion: bool = False):
        """
        Constructor del escritorio.
        
        Args:
            forma: Forma del escritorio (rectangular, L, etc.)
            tiene_cajones: Si tiene cajones
            num_cajones: Número de cajones
            tiene_iluminacion: Si tiene iluminación incorporada
            Otros argumentos heredados de Superficies
        """
        super().__init__(nombre, material, color, precio_base,
                        forma=forma, capacidad_personas=1,
                        tiene_cajones=tiene_cajones)
        
        self._num_cajones = num_cajones
        self._tiene_iluminacion = tiene_iluminacion
    
    @property
    def num_cajones(self) -> int:
        """Getter para el número de cajones."""
        return self._num_cajones
    
    @num_cajones.setter
    def num_cajones(self, value: int) -> None:
        """Setter para el número de cajones."""
        if value < 0:
            raise ValueError("El número de cajones no puede ser negativo")
        self._num_cajones = value
    
    @property
    def tiene_iluminacion(self) -> bool:
        """Getter para si tiene iluminación."""
        return self._tiene_iluminacion
    
    @tiene_iluminacion.setter
    def tiene_iluminacion(self, value: bool) -> None:
        """Setter para si tiene iluminación."""
        self._tiene_iluminacion = value
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para escritorios.
        
        Returns:
            float: Precio final del escritorio
        """
        precio_final = self.precio_base
        
        # Cajones aumentan precio
        precio_final += self.num_cajones * 30.0
        
        # Forma L aumenta precio
        if self.forma.lower() == "l":
            precio_final *= 1.2
        
        # Iluminación aumenta precio
        if self.tiene_iluminacion:
            precio_final += 50.0
        
        return round(precio_final, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica del escritorio.
        
        Returns:
            str: Descripción completa del escritorio
        """
        descripcion = f"Escritorio '{self.nombre}' de {self.material} en color {self.color}."
        descripcion += f" Forma: {self.forma}."
        if self.tiene_cajones and self.num_cajones > 0:
            descripcion += f" {self.num_cajones} cajones."
        if self.tiene_iluminacion:
            descripcion += " Con iluminación incorporada."
        return descripcion
    