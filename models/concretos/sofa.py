"""
Clase concreta Sofa.
Implementa un mueble de asiento para múltiples personas.
"""

from ..categorias.asientos import Asiento


class Sofa(Asiento):
    """
    Clase concreta que representa un sofá.
    
    Un sofá es un asiento cómodo para múltiples personas.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Asiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos del sofá
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int, tiene_respaldo: bool = True,
                 material_tapizado: str = None, es_modular: bool = False,
                 incluye_cojines: bool = False):
        """
        Constructor del sofá.
        
        Args:
            capacidad_personas: Número de personas que pueden sentarse
            tiene_respaldo: Si tiene respaldo
            material_tapizado: Material del tapizado
            es_modular: Si el sofá es modular
            incluye_cojines: Si incluye cojines
            Otros argumentos heredados de Asiento
        """
        super().__init__(nombre, material, color, precio_base,
                        capacidad_personas=capacidad_personas,
                        tiene_respaldo=tiene_respaldo,
                        material_tapizado=material_tapizado)
        
        self._es_modular = es_modular
        self._incluye_cojines = incluye_cojines
    
    @property
    def es_modular(self) -> bool:
        """Getter para si es modular."""
        return self._es_modular
    
    @es_modular.setter
    def es_modular(self, value: bool) -> None:
        """Setter para si es modular."""
        self._es_modular = value
    
    @property
    def incluye_cojines(self) -> bool:
        """Getter para si incluye cojines."""
        return self._incluye_cojines
    
    @incluye_cojines.setter
    def incluye_cojines(self, value: bool) -> None:
        """Setter para si incluye cojines."""
        self._incluye_cojines = value
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para sofás.
        
        Returns:
            float: Precio final del sofá
        """
        precio_final = self.precio_base
        
        # Factor de comodidad base
        precio_final *= self.calcular_factor_comodidad()
        
        # Factor por capacidad
        precio_final *= (1 + (self.capacidad_personas - 1) * 0.15)
        
        # Modular aumenta precio
        if self.es_modular:
            precio_final *= 1.3
        
        # Cojines aumentan precio
        if self.incluye_cojines:
            precio_final += 30.0
        
        return round(precio_final, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica del sofá.
        
        Returns:
            str: Descripción completa del sofá
        """
        descripcion = f"Sofá '{self.nombre}' de {self.material} en color {self.color}."
        descripcion += f" Capacidad: {self.capacidad_personas} personas."
        if self.material_tapizado:
            descripcion += f" Tapizado: {self.material_tapizado}."
        if self.es_modular:
            descripcion += " Modular."
        if self.incluye_cojines:
            descripcion += " Incluye cojines."
        return descripcion
    
    def es_sofa_grande(self) -> bool:
        """
        Determina si el sofá es considerado grande.
        
        Returns:
            bool: True si tiene capacidad para 3 o más personas
        """
        return self.capacidad_personas >= 3
    