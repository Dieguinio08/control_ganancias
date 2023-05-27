

TABLA_ART_94 = {
    2022: [
        (0, 5),
        (97202, 9),
        (194404.01, 12),
        (291606.01, 15),
        (388808.02, 19),
        (583212.02, 23),
        (777616.02, 27),
        (1166424.03, 31),
        (1555232.07, 35),
    ],
    2023: [
        (0, 5),
        (173834.61, 9),
        (347669.22, 12),
        (521503.83, 15),
        (695338.44, 19),
        (1043007.68, 23),
        (1390676.92, 27),
        (2086015.35, 31),
        (2781353.78, 35),
    ]
}

TABLA_ART_30 = {
    2022: {
        'Ganancia no Imponible': {
            'importe': 252564.84,
            'tipo': 'manual',
            'codigo': '1'
        },
        'Deducción Especial - Artículo 30, inciso c)': {
            'importe': 1212311.24,
            'tipo': 'manual',
            'codigo': '2'
        },
        'Cónyuge': {
            'importe': 235457.25,
            'tipo': 'cargaFamilia',
            'codigo': '1'
        },
        'Union Convivencial': {
            'importe': 235457.25,
            'tipo': 'cargaFamilia',
            'codigo': '51'
        },
        'Hijo': {
            'importe': 118741.97,
            'tipo': 'cargaFamilia',
            'codigo': '3'
        },
        'Hijastro': {
            'importe': 118741.97,
            'tipo': 'cargaFamilia',
            'codigo': '30'
        },
        'Hijo con discapacidad': {
            'importe': 237483.94,
            'tipo': 'cargaFamilia',
            'codigo': '31'
        },
        'Hijastro con discapacidad': {
            'importe': 237483.94,
            'tipo': 'cargaFamilia',
            'codigo': '32'
        },
    },
    2023: {
        'Ganancia no Imponible': {
            'importe': 451683.19,
            'tipo': 'manual',
            'codigo': '1'
        },
        'Deducción Especial - Artículo 30, inciso c)': {
            'importe': 2168079.35,
            'tipo': 'manual',
            'codigo': '2'
        },
        'Cónyuge': {
            'importe': 421088.24,
            'tipo': 'cargaFamilia',
            'codigo': '1'
        },
        'Union Convivencial': {
            'importe': 421088.24,
            'tipo': 'cargaFamilia',
            'codigo': '51'
        },
        'Hijo': {
            'importe': 212356.37,
            'tipo': 'cargaFamilia',
            'codigo': '3'
        },
        'Hijastro': {
            'importe': 212356.37,
            'tipo': 'cargaFamilia',
            'codigo': '30'
        },
        'Hijo con discapacidad': {
            'importe': 424712.74,
            'tipo': 'cargaFamilia',
            'codigo': '31'
        },
        'Hijastro con discapacidad': {
            'importe': 424712.74,
            'tipo': 'cargaFamilia',
            'codigo': '32'
        },
    }
}


TOPES = {
    2022: {
        'MNI': {
            'importe': 451683.19,
            'tipo': 'anual'
        },
        'MNI Mes': {
            'importe': 451683.19,
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
        }
    },
}

DEDUCCION_INCREMENTADA = [
    {
        'vigencia_desde': '2022-01-01',
        'vigencia_hasta': '2022-05-31',
        'sac_exento': 225539,
        'deducciones': [
            (225539, 63187),
            (226087, 64737),
            (226238, 64180),
            (226389, 63669),
            (226690, 62726),
            (226841, 62280),
            (226991, 61848),
            (227142, 61425),
            (227292, 61010),
            (227443, 60605),
            (227594, 60206),
            (227744, 59813),
            (227895, 59424),
            (228046, 59043),
            (228196, 58665),
            (228347, 58292),
            (228497, 57921),
            (228648, 57555),
            (228799, 57192),
            (228949, 56834),
            (229100, 56477),
            (229251, 56124),
            (229401, 55773),
            (229552, 55425),
            (229702, 55079),
            (229853, 54735),
            (230004, 54395),
            (230154, 54056),
            (230305, 53719),
            (230456, 53384),
            (230606, 53051),
            (230757, 52720),
            (230907, 52390),
            (231058, 52063),
            (231209, 51737),
            (231359, 51413),
            (231510, 51089),
            (231661, 50768),
            (231811, 50447),
            (231962, 50129),
            (232112, 49812),
            (232263, 49495),
            (232414, 49180),
            (232564, 48867),
            (232715, 48555),
            (232866, 48244),
            (233016, 47935),
            (233167, 47624),
            (233317, 47317),
            (233468, 47011),
            (233619, 46706),
            (233769, 46400),
            (233920, 46097),
            (234071, 45794),
            (234221, 45493),
            (234372, 45192),
            (234522, 44892),
            (234673, 44592),
            (234824, 44294),
            (234974, 43997),
            (235125, 43701),
            (235276, 43405),
            (235426, 43110),
            (235577, 42817),
            (235727, 42523),
            (235878, 42231),
            (236029, 41940),
            (236179, 41649),
            (236330, 41358),
            (236481, 41069),
            (236631, 40780),
            (236782, 40492),
            (236932, 40205),
            (237083, 39917),
            (237234, 39631),
            (237384, 39346),
            (237535, 39061),
            (237686, 38777),
            (237836, 38494),
            (237987, 38210),
            (238137, 37929),
            (238288, 37647),
            (238439, 37365),
            (238589, 37085),
            (238740, 36805),
            (238891, 36525),
            (239041, 36246),
            (239192, 35968),
            (239342, 35690),
            (239493, 35413),
            (239644, 35136),
            (239794, 34859),
            (239945, 34583),
            (240096, 34309),
            (240246, 34034),
            (240397, 33759),
            (240547, 33485),
            (240698, 33213),
            (240849, 32940),
            (240999, 32667),
            (241150, 32395),
            (241301, 32124),
            (241451, 31853),
            (241602, 31583),
            (241752, 31312),
            (241903, 31042),
            (242054, 30773),
            (242204, 30504),
            (242355, 30236),
            (242506, 29968),
            (242656, 29700),
            (242807, 29434),
            (242957, 29167),
            (243108, 28900),
            (243259, 28634),
            (243409, 28369),
            (243560, 28104),
            (243711, 27838),
            (243861, 27575),
            (244012, 27311),
            (244162, 27048),
            (244313, 26784),
            (244464, 26520),
            (244614, 26258),
            (244765, 25996),
            (244916, 25734),
            (245066, 25472),
            (245217, 25212),
            (245367, 24951),
            (245518, 24690),
            (245669, 24430),
            (245819, 24171),
            (245970, 23912),
            (246121, 23653),
            (246271, 23393),
            (246422, 23134),
            (246572, 22877),
            (246723, 22619),
            (246874, 22362),
            (247024, 22104),
            (247175, 21848),
            (247326, 21591),
            (247476, 21334),
            (247627, 21078),
            (247777, 20822),
            (247928, 20568),
            (248079, 20313),
            (248229, 20059),
            (248380, 19804),
            (248531, 19550),
            (248681, 19295),
            (248832, 19042),
            (248982, 18789),
            (249133, 18536),
            (249284, 18283),
            (249434, 18030),
            (249585, 17778),
            (249736, 17527),
            (249886, 17275),
            (250037, 17024),
            (250187, 16772),
            (250338, 16522),
            (250489, 16270),
            (250639, 16020),
            (250790, 15770),
            (250941, 15520),
            (251091, 15272),
            (251242, 15022),
            (251392, 14773),
            (251543, 14525),
            (251694, 14276),
            (251844, 14028),
            (251995, 13779),
            (252145, 13531),
            (252296, 13284),
            (252447, 13037),
            (252597, 12790),
            (252748, 12543),
            (252899, 12295),
            (253049, 12050),
            (253200, 11803),
            (253350, 11557),
            (253501, 11312),
            (253652, 11066),
            (253802, 10821),
            (253953, 10577),
            (254104, 10331),
            (254254, 10087),
            (254405, 9842),
            (254555, 9598),
            (254706, 9354),
            (254857, 9111),
            (255007, 8867),
            (255158, 8625),
            (255309, 8381),
            (255459, 8138),
            (255610, 7896),
            (255760, 7653),
            (255911, 7411),
            (256062, 7170),
            (256212, 6927),
            (256363, 6686),
            (256514, 6444),
            (256664, 6203),
            (256815, 5962),
            (256965, 5721),
            (257116, 5481),
            (257267, 5240),
            (257417, 5001),
            (257568, 4760),
            (257719, 4520),
            (257869, 4281),
            (258020, 4041),
            (258170, 3802),
            (258321, 3564),
            (258472, 3324),
            (258622, 3086),
            (258773, 2847),
            (258924, 2609),
            (259074, 2371),
            (259225, 2133),
            (259375, 1895),
            (259526, 1658),
            (259677, 1420),
            (259827, 1184),
            (259978, 946),
            (260129, 709),
            (260279, 473),
            (260430, 236),
            (260580, 0)
        ]
    },
    {
        'vigencia_desde': '2022-06-01',
        'vigencia_hasta': '2022-10-31',
        'sac_exento': 280980,
        'deducciones': [
            (280980, 109772.9),
            (281167, 108833.43),
            (281354, 107974.11),
            (281541, 107163.05),
            (281729, 106386.1),
            (281916, 105635.29),
            (282103, 104905.56),
            (282290, 104193.38),
            (282477, 103496.22),
            (282665, 102812.13),
            (282852, 102139.59),
            (283039, 101477.37),
            (283226, 100824.48),
            (283413, 100180.08),
            (283600, 99543.46),
            (283788, 98914.02),
            (283975, 98291.23),
            (284162, 97674.64),
            (284349, 97063.86),
            (284536, 96458.51),
            (284724, 95858.29),
            (284911, 95262.91),
            (285098, 94672.12),
            (285285, 94085.67),
            (285472, 93503.37),
            (285660, 92925.01),
            (285847, 92350.43),
            (286034, 91779.45),
            (286221, 91211.92),
            (286408, 90647.72),
            (286596, 90086.7),
            (286783, 89528.75),
            (286970, 88973.76),
            (287157, 88421.62),
            (287344, 87872.23),
            (287532, 87325.51),
            (287719, 86781.36),
            (287906, 86239.7),
            (288093, 85700.47),
            (288280, 85163.58),
            (288468, 84628.96),
            (288655, 84096.56),
            (288842, 83566.31),
            (289029, 83038.15),
            (289216, 82512.03),
            (289404, 81987.89),
            (289591, 81465.69),
            (289778, 80945.37),
            (289965, 80426.89),
            (290152, 79910.2),
            (290340, 79395.27),
            (290527, 78882.06),
            (290714, 78370.52),
            (290901, 77860.61),
            (291088, 77352.31),
            (291275, 76845.58),
            (291463, 76340.38),
            (291650, 75836.69),
            (291837, 75334.48),
            (292024, 74833.7),
            (292211, 74334.35),
            (292399, 73836.38),
            (292586, 73339.78),
            (292773, 72844.52),
            (292960, 72350.57),
            (293147, 71857.91),
            (293335, 71366.51),
            (293522, 70876.37),
            (293709, 70387.44),
            (293896, 69899.72),
            (294083, 69413.19),
            (294271, 68927.81),
            (294458, 68443.58),
            (294645, 67960.48),
            (294832, 67478.49),
            (295019, 66997.58),
            (295207, 66517.75),
            (295394, 66038.98),
            (295581, 65561.26),
            (295768, 65084.56),
            (295955, 64608.87),
            (296143, 64134.17),
            (296330, 63660.47),
            (296517, 63187.73),
            (296704, 62715.94),
            (296891, 62245.1),
            (297079, 61775.19),
            (297266, 61306.2),
            (297453, 60838.11),
            (297640, 60370.91),
            (297827, 59904.6),
            (298015, 59439.15),
            (298202, 58974.57),
            (298389, 58510.83),
            (298576, 58047.93),
            (298763, 57585.86),
            (298950, 57124.61),
            (299138, 56664.17),
            (299325, 56204.52),
            (299512, 55745.66),
            (299699, 55287.58),
            (299886, 54830.27),
            (300074, 54373.72),
            (300261, 53917.93),
            (300448, 53462.88),
            (300635, 53008.57),
            (300822, 52554.98),
            (301010, 52102.11),
            (301197, 51649.96),
            (301384, 51198.51),
            (301571, 50747.76),
            (301758, 50297.7),
            (301946, 49848.32),
            (302133, 49399.61),
            (302320, 48951.58),
            (302507, 48504.21),
            (302694, 48057.49),
            (302882, 47611.42),
            (303069, 47165.99),
            (303256, 46721.2),
            (303443, 46277.04),
            (303630, 45833.5),
            (303818, 45390.58),
            (304005, 44948.27),
            (304192, 44506.57),
            (304379, 44065.46),
            (304566, 43624.95),
            (304754, 43185.04),
            (304941, 42745.7),
            (305128, 42306.94),
            (305315, 41868.76),
            (305502, 41431.15),
            (305689, 40994.1),
            (305877, 40557.6),
            (306064, 40121.66),
            (306251, 39686.27),
            (306438, 39251.42),
            (306625, 38817.12),
            (306813, 38383.34),
            (307000, 37950.1),
            (307187, 37517.38),
            (307374, 37085.19),
            (307561, 36653.51),
            (307749, 36222.34),
            (307936, 35791.68),
            (308123, 35361.53),
            (308310, 34931.88),
            (308497, 34502.72),
            (308685, 34074.06),
            (308872, 33645.89),
            (309059, 33218.2),
            (309246, 32790.99),
            (309433, 32364.26),
            (309621, 31938),
            (309808, 31512.22),
            (309995, 31086.9),
            (310182, 30662.04),
            (310369, 30237.64),
            (310557, 29813.7),
            (310744, 29390.22),
            (310931, 28967.18),
            (311118, 28544.59),
            (311305, 28122.44),
            (311493, 27700.73),
            (311680, 27279.46),
            (311867, 26858.63),
            (312054, 26438.22),
            (312241, 26018.24),
            (312429, 25598.69),
            (312616, 25179.55),
            (312803, 24760.84),
            (312990, 24342.55),
            (313177, 23924.66),
            (313364, 23507.19),
            (313552, 23090.12),
            (313739, 22673.46),
            (313926, 22257.2),
            (314113, 21841.34),
            (314300, 21425.88),
            (314488, 21010.82),
            (314675, 20596.14),
            (314862, 20181.85),
            (315049, 19767.95),
            (315236, 19354.44),
            (315424, 18941.31),
            (315611, 18528.55),
            (315798, 18116.17),
            (315985, 17704.17),
            (316172, 17292.54),
            (316360, 16881.28),
            (316547, 16470.39),
            (316734, 16059.86),
            (316921, 15649.7),
            (317108, 15239.9),
            (317296, 14830.46),
            (317483, 14421.37),
            (317670, 14012.64),
            (317857, 13604.26),
            (318044, 13196.23),
            (318232, 12788.55),
            (318419, 12381.22),
            (318606, 11974.23),
            (318793, 11567.58),
            (318980, 11161.28),
            (319168, 10755.31),
            (319355, 10350),
            (319542, 9944),
            (319729, 9539),
            (319916, 9135),
            (320104, 8730),
            (320291, 8326),
            (320478, 7923),
            (320665, 7520),
            (320852, 7117),
            (321039, 6714),
            (321227, 6311),
            (321414, 5909),
            (321601, 5508),
            (321788, 5106),
            (321975, 4705),
            (322163, 4304),
            (322350, 3904),
            (322537, 3504),
            (322724, 3104),
            (322911, 2704),
            (323099, 2305),
            (323286, 1906),
            (323473, 1507),
            (323660, 1109),
            (323847, 711),
            (324182, 0)
        ]
    },
    {
        'vigencia_desde': '2022-11-01',
        'vigencia_hasta': '2022-12-31',
        'sac_exento': 330442,
        'deducciones': [
            (330442, 129097),
            (330881, 128077),
            (331321, 127150),
            (331761, 126278),
            (332202, 125446),
            (332642, 124643),
            (333081, 123863),
            (333521, 123103),
            (333961, 122359),
            (334402, 121630),
            (334842, 120914),
            (335282, 120208),
            (335721, 119512),
            (336161, 118825),
            (336600, 118146),
            (337042, 117476),
            (337482, 116811),
            (337921, 116153),
            (338361, 115501),
            (338800, 114854),
            (339242, 114213),
            (339682, 113576),
            (340121, 112944),
            (340561, 112315),
            (341000, 111691),
            (341442, 111071),
            (341882, 110454),
            (342321, 109840),
            (342761, 109230),
            (343200, 108622),
            (343642, 108018),
            (344082, 107416),
            (344521, 106817),
            (344961, 106221),
            (345400, 105626),
            (345842, 105035),
            (346282, 104445),
            (346721, 103857),
            (347161, 103272),
            (347601, 102688),
            (348042, 102107),
            (348482, 101527),
            (348921, 100948),
            (349361, 100372),
            (349801, 99797),
            (350242, 99223),
            (350682, 98651),
            (351122, 98081),
            (351561, 97512),
            (352001, 96944),
            (352443, 96378),
            (352882, 95812),
            (353322, 95248),
            (353761, 94685),
            (354201, 94124),
            (354640, 93563),
            (355082, 93004),
            (355522, 92445),
            (355961, 91887),
            (356401, 91331),
            (356840, 90775),
            (357282, 90221),
            (357722, 89667),
            (358161, 89114),
            (358601, 88561),
            (359040, 88010),
            (359482, 87460),
            (359922, 86910),
            (360361, 86361),
            (360801, 85812),
            (361240, 85265),
            (361682, 84718),
            (362122, 84171),
            (362561, 83626),
            (363001, 83080),
            (363440, 82536),
            (363882, 81992),
            (364322, 81449),
            (364761, 80906),
            (365201, 80363),
            (365641, 79822),
            (366082, 79281),
            (366522, 78740),
            (366962, 78199),
            (367401, 77660),
            (367841, 77120),
            (368283, 76581),
            (368722, 76043),
            (369162, 75505),
            (369601, 74967),
            (370041, 74430),
            (370483, 73893),
            (370922, 73356),
            (371362, 72820),
            (371801, 72284),
            (372241, 71749),
            (372680, 71213),
            (373122, 70679),
            (373562, 70144),
            (374001, 69610),
            (374441, 69076),
            (374880, 68542),
            (375322, 68009),
            (375762, 67476),
            (376201, 66943),
            (376641, 66410),
            (377080, 65878),
            (377522, 65346),
            (377962, 64814),
            (378401, 64282),
            (378841, 63751),
            (379280, 63219),
            (379722, 62688),
            (380162, 62158),
            (380601, 61627),
            (381041, 61096),
            (381481, 60566),
            (381922, 60036),
            (382362, 59506),
            (382802, 58976),
            (383241, 58447),
            (383681, 57917),
            (384122, 57388),
            (384562, 56859),
            (385002, 56330),
            (385441, 55801),
            (385881, 55272),
            (386323, 54744),
            (386762, 54215),
            (387202, 53687),
            (387641, 53158),
            (388081, 52630),
            (388520, 52102),
            (388962, 51574),
            (389402, 51046),
            (389841, 50519),
            (390281, 49991),
            (390720, 49463),
            (391162, 48936),
            (391602, 48408),
            (392041, 47881),
            (392481, 47353),
            (392920, 46826),
            (393362, 46299),
            (393802, 45772),
            (394241, 45245),
            (394681, 44718),
            (395120, 44191),
            (395562, 43664),
            (396002, 43137),
            (396441, 42610),
            (396881, 42083),
            (397321, 41557),
            (397762, 41030),
            (398202, 40503),
            (398641, 39977),
            (399081, 39450),
            (399521, 38923),
            (399962, 38397),
            (400402, 37870),
            (400842, 37343),
            (401281, 36817),
            (401721, 36290),
            (402163, 35764),
            (402602, 35237),
            (403042, 34711),
            (403481, 34184),
            (403921, 33658),
            (404363, 33131),
            (404802, 32605),
            (405242, 32078),
            (405681, 31552),
            (406121, 31025),
            (406560, 30498),
            (407002, 29972),
            (407442, 29445),
            (407881, 28919),
            (408321, 28392),
            (408760, 27865),
            (409202, 27339),
            (409642, 26812),
            (410081, 26285),
            (410521, 25758),
            (410960, 25232),
            (411402, 24705),
            (411842, 24178),
            (412281, 23651),
            (412721, 23124),
            (413160, 22597),
            (413602, 22070),
            (414042, 21543),
            (414481, 21016),
            (414921, 20489),
            (415361, 19962),
            (415802, 19435),
            (416242, 18907),
            (416682, 18380),
            (417121, 17853),
            (417561, 17325),
            (418003, 16798),
            (418442, 16270),
            (418882, 15743),
            (419321, 15215),
            (419761, 14688),
            (420203, 14160),
            (420642, 13633),
            (421082, 13104),
            (421521, 12576),
            (421961, 12049),
            (422403, 11520),
            (422842, 10992),
            (423282, 10465),
            (423721, 9937),
            (424161, 9409),
            (424600, 8880),
            (425042, 8351),
            (425482, 7822),
            (425921, 7295),
            (426361, 6765),
            (426800, 6237),
            (427242, 5708),
            (427682, 5180),
            (428121, 4651),
            (428561, 4122),
            (429000, 3592),
            (429442, 3064),
            (429882, 2534),
            (430321, 2005),
            (430761, 1476),
            (431201, 947),
            (431988, 0)
        ]
    },
    {
        'vigencia_desde': '2023-01-01',
        'vigencia_hasta': '2023-04-30',
        'sac_exento': 404062,
        'deducciones': [
            (404062, 115775),
            (404331, 114779),
            (404601, 113865),
            (404871, 113003),
            (405139, 112178),
            (405409, 111381),
            (405679, 110608),
            (405947, 109852),
            (406217, 109109),
            (406486, 108385),
            (406756, 107672),
            (407026, 106969),
            (407294, 106273),
            (407564, 105592),
            (407834, 104916),
            (408102, 104249),
            (408372, 103585),
            (408641, 102931),
            (408911, 102281),
            (409181, 101641),
            (409449, 101003),
            (409719, 100371),
            (409989, 99744),
            (410257, 99121),
            (410527, 98502),
            (410796, 97887),
            (411066, 97279),
            (411336, 96673),
            (411604, 96070),
            (411874, 95471),
            (412144, 94876),
            (412412, 94284),
            (412682, 93693),
            (412951, 93109),
            (413221, 92526),
            (413491, 91946),
            (413759, 91367),
            (414029, 90793),
            (413491, 90219),
            (414567, 89650),
            (414837, 89083),
            (415106, 88516),
            (415376, 87953),
            (415646, 87393),
            (415914, 86835),
            (416184, 86279),
            (416454, 85726),
            (416722, 85170),
            (416992, 84621),
            (417261, 84074),
            (417531, 83528),
            (417801, 82981),
            (418069, 82439),
            (418339, 81897),
            (418609, 81359),
            (418877, 80821),
            (419147, 80284),
            (419416, 79748),
            (419686, 79215),
            (419956, 78684),
            (420224, 78154),
            (420494, 77625),
            (420764, 77097),
            (421032, 76573),
            (421302, 76047),
            (421571, 75525),
            (421841, 75005),
            (422111, 74484),
            (422379, 73964),
            (422649, 73447),
            (422919, 72930),
            (423187, 72415),
            (423457, 71902),
            (423726, 71387),
            (423996, 70875),
            (424266, 70366),
            (424534, 69856),
            (424804, 69348),
            (425074, 68842),
            (425342, 68334),
            (425612, 67832),
            (425881, 67327),
            (426151, 66823),
            (426421, 66322),
            (426689, 65822),
            (426959, 65321),
            (427229, 64822),
            (427497, 64325),
            (427767, 63827),
            (428036, 63332),
            (428306, 62837),
            (428576, 62341),
            (428844, 61848),
            (429114, 61358),
            (429384, 60866),
            (429652, 60374),
            (429922, 59884),
            (430191, 59398),
            (430461, 58909),
            (430731, 58421),
            (430999, 57935),
            (431269, 57450),
            (431539, 56965),
            (431807, 56483),
            (432077, 55998),
            (432346, 55515),
            (432616, 55034),
            (432886, 54553),
            (433154, 54074),
            (433424, 53594),
            (433694, 53115),
            (433962, 52639),
            (434232, 52162),
            (434501, 51684),
            (434771, 51209),
            (435041, 50735),
            (435309, 50261),
            (435579, 49785),
            (435849, 49315),
            (436117, 48843),
            (436387, 48372),
            (436656, 47900),
            (436926, 47428),
            (437196, 46959),
            (437464, 46491),
            (437734, 46022),
            (438004, 45554),
            (438272, 45089),
            (438542, 44622),
            (438811, 44155),
            (439081, 43690),
            (439351, 43227),
            (439619, 42764),
            (439889, 42301),
            (440159, 41836),
            (440427, 41373),
            (440697, 40913),
            (440966, 40451),
            (441236, 39992),
            (441506, 39530),
            (441774, 39073),
            (442044, 38613),
            (442314, 38153),
            (442582, 37696),
            (442852, 37238),
            (443121, 36784),
            (443391, 36327),
            (443661, 35873),
            (443929, 35417),
            (444199, 34963),
            (444469, 34507),
            (444737, 34054),
            (445007, 33602),
            (445276, 33150),
            (445546, 32697),
            (445816, 32245),
            (446084, 31794),
            (446354, 31345),
            (446624, 30894),
            (446892, 30445),
            (447162, 29995),
            (447431, 29548),
            (447701, 29097),
            (447971, 28650),
            (448239, 28203),
            (448509, 27756),
            (448779, 27312),
            (449047, 26865),
            (449317, 26420),
            (449586, 25976),
            (449856, 25531),
            (450125, 25087),
            (450394, 24642),
            (450664, 24199),
            (450932, 23757),
            (451202, 23315),
            (451472, 22873),
            (451741, 22432),
            (452011, 21988),
            (452281, 21550),
            (452549, 21108),
            (452819, 20668),
            (453087, 20230),
            (453357, 19790),
            (453627, 19352),
            (453896, 18916),
            (454166, 18476),
            (454436, 18039),
            (454704, 17601),
            (454974, 17165),
            (455242, 16729),
            (455512, 16294),
            (455782, 15858),
            (456051, 15425),
            (456321, 14988),
            (456591, 14554),
            (456859, 14121),
            (457129, 13687),
            (457397, 13254),
            (457667, 12823),
            (457937, 12389),
            (458206, 11957),
            (458476, 11524),
            (458746, 11093),
            (459014, 10662),
            (459284, 10231),
            (459552, 9802),
            (459822, 9371),
            (460092, 8944),
            (460361, 8513),
            (460631, 8084),
            (460901, 7656),
            (461169, 7227),
            (461439, 6799),
            (461707, 6374),
            (461977, 5945),
            (462247, 5519),
            (462516, 5092),
            (462786, 4666),
            (463056, 4240),
            (463324, 3815),
            (463594, 3389),
            (463862, 2965),
            (464132, 2540),
            (464402, 2117),
            (464671, 1692),
            (464941, 1268),
            (465211, 846),
            (465479, 422),
            (465749, 0)
        ]
    },
    {
        'vigencia_desde': '2023-05-01',
        'vigencia_hasta': '2023-12-31',
        'sac_exento': 506230,
        'deducciones': [
            (506230, 199645),
            (506568, 197921),
            (506906, 196344),
            (507244, 194867),
            (507580, 193441),
            (507918, 192064),
            (508256, 190735),
            (508592, 189428),
            (508930, 188153),
            (509267, 186898),
            (509606, 185664),
            (509944, 184458),
            (510280, 183260),
            (510618, 182078),
            (510956, 180918),
            (511292, 179763),
            (511630, 178625),
            (511967, 177494),
            (512306, 176373),
            (512644, 175271),
            (512980, 174169),
            (513318, 173077),
            (513656, 172001),
            (513992, 170925),
            (514330, 169860),
            (514667, 168799),
            (515006, 167745),
            (515344, 166705),
            (515680, 165664),
            (516018, 164629),
            (516356, 163607),
            (516692, 162583),
            (517030, 161569),
            (517367, 160555),
            (517705, 159547),
            (518044, 158552),
            (518379, 157553),
            (518718, 156559),
            (519056, 155577),
            (519392, 154592),
            (519730, 153615),
            (520067, 152638),
            (520405, 151665),
            (520744, 150703),
            (521079, 149738),
            (521418, 148776),
            (521756, 147825),
            (522092, 146871),
            (522430, 145923),
            (522767, 144975),
            (523105, 144030),
            (523444, 143095),
            (523779, 142157),
            (524118, 141221),
            (524456, 140295),
            (524792, 139366),
            (525130, 138442),
            (525467, 137518),
            (525805, 136597),
            (526143, 135685),
            (526479, 134768),
            (526817, 133855),
            (527156, 132950),
            (527491, 132042),
            (527830, 131139),
            (528167, 130235),
            (528505, 129333),
            (528843, 128440),
            (529179, 127543),
            (529517, 126648),
            (529856, 125762),
            (530191, 124872),
            (530530, 123987),
            (530867, 123100),
            (531205, 122216),
            (531543, 121340),
            (531879, 120460),
            (532217, 119581),
            (532556, 118711),
            (532891, 117836),
            (533230, 116967),
            (533567, 116096),
            (533905, 115227),
            (534243, 114366),
            (534579, 113500),
            (534917, 112636),
            (535255, 111780),
            (535591, 110920),
            (535929, 110064),
            (536266, 109207),
            (536605, 108351),
            (536943, 107504),
            (537279, 106651),
            (537617, 105801),
            (537955, 104957),
            (538291, 104110),
            (538629, 103266),
            (538966, 102422),
            (539305, 101578),
            (539643, 100743),
            (539979, 99902),
            (540317, 99063),
            (540655, 98232),
            (540991, 97395),
            (541329, 96563),
            (541666, 95730),
            (542005, 94898),
            (542343, 94073),
            (542679, 93243),
            (543017, 92415),
            (543355, 91594),
            (543691, 90768),
            (544029, 89947),
            (544366, 89124),
            (544704, 88301),
            (545043, 87487),
            (545378, 86667),
            (545717, 85849),
            (546055, 85037),
            (546391, 84221),
            (546729, 83409),
            (547066, 82596),
            (547404, 81783),
            (547743, 80977),
            (548078, 80167),
            (548417, 79358),
            (548755, 78555),
            (549091, 77748),
            (549429, 76945),
            (549766, 76140),
            (550104, 75336),
            (550442, 74539),
            (550778, 73737),
            (551117, 72936),
            (551455, 72142),
            (551791, 71343),
            (552129, 70549),
            (552466, 69752),
            (552804, 68956),
            (553142, 68167),
            (553478, 67373),
            (553816, 66580),
            (554155, 65794),
            (554490, 65003),
            (554829, 64215),
            (555166, 63426),
            (555504, 62638),
            (555842, 61856),
            (556178, 61070),
            (556516, 60284),
            (556855, 59505),
            (557190, 58721),
            (557529, 57941),
            (557866, 57159),
            (558204, 56378),
            (558542, 55603),
            (558878, 54824),
            (559216, 54045),
            (559555, 53273),
            (559890, 52496),
            (560229, 51723),
            (560566, 50947),
            (560904, 50173),
            (561242, 49405),
            (561578, 48632),
            (561916, 47860),
            (562254, 47094),
            (562590, 46323),
            (562928, 45556),
            (563265, 44787),
            (563604, 44022),
            (563941, 43257),
            (564278, 42491),
            (564616, 41730),
            (564952, 40965),
            (565290, 40201),
            (565628, 39440),
            (565965, 38677),
            (566304, 37914),
            (566642, 37158),
            (566978, 36398),
            (567316, 35643),
            (567652, 34884),
            (567990, 34125),
            (568328, 33370),
            (568665, 32612),
            (569004, 31856),
            (569342, 31105),
            (569678, 30350),
            (570016, 29601),
            (570352, 28847),
            (570690, 28094),
            (571028, 27344),
            (571365, 26592),
            (571703, 25841),
            (572042, 25096),
            (572377, 24346),
            (572716, 23602),
            (573051, 22854),
            (573390, 22106),
            (573728, 21361),
            (574065, 20614),
            (574403, 19868),
            (574742, 19128),
            (575077, 18383),
            (575416, 17645),
            (575751, 16901),
            (576090, 16158),
            (576428, 15418),
            (576765, 14676),
            (577103, 13935),
            (577441, 13200),
            (577777, 12460),
            (578116, 11726),
            (578451, 10987),
            (578790, 10249),
            (579128, 9514),
            (579465, 8777),
            (579803, 8040),
            (580141, 7310),
            (580477, 6574),
            (580815, 5845),
            (581151, 5111),
            (581489, 4377),
            (581828, 3647),
            (582165, 2914),
            (582503, 2182),
            (582841, 1456),
            (583177, 725),
            (583515, 0),
        ]
    }
]
