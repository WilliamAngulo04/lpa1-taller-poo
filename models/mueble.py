from abc import ABC, abstractmethod


class Mueble(ABC):
    """
    Clase abstracta base para todos los muebles.

    Define la estructura común para todos los muebles de la tienda.
    No puede ser instanciada directamente.

    Conceptos OOP aplicados:
    - Abstracción: Define una interfaz común sin implementación específica
    - Encapsulación: Usa atributos privados con getters/setters
    """

    def __init__(self, nombre: str, material: str, color: str, precio_base: float):
        self._nombre = nombre
        self._material = material
        self._color = color
        self._precio_base = precio_base

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def material(self) -> str:
        return self._material

    @property
    def color(self) -> str:
        return self._color

    @property
    def precio_base(self) -> float:
        return self._precio_base

    @nombre.setter
    def nombre(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = value.strip()

    @material.setter
    def material(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El material no puede estar vacío")
        self._material = value.strip()

    @color.setter
    def color(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("El color no puede estar vacío")
        self._color = value.strip()

    @precio_base.setter
    def precio_base(self, value: float) -> None:
        if value < 0:
            raise ValueError("El precio base no puede ser negativo")
        self._precio_base = value

    @abstractmethod
    def calcular_precio(self) -> float:
        """
        Calcula el precio final del mueble.
        Debe ser implementado por cada clase concreta.

        Returns:
            float: Precio final calculado
        """
        pass

    @abstractmethod
    def obtener_descripcion(self) -> str:
        """
        Obtiene una descripción detallada del mueble.
        Debe ser implementado por cada clase concreta.

        Returns:
            str: Descripción completa del mueble
        """
        pass

    def __str__(self) -> str:
        return f"{self.nombre} de {self.material} en color {self.color}"

    def __repr__(self) -> str:
        return f"Mueble(nombre='{self.nombre}', material='{self.material}', color='{self.color}', precio_base={self.precio_base})"
