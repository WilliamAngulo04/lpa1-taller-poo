"""
Clase SofaCama que implementa herencia múltiple.
Esta clase hereda tanto de Sofa como de Cama.
"""

# Importar las clases padre
from .sofa import Sofa
from .cama import Cama
from ..mueble import Mueble


class SofaCama(Sofa, Cama):
    """
    Clase que implementa herencia múltiple heredando de Sofa y Cama.
    
    Un sofá-cama es un mueble que funciona tanto como asiento durante el día
    como cama durante la noche.
    
    Conceptos OOP aplicados:
    - Herencia múltiple: Hereda de Sofa y Cama
    - Resolución MRO: Maneja el orden de resolución de métodos
    - Polimorfismo: Implementa comportamientos únicos combinando funcionalidades
    - Super(): Usa super() para resolver conflictos de herencia
    """
    
    def __init__(self, nombre: str, material: str, color: str, precio_base: float,
                 capacidad_personas: int = 3, material_tapizado: str = "tela",
                 tamaño_cama: str = "matrimonial", incluye_colchon: bool = True,
                 mecanismo_conversion: str = "plegable"):
        """
        Constructor del sofá-cama.
        
        Args:
            mecanismo_conversion: Tipo de mecanismo de conversión (plegable, extensible, etc.)
            Otros argumentos se pasan a las clases padre
        """
        # Inicializar la clase base común (Mueble) directamente
        Mueble.__init__(self, nombre, material, color, precio_base)
        
        # Inicializar atributos de Asiento (de Sofa)
        self._capacidad_personas = capacidad_personas
        self._tiene_respaldo = True
        self._material_tapizado = material_tapizado
        
        # Inicializar atributos de Superficies (de Cama)
        self._forma = "rectangular"  # Asumir forma para sofá-cama
        self._tiene_cajones = False  # Sofá-cama generalmente no tiene cajones
        
        # Inicializar atributos específicos de Cama
        self._tamaño = tamaño_cama
        self._incluye_colchon = incluye_colchon
        self._tiene_cabecera = False  # Sofá-cama generalmente no tiene cabecera
        
        # Inicializar atributos únicos del sofá-cama
        self._mecanismo_conversion = mecanismo_conversion
        self._modo_actual = "sofa"
    
    @property
    def mecanismo_conversion(self) -> str:
        """Getter para el mecanismo de conversión."""
        return self._mecanismo_conversion
    
    @property
    def modo_actual(self) -> str:
        """Getter para el modo actual (sofa o cama)."""
        return self._modo_actual
    
    @property
    def tamaño_cama(self) -> str:
        """Getter para el tamaño de cama."""
        return self._tamaño
    
    @property
    def incluye_colchon(self) -> bool:
        """Getter para si incluye colchón."""
        return self._incluye_colchon
    
    def convertir_a_cama(self) -> str:
        """
        Convierte el sofá en cama.
        Método específico del sofá-cama.
        
        Returns:
            str: Mensaje del resultado de la conversión
        """
        if self._modo_actual == "cama":
            return "El sofá-cama ya está en modo cama"

        self._modo_actual = "cama"
        return f"Sofá convertido a cama usando mecanismo {self.mecanismo_conversion}"

    def convertir_a_sofa(self) -> str:
        """
        Convierte la cama en sofá.
        Método específico del sofá-cama.

        Returns:
            str: Mensaje del resultado de la conversión
        """
        if self._modo_actual == "sofa":
            return "El sofá-cama ya está en modo sofá"

        self._modo_actual = "sofa"
        return f"Cama convertida a sofá usando mecanismo {self.mecanismo_conversion}"
    
    def calcular_precio(self) -> float:
        """
        Calcula el precio combinando las funcionalidades de sofá y cama.
        
        Returns:
            float: Precio final del sofá-cama
        """
        # Implementar cálculo de precio combinado
        # El sofá-cama es más caro que un sofá o cama individual
        # 1. Comenzar con precio base
        precio = self.precio_base
        
        # 2. Aplicar factor de comodidad de asiento
        precio *= self.calcular_factor_comodidad()
        
        # 3. Agregar valor por funcionalidad dual
        precio *= 1.5  # 50% más caro por ser dual
        
        # 4. Agregar costo por mecanismo de conversión
        if self.mecanismo_conversion == "electrico":
            precio += 200
        elif self.mecanismo_conversion == "hidraulico":
            precio += 150
        else:  # manual/plegable
            precio += 100
        
        # 5. Agregar costo si incluye colchón
        if self.incluye_colchon:
            precio += 300
        
        # return round(precio, 2)
        return round(precio, 2)
    
    def obtener_descripcion(self) -> str:
        """
        Descripción que combina características de sofá y cama.

        Returns:
            str: Descripción completa del sofá-cama
        """
        descripcion = f"Sofá-cama '{self.nombre}' de {self.material} en color {self.color}."
        descripcion += f" Capacidad: {self.capacidad_personas} personas como sofá."
        if self.material_tapizado:
            descripcion += f" Tapizado: {self.material_tapizado}."
        descripcion += f" Tamaño de cama: {self.tamaño_cama}."
        descripcion += f" Mecanismo: {self.mecanismo_conversion}."
        descripcion += f" Colchón incluido: {'Sí' if self.incluye_colchon else 'No'}."
        return descripcion

    def obtener_capacidad_total(self) -> dict:
        """
        Obtiene las capacidades en ambos modos.

        Returns:
            dict: Diccionario con capacidades para sofá y cama
        """
        return {
            "sofa": self.capacidad_personas,
            "cama": 1 if self.tamaño_cama.lower() in ["individual", "single"] else 2
        }
    
    # Implementar método para verificar compatibilidad de modo
    def puede_usar_como_cama(self) -> bool:
        """Verifica si actualmente puede usarse como cama."""
        return self._modo_actual == "cama"
    
    def puede_usar_como_sofa(self) -> bool:
        """Verifica si actualmente puede usarse como sofá."""
        return self._modo_actual == "sofa"
    
    def __str__(self) -> str:
        """
        Representación en cadena del sofá-cama.
        Sobrescribe el método heredado para mostrar información específica.
        """
        # Implementar representación personalizada
        return f"Sofá-cama {self.nombre} (modo: {self.modo_actual})"

