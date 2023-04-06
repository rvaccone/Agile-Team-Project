def corresponding_entries(individual_list):
    for individual in individual_list:
        assert(individual['Family'] != 'N/A' or individual['Spouse'] != 'N/A' and len(individual['Children']) == 0)