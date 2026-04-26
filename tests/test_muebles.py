"""
Pruebas unitarias para las clases de muebles.
Estas pruebas validan el correcto funcionamiento de todos los conceptos OOP implementados.
"""

import pytest
from models.mueble import Mueble
from models.concretos.silla import Silla
from models.concretos.mesa import Mesa
from models.concretos.sofa import Sofa
from models.concretos.sillon import Sillon
from models.concretos.armario import Armario
from models.concretos.cajonera import Cajonera
from models.concretos.cama import Cama
from models.concretos.escritorio import Escritorio
from models.concretos.sofacama import SofaCama
from models.composicion.comedor import Comedor


class TestMuebleBase:
    """
    Pruebas para la clase base abstracta Mueble.
    Valida conceptos de abstracción y encapsulación.
    """
    
    def test_no_puede_instanciar_mueble_directamente(self):
        """Prueba que no se puede instanciar la clase abstracta Mueble directamente."""
        with pytest.raises(TypeError):
            mueble = Mueble("Test", "Madera", "Café", 100.0)


class TestSilla:
    """
    Pruebas para la clase Silla.
    Valida herencia, polimorfismo y encapsulación.
    """
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.silla_basica = Silla(
            nombre="Silla Básica",
            material="Madera",
            color="Café",
            precio_base=150.0,
            tiene_respaldo=True
        )

        self.silla_oficina = Silla(
            nombre="Silla Oficina",
            material="Metal",
            color="Negro",
            precio_base=300.0,
            tiene_respaldo=True,
            material_tapizado="cuero",
            altura_regulable=True,
            tiene_ruedas=True
        )
    
    def test_creacion_silla_basica(self):
        """Prueba la creación correcta de una silla básica."""
        assert self.silla_basica.nombre == "Silla Básica"
        assert self.silla_basica.material == "Madera"
        assert self.silla_basica.color == "Café"
        assert self.silla_basica.precio_base == 150.0
        assert self.silla_basica.capacidad_personas == 1
        assert self.silla_basica.tiene_respaldo == True
        assert self.silla_basica.material_tapizado == None
    
    def test_calculo_precio_silla_basica(self):
        """Prueba el cálculo de precio para silla básica."""
        precio = self.silla_basica.calcular_precio()

        # El precio debe incluir el precio base + factor de comodidad por respaldo
        # Precio base: 150.0
        # Factor comodidad con respaldo: 1.2 (150.0 * 1.2 = 180.0)
        assert precio == 180.0
    
    def test_calculo_precio_silla_oficina(self):
        """Prueba el cálculo de precio para silla de oficina con todas las características."""
        precio = self.silla_oficina.calcular_precio()
        
        # Precio base: 300.0
        # Factor comodidad: 1.0 + 0.2 (respaldo) + 0.3 (cuero) = 1.5
        # Subtotal: 300 * 1.5 = 450
        # Altura regulable: +20
        # Ruedas: +15
        # Total: 485
        assert precio == 485.0
    
    def test_es_silla_oficina(self):
        """Prueba la lógica de identificación de silla de oficina."""
        assert self.silla_basica.es_silla_oficina() == False
        assert self.silla_oficina.es_silla_oficina() == True
    
    def test_regular_altura_silla_sin_mecanismo(self):
        """Prueba que las sillas sin altura regulable no pueden ajustarse."""
        resultado = self.silla_basica.regular_altura(50)
        assert "no tiene altura regulable" in resultado
    
    def test_regular_altura_silla_con_mecanismo(self):
        """Prueba la regulación de altura en sillas que lo permiten."""
        resultado = self.silla_oficina.regular_altura(50)
        assert "Altura de la silla regulada a 50 cm" in resultado
    
    def test_validaciones_setter(self):
        """Prueba las validaciones en los setters."""

        with pytest.raises(ValueError):
            self.silla_basica.nombre = ""

        with pytest.raises(ValueError):
            self.silla_basica.precio_base = -100

        with pytest.raises(ValueError):
            self.silla_basica.capacidad_personas = 0
    
    def test_obtener_descripcion(self):
        """Prueba que la descripción contenga información relevante."""
        descripcion = self.silla_basica.obtener_descripcion()
        assert "Silla Básica" in descripcion
        assert "Madera" in descripcion
        assert "Café" in descripcion
    
    def test_polimorfismo_herencia(self):
        """Prueba que la silla implementa correctamente los métodos abstractos."""

        # Debe poder llamarse como Mueble (polimorfismo)
        from models.categorias.asientos import Asiento

        assert isinstance(self.silla_basica, Asiento)
        assert hasattr(self.silla_basica, 'calcular_precio')
        assert hasattr(self.silla_basica, 'obtener_descripcion')

        # Los métodos deben retornar valores válidos
        precio = self.silla_basica.calcular_precio()
        assert isinstance(precio, (int, float))
        assert precio > 0

        descripcion = self.silla_basica.obtener_descripcion()
        assert isinstance(descripcion, str)
        assert len(descripcion) > 0


class TestSofaCama:
    """
    Pruebas para la clase SofaCama.
    Valida herencia múltiple y resolución MRO.
    """
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""
        self.sofacama = SofaCama(
            nombre="SofaCama Deluxe",
            material="Tela",
            color="Beige",
            precio_base=1000.0,
            capacidad_personas=3,
            material_tapizado="tela",
            tamaño_cama="matrimonial",
            incluye_colchon=True,
            mecanismo_conversion="plegable"
        )
    
    def test_creacion_sofacama(self):
        """Prueba la creación correcta del sofá-cama."""
        assert self.sofacama.nombre == "SofaCama Deluxe"
        assert self.sofacama.capacidad_personas == 3
        assert self.sofacama.tamaño_cama == "matrimonial"
        assert self.sofacama.incluye_colchon == True
        assert self.sofacama.mecanismo_conversion == "plegable"
        assert self.sofacama.modo_actual == "sofa"
    
    def test_conversion_modos(self):
        """Prueba la conversión entre modos sofá y cama."""
        # Inicialmente debe estar en modo sofá
        assert self.sofacama.modo_actual == "sofa"

        # Convertir a cama
        resultado = self.sofacama.convertir_a_cama()
        assert "convertido a cama" in resultado.lower()
        assert self.sofacama.modo_actual == "cama"

        # Intentar convertir a cama nuevamente
        resultado2 = self.sofacama.convertir_a_cama()
        assert "ya está en modo cama" in resultado2.lower()

        # Convertir de vuelta a sofá
        resultado3 = self.sofacama.convertir_a_sofa()
        assert "convertida a sofá" in resultado3.lower()
        assert self.sofacama.modo_actual == "sofa"
    
    def test_calculo_precio_dual(self):
        """Prueba el cálculo de precio considerando funcionalidad dual."""
        precio = self.sofacama.calcular_precio()
        
        # Precio base sofá: 1000 * factor comodidad (1.3) = 1300
        # Funcionalidad dual: 1300 * 1.5 = 1950
        # Mecanismo: +100
        # Colchón: +300
        # Total: 2350
        assert precio == 2350.0
    
    def test_capacidad_total(self):
        """Prueba las capacidades en ambos modos."""
        capacidades = self.sofacama.obtener_capacidad_total()
        assert capacidades["sofa"] == 3
        assert capacidades["cama"] == 2  # matrimonial
    
    def test_herencia_multiple_mro(self):
        """Prueba que la herencia múltiple funciona correctamente."""
        from models.concretos.sofa import Sofa
        from models.concretos.cama import Cama

        assert isinstance(self.sofacama, Sofa)
        assert isinstance(self.sofacama, Cama)

        # Verificar que tiene métodos de ambas clases padre
        assert hasattr(self.sofacama, 'convertir_a_cama')
        assert hasattr(self.sofacama, 'convertir_a_sofa')
        assert hasattr(self.sofacama, 'calcular_precio')
        assert hasattr(self.sofacama, 'obtener_descripcion')


class TestComedor:
    """
    Pruebas para la clase Comedor.
    Valida composición y agregación.
    """
    
    def setup_method(self):
        """Configuración que se ejecuta antes de cada test."""

        # Crear instancias para composición
        self.mesa = Mesa(
            nombre="Mesa Familiar",
            material="Madera",
            color="Roble",
            precio_base=500.0,
            forma="rectangular",
            capacidad_personas=6
        )

        self.silla1 = Silla("Silla 1", "Madera", "Roble", 120.0, True)
        self.silla2 = Silla("Silla 2", "Madera", "Roble", 120.0, True)

        self.comedor = Comedor(
            nombre="Comedor Familiar",
            mesa=self.mesa,
            sillas=[self.silla1, self.silla2]
        )
    
    def test_creacion_comedor(self):
        """Prueba la creación correcta del comedor con composición."""

        # Implementar test de composición
        assert self.comedor.nombre == "Comedor Familiar"
        assert self.comedor.mesa == self.mesa
        assert len(self.comedor.sillas) == 2
        assert self.silla1 in self.comedor.sillas
        assert self.silla2 in self.comedor.sillas
    
    def test_agregar_silla(self):
        """Prueba agregar sillas al comedor."""
        silla_nueva = Silla("Silla Nueva", "Madera", "Roble", 120.0, True)

        resultado = self.comedor.agregar_silla(silla_nueva)
        assert "exitosamente" in resultado.lower()
        assert len(self.comedor.sillas) == 3
        assert silla_nueva in self.comedor.sillas
    
    def test_agregar_objeto_invalido(self):
        """Prueba que no se pueden agregar objetos que no sean sillas."""
        mesa_invalida = Mesa("Mesa Invalida", "Madera", "Roble", 300.0, "rectangular", 4)
        resultado = self.comedor.agregar_silla(mesa_invalida)
        assert "Solo se pueden agregar objetos de tipo Silla" in resultado
    
    def test_quitar_silla(self):
        """Prueba quitar sillas del comedor."""
        resultado = self.comedor.quitar_silla()
        assert "removida del comedor" in resultado
        assert len(self.comedor.sillas) == 1
    
    def test_calculo_precio_total(self):
        """Prueba el cálculo del precio total del comedor."""
        precio_total = self.comedor.calcular_precio_total()

        # Mesa: 500 * (1 + 5*0.1) * 1.2 (madera) = 500 * 1.5 * 1.2 = 900
        # Sillas: 2 * (120 * 1.2) = 288
        # Total: 1188 (sin descuento, menos de 4 sillas)
        assert precio_total == 1188.0
    
    def test_descuento_set_completo(self):
        """Prueba el descuento por set completo (4+ sillas)."""
        # Agregar más sillas para alcanzar el descuento
        silla3 = Silla("Silla 3", "Madera", "Roble", 120.0, True)
        silla4 = Silla("Silla 4", "Madera", "Roble", 120.0, True)
        
        self.comedor.agregar_silla(silla3)
        self.comedor.agregar_silla(silla4)
        
        precio_con_descuento = self.comedor.calcular_precio_total()
        
        # Precio sin descuento: 900 (mesa) + 4 * 144 (sillas) = 900 + 576 = 1476
        # Con descuento 5%: 1476 * 0.95 = 1402.2
        assert precio_con_descuento == 1402.2
    
    def test_descripcion_completa(self):
        """Prueba la generación de descripción completa."""
        descripcion = self.comedor.obtener_descripcion_completa()
        assert "COMEDOR FAMILIAR" in descripcion
        assert "MESA:" in descripcion
        assert "SILLAS (2 unidades):" in descripcion
        assert "PRECIO TOTAL:" in descripcion
    
    def test_resumen_estadistico(self):
        """Prueba la generación de resumen estadístico."""
        resumen = self.comedor.obtener_resumen()
        assert resumen["nombre"] == "Comedor Familiar"
        assert resumen["total_muebles"] == 3  # mesa + 2 sillas
        assert resumen["capacidad_personas"] == 2
        assert isinstance(resumen["precio_total"], float)
    
    def test_len_comedor(self):
        """Prueba el método __len__ del comedor."""
        assert len(self.comedor) == 2


class TestConceptosOOPGenerales:
    """
    Pruebas que validan conceptos generales de OOP aplicados en todo el sistema.
    """
    
    def test_polimorfismo_general(self):
        """Prueba que diferentes tipos de muebles implementan polimorfismo correctamente."""
        muebles = [
            Silla("Silla Test", "Madera", "Café", 150.0, True),
            Mesa("Mesa Test", "Madera", "Roble", 500.0, "rectangular", 4),
            Sofa("Sofa Test", "Tela", "Azul", 800.0, 3, "tela")
        ]
        
        for mueble in muebles:
            assert hasattr(mueble, 'calcular_precio')
            assert hasattr(mueble, 'obtener_descripcion')
            precio = mueble.calcular_precio()
            descripcion = mueble.obtener_descripcion()
            assert isinstance(precio, (int, float))
            assert isinstance(descripcion, str)
    
    def test_encapsulacion_general(self):
        """Prueba que la encapsulación funciona correctamente."""
        silla = Silla("Silla Test", "Madera", "Café", 150.0, True)
        
        # Acceso a través de propiedades (encapsulación)
        assert silla.nombre == "Silla Test"
        assert silla.material == "Madera"
        
        # Validación de setters
        with pytest.raises(ValueError):
            silla.nombre = ""
        with pytest.raises(ValueError):
            silla.precio_base = -50
    
    def test_herencia_jerarquia(self):
        """Prueba que la jerarquía de herencia funciona correctamente."""
        from models.categorias.asientos import Asiento
        from models.categorias.almacenamiento import Almacenamiento
        from models.categorias.superficies import Superficies
        
        silla = Silla("Silla Test", "Madera", "Café", 150.0, True)
        mesa = Mesa("Mesa Test", "Madera", "Roble", 500.0, "rectangular", 4)
        armario = Armario("Armario Test", "Madera", "Roble", 1200.0, 3, 2, True)
        
        # Verificar jerarquía
        assert isinstance(silla, Asiento)
        assert isinstance(mesa, Superficies)
        assert isinstance(armario, Almacenamiento)
        
        # Todos heredan de Mueble
        assert isinstance(silla, Mueble)
        assert isinstance(mesa, Mueble)
        assert isinstance(armario, Mueble)


# Agregar fixture para datos de prueba si es necesario
@pytest.fixture
def muebles_de_prueba():
    """Fixture que proporciona muebles de prueba para múltiples tests."""
    return {
        'silla_basica': Silla("Silla Test", "Madera", "Café", 100.0, True),
        'mesa_basica': Mesa("Mesa Test", "Madera", "Roble", 300.0, "rectangular", 4),
        'sofacama': SofaCama("SofaCama Test", "Tela", "Gris", 800.0)
    }


class TestIntegracion:
    """
    Pruebas de integración que validan el funcionamiento conjunto de múltiples clases.
    """
    
    def test_creacion_tienda_completa(self):
        """Prueba la creación de una tienda con múltiples tipos de muebles."""
        from services.tienda import TiendaMuebles
        from models.concretos.armario import Armario
        from models.concretos.cama import Cama
        from models.concretos.sofacama import SofaCama
        from models.composicion.comedor import Comedor

        tienda = TiendaMuebles("Tienda Integración")

        # Crear y agregar muebles variados
        silla = Silla("Silla Oak", "Madera", "Roble", 180.0, True, "tela")
        mesa = Mesa("Mesa Familiar", "Madera", "Roble", 600.0, "rectangular", 6)
        sofa = Sofa("Sofá 3P", "Tela", "Gris", 900.0, 3, True, "tela", True)
        armario = Armario("Armario 3P", "Madera", "Blanco", 700.0, 3, 2, True)
        cama = Cama("Cama King", "Madera", "Nogal", 1200.0, "king", True, True)
        sofacama = SofaCama("SofaCama", "Tela", "Beige", 1000.0)

        for m in [silla, mesa, sofa, armario, cama, sofacama]:
            resultado = tienda.agregar_mueble(m)
            assert "exitosamente" in resultado.lower()

        assert tienda.total_muebles == 6

        # Agregar comedor
        comedor = Comedor("Set Familiar", mesa, [silla])
        tienda.agregar_comedor(comedor)
        assert tienda.total_comedores == 1

        # Búsquedas
        assert len(tienda.buscar_muebles_por_nombre("Silla")) == 1
        assert len(tienda.filtrar_por_material("Madera")) >= 1
        assert len(tienda.obtener_muebles_por_tipo(Silla)) == 1

        # Estadísticas
        stats = tienda.obtener_estadisticas()
        assert stats["total_muebles"] == 6
        assert stats["valor_inventario"] > 0

        # Reporte
        reporte = tienda.generar_reporte_inventario()
        assert "Tienda Integración" in reporte


if __name__ == "__main__":
    # Configurar ejecución de pruebas
    pytest.main([__file__, "-v"])

