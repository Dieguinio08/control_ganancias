
TOPES = {
    2022: {
        'MNI': {
            'importe': 252564.84,
            'tipo': 'anual'
        },
        'MNI Mes': {
            'importe': 252564.84,
        },
        '40pMNI': {
            'importe': 101025.94,
        },
        'Gastos Sepelio': {
            'importe': 996.23,
            'tipo': 'anual'
        },
        'Crédito Hipotecario': {
            'importe': 20000,
            'tipo': 'anual'
        },
        'Seguros': {
            'importe': 42921.24,
            'tipo': 'anual'
        },
        'GN5': {
            'importe': 9999999999.99,
        }
    },
    2023: {
        'MNI': {
            'importe': 451683.19,
            'tipo': 'anual'
        },
        'MNI Mes': {
            'importe': 451683.19,
        },
        '40pMNI': {
            'importe': 180673.28,
        },
        'Gastos Sepelio': {
            'importe': 996.23,
            'tipo': 'anual'
        },
        'Crédito Hipotecario': {
            'importe': 20000,
            'tipo': 'anual'
        },
        'Seguros': {
            'importe': 42921.24,
            'tipo': 'anual'
        },
        'GN5': {
            'importe': 9999999999.99,
        }
    },
}


DEDUCCIONES = {
    'deduccion': {
        '1': {'name': 'Cuotas Médico-Asistenciales',
              'tope': 'GN5'},
        '2': {'name': 'Primas de Seguro para el caso de muerte',
              'tope': 'Seguros',
              'periodicidad': 'AN'},
        '3': {'name': 'Donaciones',
              'tope': 'GN5'},
        '4': {'name': 'Intereses Préstamo Hipotecario',
              'tope': 'Crédito Hipotecario'},
        '5': {'name': 'Gastos de Sepelio',
              'tope': 'Gastos Sepelio'},
        '7': {'name': 'Gastos Médicos y Paramédicos',
              'tope': 'GN5',
              'periodicidad': 'AN'},
        '8': {'name': 'Deducción del Personal Doméstico',
              'tope': 'MNI'},
        '9': {'name': 'Aporte a Sociedades de Garantía Recíproca'},
        '10': {'name': 'Vehiculos de Corredores y Viajantes de Comercio'},
        '11': {'name': 'Gastos de Representación e Intereses de Corredores y Viajantes de Comercio'},
        '21': {'name': 'Gastos de Adquisición de Indumentaria y Equipamiento uso Lugar de Trabajo'},
        '22': {'name': 'Alquiler de Inmuebles destinados a casa habitación',
               'tope': 'MNI'},
        '23': {'name': 'Primas de Ahorro correspondientes a Seguros Mixtos',
               'tope': 'Seguros',
               'periodicidad': 'AN'},
        '24': {'name': 'Aportes correspondientes a Planes de Seguro de Retiro Privados',
               'tope': 'Seguros',
               'periodicidad': 'AN'},
        '25': {'name': 'Adquisición de Cuotapartes de Fondos Comunes de Inversión con fines de retiro',
               'tope': 'Seguros',
               'periodicidad': 'AN'},
        # Combina ambos tipos de deducciones (32-1 y 32-2) por motivos de tope
        '32': {'name': 'Herramientas educativas - Servicios con fines educativos',
               'tope': '40pMNI',
               },
        '99-1': {'name': 'Aportes para fondos de Jubilación, Retiros, Pensiones o Subsidios destinados al ANSES'},
        '99-2': {'name': 'Cajas Provinciales o Municipales'},
        '99-3': {'name': 'Impuesto sobre los Créditos y Débitos en Cuenta Bancaria sin CBU'},
        '99-4': {'name': 'Beneficios Derivados de Regímenes tratamientos Preferenciales Mediante Deducciones'},
        '99-5': {'name': 'Beneficios Derivados de Regímenes tratamientos Preferenciales No Mediante Deducciones'},
        '99-6': {'name': 'Actores - Retribuciones Abonadas a Representantes - R.G.N° 2442/08'},
        '99-7': {'name': 'Cajas Complementarias de Previsión'},
        '99-8': {'name': 'Fondos Compensadores de Previsión'},
        '99-9': {'name': 'Otros'},
    },
    'cargaFamilia': {
        '1': 'Cónyuge',
        '3': 'Hijo/a Menor de 18 Años',
        '30': 'Hijastro/a Menor de 18 Años',
        '31': 'Hijo/a Incapacitado para el Trabajo',
        '32': 'Hijastro/a Incapcacitado para el Trabajo',
        '51': 'Union convivencial',
    },
    'retPerPago': {
        '6': 'Impuestos sobre Créditos y Débitos en cuenta Bancaria',
        '12': 'Retenciones y Percepciones Aduaneras',
        '13': 'Pago a Cuenta - Compras en el Exterior',
        '14': 'Impuesto sobre los Movimientos de Fondos Propios o de Terceros',
        '15': 'Pago a Cuenta - Compra de Paquetes Turísticos',
        '16': 'Pago a Cuenta - Compra de Pasajes',
        '17': 'Pago a Cuenta - Compra de Moneda Extranjera para Turismo / Transf. al Exterior',
        '18': 'Pago a Cuenta - Adquisición de moneda extranjera para tenencia de billetes extranjeros',
        '19': 'Pago a Cuenta - Compra de Paquetes Turísticos en efectivo',
        '20': 'Pago a Cuenta - Compra de Pasajes en efectivo',
        '27': 'Pago a Cuenta - RG 4815 - Ley 27541 - Art. 35 inc. a)',
        '28': 'Pago a Cuenta - RG 4815 - Ley 27541 - Art. 35 inc. b)',
        '29': 'Pago a Cuenta - RG 4815 - Ley 27541 - Art. 35 inc. c)',
        '30': 'Pago a Cuenta - RG 4815 - Ley 27541 - Art. 35 inc. e)',
        '31': 'Pago a Cuenta - RG 4815 - Ley 27541 - Art. 35 inc. e)',
    },
    'manual': {
        '1': 'Ganancia No Imponible',
        '2': 'Deducción Especial [art 30º, inciso c), Apartado 2]',
        '10': 'Ded Especial Incrementada Rango 1',
        '12': 'Ded Especial Incrementada Rango 2 - (Tabla Anexo IV)',
    }
}

DEDUCCIONES_ANUALES = {
    'deduccion': {
        '2': 'Primas de Seguro para el caso de muerte',
        '7': 'Gastos Médicos y Paramédicos',
        '23': 'Primas de Ahorro correspondientes a Seguros Mixtos',
        '24': 'Aportes correspondientes a Planes de Seguro de Retiro Privados',
        '25': 'Adquisición de Cuotapartes de Fondos Comunes de Inversión con fines de retiro',
    },
    'retPerPago': {
        '6': 'Impuestos sobre Créditos y Débitos en cuenta Bancaria',
        '12': 'Retenciones y Percepciones Aduaneras',
        '13': 'Pago a Cuenta - Compras en el Exterior',
        '14': 'Impuesto sobre los Movimientos de Fondos Propios o de Terceros',
        '15': 'Pago a Cuenta - Compra de Paquetes Turísticos',
        '16': 'Pago a Cuenta - Compra de Pasajes',
        '17': 'Pago a Cuenta - Compra de Moneda Extranjera para Turismo / Transf. al Exterior',
        '18': 'Pago a Cuenta - Adquisición de moneda extranjera para tenencia de billetes extranjeros',
        '19': 'Pago a Cuenta - Compra de Paquetes Turísticos en efectivo',
        '20': 'Pago a Cuenta - Compra de Pasajes en efectivo',
        '27': 'Pago a Cuenta - RG 4815 - Ley 27541 - Art. 35 inc. a)',
        '28': 'Pago a Cuenta - RG 4815 - Ley 27541 - Art. 35 inc. b)',
        '29': 'Pago a Cuenta - RG 4815 - Ley 27541 - Art. 35 inc. c)',
        '30': 'Pago a Cuenta - RG 4815 - Ley 27541 - Art. 35 inc. e)',
        '31': 'Pago a Cuenta - RG 4815 - Ley 27541 - Art. 35 inc. e)',
    },
}
