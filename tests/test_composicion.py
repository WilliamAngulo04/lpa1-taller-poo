"""
Pruebas unitarias para las clases de composición.
"""

import pytest
from models.concretos.mesa import Mesa
from models.concretos.silla import Silla
from models.composicion.comedor import Comedor


class TestComedorCreacion:
    """Pruebas de creación y atributos básicos del Comedor."""

    def setup_method(self):
        self.mesa = Mesa("Mesa Test", "Madera", "Roble", 400.0, "rectangular", 4)
        self.silla_a = Silla("Silla A", "Madera", "Roble", 100.0, True)
        self.silla_b = Silla("Silla B", "Madera", "Roble", 100.0, True)

    def test_comedor_sin_sillas(self):
        comedor = Comedor("Vacío", self.mesa)
        assert comedor.nombre == "Vacío"
        assert len(comedor) == 0
        assert comedor.sillas == []

    def test_comedor_con_sillas_iniciales(self):
        comedor = Comedor("Lleno", self.mesa, [self.silla_a, self.silla_b])
        assert len(comedor) == 2

    def test_str_comedor(self):
        comedor = Comedor("Familiar", self.mesa, [self.silla_a])
        texto = str(comedor)
        assert "Familiar" in texto
        assert "1" in texto

    def test_sillas_retorna_copia(self):
        """Modificar la lista devuelta no debe afectar al comedor."""
        comedor = Comedor("Test", self.mesa, [self.silla_a])
        copia = comedor.sillas
        copia.clear()
        assert len(comedor) == 1


class TestComedorOperaciones:
    """Pruebas de agregar, quitar sillas y cálculo de precios."""

    def setup_method(self):
        self.mesa = Mesa("Mesa Op", "Madera", "Café", 500.0, "rectangular", 6)
        self.comedor = Comedor("Op", self.mesa)

    def test_agregar_silla_valida(self):
        silla = Silla("S1", "Madera", "Café", 120.0, True)
        resultado = self.comedor.agregar_silla(silla)
        assert "exitosamente" in resultado.lower()
        assert len(self.comedor) == 1

    def test_agregar_objeto_no_silla(self):
        mesa_extra = Mesa("Extra", "Metal", "Gris", 200.0, "redonda", 2)
        resultado = self.comedor.agregar_silla(mesa_extra)
        assert "Solo se pueden agregar objetos de tipo Silla" in resultado
        assert len(self.comedor) == 0

    def test_quitar_silla_existente(self):
        silla = Silla("S1", "Madera", "Café", 120.0, True)
        self.comedor.agregar_silla(silla)
        resultado = self.comedor.quitar_silla()
        assert "removida" in resultado.lower()
        assert len(self.comedor) == 0

    def test_quitar_silla_comedor_vacio(self):
        resultado = self.comedor.quitar_silla()
        assert "no hay sillas" in resultado.lower()

    def test_precio_total_solo_mesa(self):
        precio = self.comedor.calcular_precio_total()
        assert precio == self.mesa.calcular_precio()

    def test_precio_total_con_sillas(self):
        silla = Silla("S1", "Madera", "Café", 120.0, True)
        self.comedor.agregar_silla(silla)
        esperado = round(self.mesa.calcular_precio() + silla.calcular_precio(), 2)
        assert self.comedor.calcular_precio_total() == esperado

    def test_descuento_4_o_mas_sillas(self):
        for i in range(4):
            self.comedor.agregar_silla(Silla(f"S{i}", "Madera", "Café", 100.0, True))
        precio_bruto = self.mesa.calcular_precio() + 4 * Silla("x", "Madera", "Café", 100.0, True).calcular_precio()
        esperado = round(precio_bruto * 0.95, 2)
        assert self.comedor.calcular_precio_total() == esperado


class TestComedorResumen:
    """Pruebas de descripción y resumen estadístico."""

    def setup_method(self):
        mesa = Mesa("Mesa R", "Vidrio", "Negro", 600.0, "redonda", 4)
        sillas = [Silla(f"SR{i}", "Metal", "Negro", 130.0, True) for i in range(2)]
        self.comedor = Comedor("Moderno", mesa, sillas)

    def test_descripcion_completa_contiene_elementos(self):
        desc = self.comedor.obtener_descripcion_completa()
        assert "MODERNO" in desc
        assert "MESA:" in desc
        assert "SILLAS (2 unidades):" in desc
        assert "PRECIO TOTAL:" in desc

    def test_resumen_contiene_campos_esperados(self):
        resumen = self.comedor.obtener_resumen()
        assert resumen["nombre"] == "Moderno"
        assert resumen["total_muebles"] == 3  # 1 mesa + 2 sillas
        assert resumen["capacidad_personas"] == 2
        assert "precio_total" in resumen
        assert "materiales_utilizados" in resumen
        assert isinstance(resumen["materiales_utilizados"], list)
