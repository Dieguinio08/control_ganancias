from datetime import date
from django.test import TestCase

from ganancias.exceptions import DeduccionIncrementadaException, GananciaNoCalculadaException
from ganancias.management.commands.init_tablas import Command
from ganancias.utils.deducciones import get_deduccion_incrementada
from ganancias.utils.ganancias import get_impuesto_determinado


class CalculosTesting(TestCase):
    """ Testing de Cálculos de Ganancias """
    @classmethod
    def setUpClass(cls):
        my_command_t = Command()
        my_command_t.tabla_art_94()
        my_command_t.deduccion_incrementada()
        super().setUpClass()

    def test_calculo_ganancias_ok(self):
        periodo = date(2023, 1, 1)
        ganancias = 1000000.0
        impuesto_determinado = round(get_impuesto_determinado(ganancias, periodo), 2)
        self.assertEqual(impuesto_determinado, 320592.98)

    def test_calculo_ganancias2_ok(self):
        periodo = date(2023, 5, 1)
        ganancias = 200000.0
        impuesto_determinado = round(get_impuesto_determinado(ganancias, periodo), 2)
        self.assertEqual(impuesto_determinado, 16756.89)

    def test_calculo_ganancias_wrong(self):
        periodo = date(2020, 1, 1)
        ganancias = 1000000.0
        self.assertRaisesMessage(
            GananciaNoCalculadaException,
            f'Ganancia {ganancias} no encontrada en la tabla del Art. 94',
            get_impuesto_determinado, ganancias, periodo
        )

    def test_calculo_deduccion_incrementada_ok_1(self):
        periodo = date(2023, 1, 1)
        remuneracion_base = 1000000.0
        deduccion_incrementada = round(get_deduccion_incrementada(remuneracion_base, periodo), 2)
        self.assertEqual(deduccion_incrementada, 0.0)

    def test_calculo_deduccion_incrementada_ok_2(self):
        periodo = date(2023, 1, 1)
        remuneracion_base = 100000.0
        deduccion_incrementada = round(get_deduccion_incrementada(remuneracion_base, periodo), 2)
        self.assertEqual(deduccion_incrementada, 0.0)

    def test_calculo_deduccion_incrementada_ok_3(self):
        periodo = date(2023, 5, 1)
        remuneracion_base = 514000.0
        deduccion_incrementada = round(get_deduccion_incrementada(remuneracion_base, periodo), 2)
        self.assertEqual(deduccion_incrementada, 170925.0)

    def test_calculo_deduccion_incrementada_wrong_1(self):
        periodo = date(2020, 5, 1)
        remuneracion_base = 514000.0
        self.assertRaisesMessage(
            DeduccionIncrementadaException,
            f'Período {periodo.strftime("%Y/%m")} no configurado',
            get_deduccion_incrementada, remuneracion_base, periodo
        )

    def test_calculo_deduccion_incrementada_wrong_2(self):
        periodo = date(2120, 5, 1)
        remuneracion_base = 514000.0
        self.assertRaisesMessage(
            DeduccionIncrementadaException,
            f'Período {periodo.strftime("%Y/%m")} no configurado',
            get_deduccion_incrementada, remuneracion_base, periodo
        )
