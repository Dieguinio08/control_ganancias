from datetime import date
from django.test import TestCase

from deducciones.exceptions import DeduccionInexistenteException, DeduccionPeriodoException
from deducciones.management.commands.init_deducciones import Command as CommandDeducciones
from deducciones.management.commands.init_tablas_d import Command as CommandTablasD
from deducciones.utils.deducciones import get_deduccion_periodo


class CalculosTesting(TestCase):
    """ Testing de Cálculos de Ganancias """
    @classmethod
    def setUpClass(cls):
        my_command_deducciones = CommandDeducciones()
        my_command_deducciones.handle()
        my_command = CommandTablasD()
        my_command.handle()
        super().setUpClass()

    def test_deduccion_hijo_ok_1(self):
        periodo = date(2023, 1, 1)
        deduccion_resultante = get_deduccion_periodo('CF', '3', periodo)
        self.assertEqual(deduccion_resultante, 17696.36)

    def test_deduccion_hijo_ok_2(self):
        periodo = date(2023, 7, 1)
        deduccion_resultante = get_deduccion_periodo('CF', '3', periodo)
        self.assertEqual(deduccion_resultante, 123874.55)

    def test_deduccion_hijo_ok_3(self):
        periodo = date(2023, 7, 1)
        deduccion_resultante = get_deduccion_periodo('CF', '30', periodo)
        self.assertEqual(deduccion_resultante, 123874.55)

    def test_deduccion_conyuge(self):
        periodo = date(2023, 6, 1)
        deduccion_resultante = get_deduccion_periodo('CF', '1', periodo)
        self.assertEqual(deduccion_resultante, 210544.12)

    def test_deduccion_indumentaria(self):
        periodo = date(2023, 6, 1)
        deduccion_resultante = get_deduccion_periodo('DE', '21', periodo, 9999999.99)
        self.assertEqual(deduccion_resultante, 9999999.99)

    def test_seguro_vida(self):
        periodo = date(2023, 6, 1)
        deduccion_resultante = get_deduccion_periodo('DE', '2', periodo, 99999.99)
        self.assertEqual(deduccion_resultante, 42921.24)

    def test_credito_hipotecario(self):
        periodo = date(2023, 6, 1)
        deduccion_resultante = get_deduccion_periodo('DE', '4', periodo, 99999.99)
        self.assertEqual(deduccion_resultante, 20000)

    def test_serv_educativos(self):
        periodo = date(2023, 6, 1)
        deduccion_resultante = get_deduccion_periodo('DE', '32', periodo, 99999.99)
        self.assertEqual(deduccion_resultante, 90336.64)

    def test_deduccion_no_configurada_1(self):
        periodo = date(2023, 6, 1)
        deduccion_tipo = 'CF'
        codigo_siradig = '99'
        self.assertRaisesMessage(
            DeduccionInexistenteException,
            f'Deduccion {deduccion_tipo} - {codigo_siradig} no configurada',
            get_deduccion_periodo, deduccion_tipo, codigo_siradig, periodo
        )

    def test_deduccion_no_configurada_2(self):
        periodo = date(2023, 6, 1)
        deduccion_tipo = 'DE'
        codigo_siradig = 'xd'
        self.assertRaisesMessage(
            DeduccionInexistenteException,
            f'Deduccion {deduccion_tipo} - {codigo_siradig} no configurada',
            get_deduccion_periodo, deduccion_tipo, codigo_siradig, periodo
        )

    def test_deduccion_wrong_period(self):
        periodo = date(1999, 6, 1)
        deduccion_tipo = 'CF'
        codigo_siradig = '3'
        self.assertRaisesMessage(
            DeduccionPeriodoException,
            f'Deduccion {deduccion_tipo} - {codigo_siradig} no configurada para el período 1999/06',
            get_deduccion_periodo, deduccion_tipo, codigo_siradig, periodo
        )
