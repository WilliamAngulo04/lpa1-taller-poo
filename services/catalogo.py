"""
Servicio de catálogo para presentar y organizar los muebles de la tienda.
"""

from typing import List, Dict
from models.mueble import Mueble


class Catalogo:
    """
    Clase que representa el catálogo de productos de la tienda.

    Proporciona métodos para organizar y presentar los muebles disponibles,
    sin manejar inventario ni ventas (eso es responsabilidad de TiendaMuebles).

    Conceptos OOP aplicados:
    - Separación de responsabilidades: sólo se ocupa de la presentación del catálogo
    - Encapsulación: maneja internamente la lista de muebles
    """

    def __init__(self, nombre: str = "Catálogo General"):
        self._nombre = nombre
        self._muebles: List[Mueble] = []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def total(self) -> int:
        return len(self._muebles)

    def agregar(self, mueble: Mueble) -> None:
        if not isinstance(mueble, Mueble):
            raise TypeError("Solo se pueden agregar objetos de tipo Mueble")
        self._muebles.append(mueble)

    def listar(self) -> List[Mueble]:
        return list(self._muebles)

    def agrupar_por_tipo(self) -> Dict[str, List[Mueble]]:
        """Devuelve los muebles agrupados por nombre de clase."""
        grupos: Dict[str, List[Mueble]] = {}
        for mueble in self._muebles:
            tipo = type(mueble).__name__
            grupos.setdefault(tipo, []).append(mueble)
        return grupos

    def mueble_mas_caro(self) -> Mueble | None:
        if not self._muebles:
            return None
        return max(self._muebles, key=lambda m: m.calcular_precio())

    def mueble_mas_barato(self) -> Mueble | None:
        if not self._muebles:
            return None
        return min(self._muebles, key=lambda m: m.calcular_precio())

    def resumen(self) -> str:
        grupos = self.agrupar_por_tipo()
        lineas = [f"=== {self._nombre} ===", f"Total de productos: {self.total}"]
        for tipo, muebles in grupos.items():
            lineas.append(f"  {tipo}: {len(muebles)} unidad(es)")
        return "\n".join(lineas)

    def __len__(self) -> int:
        return self.total

    def __str__(self) -> str:
        return f"Catálogo '{self._nombre}' ({self.total} productos)"
