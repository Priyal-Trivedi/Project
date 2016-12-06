from methods.methods import *
from methods.save_methods import *
from methods.get_methods  import *

STEPS_NAME = {
    '1': "Select System Boundary",
    '2': "Generate Requirements",
    '3': "Select Sustainability Definitions",
    '4': "Select Sustainability Indicators",
    '5': "Select Methods TC in the task clarification phase",
    '6': "Select Methods TC in the task clarification phase",
    '7': "Conceptual Design - Design Stage",
    '8': "Conceptual Design - Generate-Select Activity",
    '9': "Conceptual Design - Generate-Select Activity",
    '10': "Conceptual Design - Generate-Select Activity",
    '11': "Conceptual Design - Generate-Select Activity",
    '12': "Conceptual Design - Generate-Select Activity",
    '13': "Conceptual Design - Generate-Select Activity",
    '14': "Conceptual Design - Generate-Select Activity",
    '15': "Conceptual Design - Generate-Select Activity",
    '16': "Conceptual Design - Generate-Select Activity",
    '17': "Conceptual Design - Generate-Select Activity",

}

STEPS_METHODS = {
    '1': select_system_boundary,
    '2': generate_requirements,
    '3': select_sustainability_definitions,
    '4': select_sustainability_indicators,
    '5': select_methods_tc,
    '6': select_methods_tc,
    '7': conceptual_design_home,
    '8': conceptual_design_gs,
    '9': conceptual_design_es_ss,
    '10': conceptual_design_gs_ms,
    '11': conceptual_design_es_ms,
    '12': embodiment_design_home,
    '13': embodiment_design_gs,
    '14': embodiment_design_es_ss,
    '15': embodiment_design_gs_ms,
    '16': embodiment_design_es_ms,
    '17': detail_design_home,
}

SAVE_STEPS_METHODS = {
    1: save_system_boundary,
    2: save_generate_requirements,
    3: save_sustainability_definitions,
    4: save_sustainability_indicators,
    8: save_conceptual_design_gs,
    9: save_conceptual_design_es_ss,
    10: save_conceptual_design_gs_ms,
    11: save_conceptual_design_es_ms,

}

GET_METHODS_DATA = {
    1: get_system_boundary,
    2 : get_generate_requirements,
    3 : get_sustainability_definitions,
    4 : get_sustainability_indicators,
    8 : get_conceptual_design_methods_data,
    9 : get_conceptual_design_methods_data,
    10 : get_conceptual_design_methods_data,
    11 : get_conceptual_design_methods_data,
    13 : get_conceptual_design_methods_data,
    14 : get_conceptual_design_methods_data,
    15 : get_conceptual_design_methods_data,
    16 : get_conceptual_design_methods_data,
}