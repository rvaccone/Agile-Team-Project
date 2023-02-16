# [US10] - Rocco
def individual_is_too_young_to_be_married(individual_list):
    for individual in individual_list:
        if individual['Age'] != 'N/A' and individual['Spouse'] != 'N/A':
            assert int(individual['Age']) >= 14, "Individual is too young to be married"
    return True