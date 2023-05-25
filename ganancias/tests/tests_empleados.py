from django.contrib.auth.models import User
from django.test import Client, TestCase

from ganancias.exceptions import CuitValidationException, NameValidationException
from ganancias.models import Empleado, Empresa


class EmpleadoTesting(TestCase):
    """ Testing para Empleado
    """
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create(username='testuser', password='12345')
        self.empresa = Empresa.objects.create(name='Empleado 1', cuit='30999999991', user=self.user)

    def test_create_empleado_ok(self):
        expected_value = f'Empleado 1 - L.1: {self.empresa}'
        this_empleado = Empleado.objects.create(leg=1, empresa=self.empresa, name='Empleado 1', cuil='20999999991')
        self.assertTrue(isinstance(this_empleado, Empleado))
        self.assertEqual(str(this_empleado), expected_value)

    def test_create_empleado_long_name(self):
        long_name = "a" * 121
        with self.assertRaisesMessage(NameValidationException, "El nombre es demasiado largo"):
            Empleado.objects.create(leg=1, empresa=self.empresa, name=long_name, cuil='20999999991')

    def test_create_empleado_empty_name(self):
        with self.assertRaisesMessage(NameValidationException, "El nombre debe ser una cadena de texto"):
            Empleado.objects.create(leg=1, empresa=self.empresa, name='', cuil='20999999991')

    def test_create_empleado_wrong_type_name(self):
        with self.assertRaisesMessage(NameValidationException, "El nombre debe ser una cadena de texto"):
            Empleado.objects.create(leg=1, empresa=self.empresa, name=['Nombre en lista'], cuil='20999999991')

    def test_create_empleado_long_cuil(self):
        with self.assertRaisesMessage(CuitValidationException, "El CUIL debe tener 11 caracteres"):
            Empleado.objects.create(leg=1, empresa=self.empresa, name="Empleado 1", cuil='123456789012')

    def test_create_empleado_short_cuil(self):
        with self.assertRaisesMessage(CuitValidationException, "El CUIL debe tener 11 caracteres"):
            Empleado.objects.create(leg=1, empresa=self.empresa, name="Empleado 1", cuil='1234567890')

    def test_create_empresa_not_numeric_cuil(self):
        with self.assertRaisesMessage(CuitValidationException, "El CUIL debe contener sólo valores numéricos"):
            Empleado.objects.create(leg=1, empresa=self.empresa, name="Empleado 1", cuil='30a30002012')

    def test_create_empleado_empty_cuit(self):
        with self.assertRaisesMessage(CuitValidationException, "El CUIL debe tener 11 caracteres"):
            Empleado.objects.create(leg=1, empresa=self.empresa, name="Empleado 1", cuil='')
