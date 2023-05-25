

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
}
