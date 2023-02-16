# [US12] - Rocco
def parents_not_too_old(individual_list):
    for individual in individual_list:
        if individual['Age'] != 'N/A' and individual['Children'] != []:
            assert int(individual['Age']) < 150, "Individual is too old to be a parent"
    return True