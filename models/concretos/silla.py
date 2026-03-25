"""
Clase concreta Silla.
Implementa un mueble de asiento específico para una persona.
"""

# Importar la clase padre Asiento
from ..categorias.asientos import Asiento


class Silla(Asiento):
    """
    Clase concreta que representa una silla.
    
    Una silla es un asiento individual con características específicas
    como altura regulable, ruedas, etc.
    
    Conceptos OOP aplicados:
    - Herencia: Hereda de Asiento
    - Polimorfismo: Implementa métodos abstractos de manera específica
    - Encapsulación: Protege atributos específicos de la silla
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 tiene_respaldo: bool = True, material_tapizado: str = None,
                 altura_regulable: bool = False, tiene_ruedas: bool = False):
        """
        Constructor de la silla.
        
        Args:
            altura_regulable: Si la silla puede regular su altura
            tiene_ruedas: Si la silla tiene ruedas
            Otros argumentos heredados de Asiento
        """
        # Llamar al constructor padre con capacidad fija de 1 persona
        super().__init__(nombre, material, color, precio_base, capacidad=1)
        
        # Inicializar atributos específicos de la silla
        self._tiene_respaldo = tiene_respaldo
        self._material_tapizado = material_tapizado
        self._altura_regulable = altura_regulable
        self._tiene_ruedas = tiene_ruedas

        pass
    
    # TODO: Implementar propiedades para los nuevos atributos
    @property
    def altura_regulable(self) -> bool:
        """Getter para altura regulable."""
        return self._altura_regulable
    
    @altura_regulable.setter
    def altura_regulable(self, value: bool) -> None:
        """Setter para altura regulable."""
        self._altura_regulable = value
    
    def calcular_precio(self) -> float:
        """
        Implementa el cálculo de precio específico para sillas.
        
        Returns:
            float: Precio final de la silla
        """
        # Implementar cálculo de precio para silla

        # 1. Comenzar con el precio base
        precio_final = self.precio_base
        # 2. Aplicar factor de comodidad heredado
        precio_final *= self.calcular_factor_comodidad()
        # 3. Agregar costos por características especiales
        if self.altura_regulable:
            precio_final += 20.0  # Costo adicional por altura regulable
        if self.tiene_ruedas:
            precio_final += 15.0  # Costo adicional por ruedas
        # 4. Retornar precio redondeado a 2 decimales

        return round(precio_final, 2)

    def obtener_descripcion(self) -> str:
        """
        Implementa la descripción específica de la silla.
        
        Returns:
            str: Descripción completa de la silla
        """
        # Crear y retornar descripción detallada
        descripcion = f"Silla '{self.nombre}' de material {self.material}, color {self.color}."
        descripcion += f" Respaldo: {'Sí' if self.tiene_respaldo else 'No'}."
        if self.material_tapizado:
            descripcion += f" Tapizado: {self.material_tapizado}."
        descripcion += f" Altura regulable: {'Sí' if self.altura_regulable else 'No'}."
        descripcion += f" Ruedas: {'Sí' if self.tiene_ruedas else 'No'}."
        return descripcion
        
        pass
    
    def regular_altura(self, nueva_altura: int) -> str:
        """
        Simula la regulación de altura de la silla.
        Método específico de la clase Silla.
        
        Args:
            nueva_altura: Nueva altura en centímetros
            
        Returns:
            str: Mensaje del resultado de la operación
        """
        # Implementar lógica de regulación
        if not self.altura_regulable:
            return "Esta silla no tiene altura regulable."
        # Aquí podríamos agregar lógica para validar la nueva altura, etc.
        return f"Altura de la silla regulada a {nueva_altura} cm."
        pass
    
    def es_silla_oficina(self) -> bool:
        """
        Determina si la silla es adecuada para oficina.
        
        Returns:
            bool: True si es silla de oficina
        """
        # Una silla es de oficina si tiene ruedas Y altura regulable
        return self.tiene_ruedas and self.altura_regulable

