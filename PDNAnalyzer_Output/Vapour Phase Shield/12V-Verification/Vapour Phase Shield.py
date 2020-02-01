designFile = "Y:/Altium Projects/VapourPhaseReflowShield/PDNAnalyzer_Output/Vapour Phase Shield/odb.tgz"

powerNets = ["12V"]

groundNets = ["GND", "FANGND"]

excitation = [
{
"id": "0",
"type": "source",
"power_pins": [ ("J2", "1") ],
"ground_pins": [ ("J2", "2") ],
"voltage": 12,
"Rpin": 0,
}
,
{
"id": "1",
"type": "load",
"power_pins": [ ("J4", "1") ],
"ground_pins": [ ("J4", "2") ],
"current": 2.25,
"Rpin": 0.0444444444444444,
}
,
{
"id": "2",
"type": "load",
"power_pins": [ ("J5", "1") ],
"ground_pins": [ ("J5", "2") ],
"current": 2.25,
"Rpin": 0.0444444444444444,
}
,
{
"id": "3",
"type": "load",
"power_pins": [ ("J6", "1") ],
"ground_pins": [ ("J6", "2") ],
"current": 2.25,
"Rpin": 0.0444444444444444,
}
,
{
"id": "4",
"type": "load",
"power_pins": [ ("J7", "1") ],
"ground_pins": [ ("J7", "2") ],
"current": 2.25,
"Rpin": 0.0444444444444444,
}
,
{
"id": "5",
"type": "load",
"power_pins": [ ("J8", "1") ],
"ground_pins": [ ("J8", "2") ],
"current": 2.25,
"Rpin": 0.0444444444444444,
}
,
{
"id": "6",
"type": "load",
"power_pins": [ ("J9", "1") ],
"ground_pins": [ ("J9", "2") ],
"current": 2.25,
"Rpin": 0.0444444444444444,
}
,
{
"id": "7",
"type": "load",
"power_pins": [ ("J10", "1") ],
"ground_pins": [ ("J10", "2") ],
"current": 2.25,
"Rpin": 0.0444444444444444,
}
,
{
"id": "8",
"type": "load",
"power_pins": [ ("J11", "1") ],
"ground_pins": [ ("J11", "2") ],
"current": 2.25,
"Rpin": 0.0444444444444444,
}
]


voltage_regulators = [
{
"id": "9",
"type": "linear",

"in": [ ("IC4", "3"), ("IC4", "2"), ("IC4", "1") ],
"out": [ ("IC4", "8"), ("IC4", "7"), ("IC4", "6"), ("IC4", "5") ],
"ref": [],

"v2": 0,
"i1": 0,
"Ro": 1E-06,
"Rpin": 0.00274285714285714,
}
]


# Resistors / Inductors

passives = []


# Material Properties:

tech = [

        {'name': 'TOP_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05},
        {'name': 'TOP_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'SUBSTRATE-1', 'DielectricConstant': 4.8, 'Thickness': 0.00155},
        {'name': 'BOTTOM_LAYER', 'Conductivity': 47000000, 'Thickness': 3.556E-05},
        {'name': 'BOTTOM_SOLDER', 'DielectricConstant': 3.5, 'Thickness': 1.016E-05}

       ]

special_settings = {'removecutoutsize' : 7.8 }


plating_thickness = 0.7
finished_hole_diameters = False
