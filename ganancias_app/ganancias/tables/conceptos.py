

APORTES = {
    'jubilacion': {
        'long_name': 'Jubilación',
        'f1357field': 'jubilacion',
    },
    'obra_social': {
        'long_name': 'Obra Social',
        'f1357field': 'obra_social',
    },
    'cuota_sindical': {
        'long_name': 'Cuota Sindical',
        'f1357field': 'cuota_sindical',
    },
    'oe_jubilacion': {
        'long_name': 'Jubilación Otros Empleos',
        'f1357field': 'oe_jubilacion',
    },
    'oe_obra_social': {
        'long_name': 'Obra Social Otros Empleos',
        'f1357field': 'oe_obra_social',
    },
    'oe_cuota_sindical': {
        'long_name': 'Cuota Sindical Otros Empleos',
        'f1357field': 'oe_cuota_sindical',
    },
}


CONCEPTOS = {
    'Remuneración bruta gravada': {'f1357field': 'rem_gravada'},
    'No Remunerativo bruto gravada': {
        'f1357field': 'rem_gravada',
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
    'Gastos Movilidad': {'f1357field': 'viaticos_gravado'},
    'Gastos Viaticos': {'f1357field': 'viaticos_gravado'},
    'Gastos otras compensaciones análogas': {'f1357field': 'viaticos_gravado'},
    'Gastos Movilidad Larga Distancia': {'f1357field': 'viaticos_gravado'},
    'Gastos Viaticos Larga Distancia': {'f1357field': 'viaticos_gravado'},
    'Gastos Movilidad Larga Distancia CCT 40/89': {'f1357field': 'viaticos_gravado'},
    'Gastos Viaticos Larga Distancia CCT 40/89': {'f1357field': 'viaticos_gravado'},
    'Gastos otras comp analogas Larga Distancia CCT 40/89': {'f1357field': 'viaticos_gravado'},
    'Material didáctico personal docente': {},
    'Bonos de productividad gravados': {
        'habitualidad': 'NH',
    },
    'Fallos de caja gravados': {},
    'Conceptos de similar naturaleza gravados': {},
    'Remuneración exenta o no alcanzada': {
        'f1357field': 'rem_exenta',
        'exento': True,
    },
    'No remunerativo exento o no alcanzado': {
        'f1357field': 'rem_exenta',
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
        'f1357field': 'l27718_exento',
        'exento': True,
    },
    'Bonos de productividad exentos': {
        'f1357field': 'bonos_prod_exento',
        'habitualidad': 'NH',
        'exento': True,
    },
    'Fallos de caja exentos': {
        'f1357field': 'fallos_caja_exento',
        'exento': True,
    },
    'Conceptos de similar naturaleza exentos': {
        'f1357field': 'sim_nat_exento',
        'exento': True,
    },
    'Suplementos particulares artículo 57 de la Ley N° 19.101 exentos': {
        'f1357field': 'l19101_exento',
        'exento': True,
    },
    'Compensación gastos de teletrabajo exentos': {
        'f1357field': 'teletrabajo_exento',
        'habitualidad': 'NH',
        'exento': True,
    },
    'Ajustes períodos anteriores - Remuneración gravada': {
        'f1357field': 'ajuste_per_ant_gravado',
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
    'OE Remuneración bruta gravada': {'others': True, 'f1357field': 'oe_rem_gravada'},
    'OE No Remunerativo bruto gravada': {
        'f1357field': 'oe_rem_gravada',
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
    'OE Gastos Movilidad y viáticos': {'others': True, 'f1357field': 'oe_viaticos_gravado'},
    'OE Material didáctico personal docente': {'others': True},
    'OE Bonos de productividad gravados': {
        'others': True,
        'habitualidad': 'NH',
    },
    'OE Fallos de caja gravados': {'others': True, 'f1357field': 'oe_fallos_caja_gravado'},
    'OE Conceptos de similar naturaleza gravados': {
        'others': True,
        'f1357field': 'oe_sim_nat_gravado',
    },
    'OE Remuneración exenta o no alcanzada': {
        'f1357field': 'oe_rem_exenta',
        'others': True,
        'exento': True,
    },
    'OE No remunerativo exento o no alcanzado': {
        'f1357field': 'oe_rem_exenta',
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
        'f1357field': 'oe_l27718_exento',
        'others': True,
        'exento': True,
    },
    'OE Bonos de productividad exentos': {
        'f1357field': 'oe_bonos_prod_exento',
        'others': True,
        'habitualidad': 'NH',
        'exento': True,
    },
    'OE Fallos de caja exentos': {
        'f1357field': 'oe_fallos_caja_exento',
        'others': True,
        'exento': True,
    },
    'OE Conceptos de similar naturaleza exentos': {
        'f1357field': 'oe_sim_nat_exento',
        'others': True,
        'exento': True,
    },
    'OE Suplementos particulares artículo 57 de la Ley N° 19.101 exentos': {
        'f1357field': 'oe_l19101_exento',
        'others': True,
        'exento': True,
    },
    'OE Compensación gastos de teletrabajo exentos': {
        'f1357field': 'oe_teletrabajo_exento',
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
