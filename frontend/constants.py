from methods.methods import select_system_boundary, generate_requirements, select_sustainability_definitions, select_sustainability_indicators , select_methods_tc


STEPS_NAME = {
    '0': "Select System Boundary",
    '1': "Generate Requirements",
    '2': "Select Sustainability Definitions",
    '3': "Select Sustainability Indicators",
    '4': "Select Methods TC in the task clarification phase",

}

STEPS_METHODS = {
    '0': select_system_boundary,
    '1': generate_requirements,
    '2': select_sustainability_definitions,
    '3': select_sustainability_indicators,
    '4': select_methods_tc
}
