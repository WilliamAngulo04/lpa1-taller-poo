"""
Pruebas unitarias para el servicio TiendaMuebles.
"""

import pytest
from services.tienda import TiendaMuebles
from models.concretos.silla import Silla
from models.concretos.mesa import Mesa
from models.concretos.sofa import Sofa
from models.concretos.armario import Armario
from models.composicion.comedor import Comedor


def _silla(nombre="Silla Test", material="Madera", precio=150.0):
    return Silla(nombre, material, "Café", precio, True)


def _mesa(nombre="Mesa Test", material="Madera", precio=400.0):
    return Mesa(nombre, material, "Roble", precio, "rectangular", 4)


class TestTiendaInventario:
    """Pruebas de gestión del inventario."""

    def setup_method(self):
        self.tienda = TiendaMuebles("Tienda Test")

    def test_nombre_tienda(self):
        assert self.tienda.nombre == "Tienda Test"

    def test_inventario_inicial_vacio(self):
        assert self.tienda.total_muebles == 0

    def test_agregar_mueble_valido(self):
        resultado = self.tienda.agregar_mueble(_silla())
        assert "exitosamente" in resultado.lower()
        assert self.tienda.total_muebles == 1

    def test_agregar_objeto_invalido(self):
        resultado = self.tienda.agregar_mueble("no soy un mueble")
        assert "error" in resultado.lower()
        assert self.tienda.total_muebles == 0

    def test_agregar_comedor(self):
        mesa = _mesa()
        comedor = Comedor("Set", mesa)
        resultado = self.tienda.agregar_comedor(comedor)
        assert "exitosamente" in resultado.lower()
        assert self.tienda.total_comedores == 1

    def test_agregar_objeto_invalido_como_comedor(self):
        resultado = self.tienda.agregar_comedor(_silla())
        assert "error" in resultado.lower()


class TestTiendaBusqueda:
    """Pruebas de búsqueda y filtrado de muebles."""

    def setup_method(self):
        self.tienda = TiendaMuebles("Tienda Búsqueda")
        self.tienda.agregar_mueble(_silla("Silla Clásica", "Madera", 150.0))
        self.tienda.agregar_mueble(_silla("Silla Moderna", "Metal", 200.0))
        self.tienda.agregar_mueble(_mesa("Mesa Grande", "Madera", 500.0))
        self.tienda.agregar_mueble(
            Armario("Armario Roble", "Madera", "Roble", 600.0, 2)
        )

    def test_buscar_por_nombre_exacto(self):
        resultados = self.tienda.buscar_muebles_por_nombre("Silla Clásica")
        assert len(resultados) == 1
        assert resultados[0].nombre == "Silla Clásica"

    def test_buscar_por_nombre_parcial(self):
        resultados = self.tienda.buscar_muebles_por_nombre("Silla")
        assert len(resultados) == 2

    def test_buscar_case_insensitive(self):
        resultados = self.tienda.buscar_muebles_por_nombre("silla")
        assert len(resultados) == 2

    def test_buscar_sin_resultados(self):
        resultados = self.tienda.buscar_muebles_por_nombre("Sofá")
        assert resultados == []

    def test_buscar_nombre_vacio(self):
        assert self.tienda.buscar_muebles_por_nombre("") == []

    def test_filtrar_por_material_madera(self):
        resultados = self.tienda.filtrar_por_material("Madera")
        assert len(resultados) == 3

    def test_filtrar_por_material_metal(self):
        resultados = self.tienda.filtrar_por_material("Metal")
        assert len(resultados) == 1

    def test_filtrar_por_material_inexistente(self):
        assert self.tienda.filtrar_por_material("Plastico") == []

    def test_filtrar_por_material_vacio(self):
        assert self.tienda.filtrar_por_material("") == []

    def test_filtrar_por_precio_rango(self):
        resultados = self.tienda.filtrar_por_precio(100, 300)
        for m in resultados:
            assert 100 <= m.calcular_precio() <= 300

    def test_filtrar_por_precio_sin_limite(self):
        resultados = self.tienda.filtrar_por_precio()
        assert len(resultados) == 4

    def test_obtener_por_tipo(self):
        resultados = self.tienda.obtener_muebles_por_tipo(Silla)
        assert len(resultados) == 2
        for m in resultados:
            assert isinstance(m, Silla)


class TestTiendaVentas:
    """Pruebas del sistema de ventas y descuentos."""

    def setup_method(self):
        self.tienda = TiendaMuebles("Tienda Ventas")
        self.silla = _silla("Mi Silla", "Madera", 200.0)
        self.tienda.agregar_mueble(self.silla)

    def test_venta_exitosa(self):
        venta = self.tienda.realizar_venta(self.silla, "Juan")
        assert "error" not in venta
        assert venta["cliente"] == "Juan"
        assert venta["mueble"] == "Mi Silla"
        assert venta["precio_final"] > 0
        assert self.tienda.total_muebles == 0

    def test_venta_mueble_no_disponible(self):
        otra_silla = _silla("Otra", "Metal", 100.0)
        resultado = self.tienda.realizar_venta(otra_silla, "Ana")
        assert "error" in resultado

    def test_aplicar_descuento_valido(self):
        resultado = self.tienda.aplicar_descuento("silla", 10)
        assert "10%" in resultado

    def test_aplicar_descuento_invalido(self):
        resultado = self.tienda.aplicar_descuento("silla", 150)
        assert "error" in resultado.lower()

    def test_venta_con_descuento_aplicado(self):
        self.tienda.aplicar_descuento("silla", 50)
        precio_original = self.silla.calcular_precio()
        venta = self.tienda.realizar_venta(self.silla, "Carlos")
        assert venta["precio_final"] == round(precio_original * 0.5, 2)
        assert venta["descuento"] == 50.0


class TestTiendaEstadisticas:
    """Pruebas de estadísticas y reportes."""

    def setup_method(self):
        self.tienda = TiendaMuebles("Tienda Stats")
        self.tienda.agregar_mueble(_silla("S1"))
        self.tienda.agregar_mueble(_silla("S2"))
        self.tienda.agregar_mueble(_mesa("M1"))

    def test_calcular_valor_inventario(self):
        valor = self.tienda.calcular_valor_inventario()
        esperado = sum(
            m.calcular_precio() for m in self.tienda._inventario
        )
        assert valor == round(esperado, 2)

    def test_estadisticas_contienen_campos(self):
        stats = self.tienda.obtener_estadisticas()
        assert stats["total_muebles"] == 3
        assert stats["ventas_realizadas"] == 0
        assert "valor_inventario" in stats
        assert "tipos_muebles" in stats

    def test_estadisticas_tipos_muebles(self):
        stats = self.tienda.obtener_estadisticas()
        tipos = stats["tipos_muebles"]
        assert tipos.get("Silla") == 2
        assert tipos.get("Mesa") == 1

    def test_generar_reporte_contiene_info(self):
        reporte = self.tienda.generar_reporte_inventario()
        assert "Tienda Stats" in reporte
        assert "Total de muebles: 3" in reporte
        assert "Silla" in reporte
        assert "Mesa" in reporte
