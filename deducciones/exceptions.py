

class DeduccionInexistenteException(Exception):
    """Excepcion para cuando no se encontrar la deducción en la base de datos"""
    pass


class DeduccionPeriodoException(Exception):
    """Excepcion para cuando no se encontrar el período de
    la deducción en la base de datos"""
    pass
