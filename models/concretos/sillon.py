"""
Clase concreta Sillón.
Implementa un mueble de asiento cómodo para una persona.
"""

from ..categorias.asientos import Asiento


class Sillon(Asiento):
    """
    Clase concreta que representa un sillón.
    
    Un sillón es un asiento cómodo individual, a menudo reclinable.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Asiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos del sillón
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = None,
                 es_reclinable: bool = False, tiene_reposapiés: bool = False):
        """
        Constructor del sillón.
        
        Args:
            tiene_respaldo: Si tiene respaldo
            material_tapizado: Material del tapizado
            es_reclinable: Si es reclinable
            tiene_reposapiés: Si tiene reposapiés
            Otros argumentos heredados de Asiento
        """
        super().__init__(nombre, material, color, precio_base, capacidad_personas=1,
                        tiene_respaldo=tiene_respaldo, material_tapizado=material_tapizado)
        
        self._es_reclinable = es_reclinable
        self._tiene_reposapiés = tiene_reposapiés
    
    @property
    def es_reclinable(self) -> bool:
        """Getter para si es reclinable."""
        return self._es_reclinable
    
    @es_reclinable.setter
    def es_reclinable(self, value: bool) -> None:
        """Setter para si es reclinable."""
        self._es_reclinable = value
    
    @property
    def tiene_reposapiés(self) -> bool:
        """Getter para si tiene reposapiés."""
        return self._tiene_reposapiés
    
    @tiene_reposapiés.setter
    def tiene_reposapiés(self, value: bool) -> None:
        """Setter para si tiene reposapiés."""
        self._tiene_reposapiés = value
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para sillones.
        
        Returns:
            float: Precio final del sillón
        """
        precio_final = self.precio_base
        
        # Factor de comodidad
        precio_final *= self.calcular_factor_comodidad()
        
        # Reclinable aumenta precio significativamente
        if self.es_reclinable:
            precio_final *= 1.4
        
        # Reposapiés añade costo
        if self.tiene_reposapiés:
            precio_final += 40.0
        
        return round(precio_final, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica del sillón.
        
        Returns:
            str: Descripción completa del sillón
        """
        descripcion = f"Sillón '{self.nombre}' de {self.material} en color {self.color}."
        if self.material_tapizado:
            descripcion += f" Tapizado: {self.material_tapizado}."
        if self.es_reclinable:
            descripcion += " Reclinable."
        if self.tiene_reposapiés:
            descripcion += " Con reposapiés."
        return descripcion
    
    def reclinar(self) -> str:
        """
        Simula la acción de reclinar el sillón.

        Returns:
            str: Mensaje del resultado
        """
        if not self.es_reclinable:
            return "Este sillón no es reclinable."
        return "Sillón reclinado para mayor comodidad."
    