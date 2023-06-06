

CONCEPTOS = {
    'Remuneración bruta gravada': {},
    'No Remunerativo bruto gravada': {
        'tipo_concepto': 'NOREM',
    },
    'Retribuciones no habituales gravada': {
        'habitualidad': 'NH',
    },
    'Retribuciones no habituales NR bruto gravada': {
        'tipo_concepto': 'NOREM',
        'habitualidad': 'NH',
    },
    'Horas Extras 50% Ds. Hab': {
        'extras': {
            'tipo': 'HE',
            'porcentaje': 50,
            'dias': 'HAB',
        }
    },
    'Horas Extras 50% Ds. Inhab': {
        'extras': {
            'tipo': 'HE',
            'porcentaje': 50,
            'dias': 'INHAB',
        }
    },
    'Horas Extras 100% Ds. Hab': {
        'extras': {
            'tipo': 'HE',
            'porcentaje': 100,
            'dias': 'INHAB',
        }
    },
    'Gastos Movilidad': {},
    'Gastos Viaticos': {},
    'Gastos otras compensaciones análogas': {},
    'Gastos Movilidad Larga Distancia': {},
    'Gastos Viaticos Larga Distancia': {},
    'Gastos Movilidad Larga Distancia CCT 40/89': {},
    'Gastos Viaticos Larga Distancia CCT 40/89': {},
    'Gastos otras comp analogas Larga Distancia CCT 40/89': {},
    'Material didáctico personal docente': {},
    'Bonos de productividad gravados': {
        'habitualidad': 'NH',
    },
    'Fallos de caja gravados': {},
    'Conceptos de similar naturaleza gravados': {},
    'Remuneración exenta o no alcanzada': {
        'exento': True,
    },
    'No remunerativo exento o no alcanzado': {
        'tipo_concepto': 'NOREM',
        'exento': True,
    },
    'Remuneración No Habitual exenta o no alcanzada': {
        'exento': True,
    },
    'No remunerativo No Habitual exento o no alcanzado': {
        'tipo_concepto': 'NOREM',
        'habitualidad': 'NH',
        'exento': True,
    },
    'Remuneración exenta Ley N° 27.718': {
        'exento': True,
    },
    'Bonos de productividad exentos': {
        'habitualidad': 'NH',
        'exento': True,
    },
    'Fallos de caja exentos': {
        'exento': True,
    },
    'Conceptos de similar naturaleza exentos': {
        'exento': True,
    },
    'Suplementos particulares artículo 57 de la Ley N° 19.101 exentos': {
        'exento': True,
    },
    'Compensación gastos de teletrabajo exentos': {
        'habitualidad': 'NH',
        'exento': True,
    },
    'Ajustes períodos anteriores - Remuneración gravada': {
        'habitualidad': 'NH',
    },
    'Ajustes NR períodos anteriores - No remunerativo gravado': {
        'tipo_concepto': 'NOREM',
        'habitualidad': 'NH',
    },
    'Ajustes períodos anteriores - Remuneración exenta': {
        'exento': True,
        'habitualidad': 'NH',
    },
    'Ajustes NR períodos anteriores - No remunerativo exento': {
        'exento': True,
        'tipo_concepto': 'NOREM',
        'habitualidad': 'NH',
    },
    # Otros Empleos -----------------------------------------------------------
    'OE Remuneración bruta gravada': {'others': True},
    'OE No Remunerativo bruto gravada': {
        'others': True,
        'tipo_concepto': 'NOREM',
    },
    'OE Retribuciones no habituales gravada': {
        'others': True,
        'habitualidad': 'NH',
    },
    'OE Retribuciones no habituales NR bruto gravada': {
        'others': True,
        'tipo_concepto': 'NOREM',
        'habitualidad': 'NH',
    },
    'OE Horas Extras Gravadas': {
        'others': True,
        'extras': {
            'tipo': 'HE',
            'dias': 'READY',
        }
    },
    'OE Horas Extras Exentas': {
        'exento': True,
        'others': True,
        'extras': {
            'tipo': 'HE',
            'dias': 'READY',
        }
    },
    'OE Gastos Movilidad': {'others': True},
    'OE Gastos Viaticos': {'others': True},
    'OE Gastos otras compensaciones análogas': {'others': True},
    'OE Gastos Movilidad Larga Distancia': {'others': True},
    'OE Gastos Viaticos Larga Distancia': {'others': True},
    'OE Gastos Movilidad Larga Distancia CCT 40/89': {'others': True},
    'OE Gastos Viaticos Larga Distancia CCT 40/89': {'others': True},
    'OE Gastos otras comp analogas Larga Distancia CCT 40/89': {'others': True},
    'OE Material didáctico personal docente': {'others': True},
    'OE Bonos de productividad gravados': {
        'others': True,
        'habitualidad': 'NH',
    },
    'OE Fallos de caja gravados': {'others': True},
    'OE Conceptos de similar naturaleza gravados': {'others': True},
    'OE Remuneración exenta o no alcanzada': {
        'others': True,
        'exento': True,
    },
    'OE No remunerativo exento o no alcanzado': {
        'others': True,
        'tipo_concepto': 'NOREM',
        'exento': True,
    },
    'OE Remuneración No Habitual exenta o no alcanzada': {
        'others': True,
        'exento': True,
    },
    'OE No remunerativo No Habitual exento o no alcanzado': {
        'others': True,
        'tipo_concepto': 'NOREM',
        'habitualidad': 'NH',
        'exento': True,
    },
    'OE Remuneración exenta Ley N° 27.718': {
        'others': True,
        'exento': True,
    },
    'OE Bonos de productividad exentos': {
        'others': True,
        'habitualidad': 'NH',
        'exento': True,
    },
    'OE Fallos de caja exentos': {
        'others': True,
        'exento': True,
    },
    'OE Conceptos de similar naturaleza exentos': {
        'others': True,
        'exento': True,
    },
    'OE Suplementos particulares artículo 57 de la Ley N° 19.101 exentos': {
        'others': True,
        'exento': True,
    },
    'OE Compensación gastos de teletrabajo exentos': {
        'others': True,
        'habitualidad': 'NH',
        'exento': True,
    },
    'OE Ajustes períodos anteriores - Remuneración gravada': {
        'others': True,
        'habitualidad': 'NH',
    },
    'OE Ajustes NR períodos anteriores - No remunerativo gravado': {
        'others': True,
        'tipo_concepto': 'NOREM',
        'habitualidad': 'NH',
    },
    'OE Ajustes períodos anteriores - Remuneración exenta': {
        'others': True,
        'exento': True,
        'habitualidad': 'NH',
    },
    'OE Ajustes NR períodos anteriores - No remunerativo exento': {
        'others': True,
        'exento': True,
        'tipo_concepto': 'NOREM',
        'habitualidad': 'NH',
    },
}
