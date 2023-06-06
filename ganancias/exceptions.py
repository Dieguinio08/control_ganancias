from django.core.exceptions import ValidationError


class NameValidationException(ValidationError):
    pass


class CuitValidationException(ValidationError):
    pass


class GananciaNoCalculadaException(Exception):
    """Excepcion para cuando no se puede calcular la ganancia de un empleado"""
    pass
