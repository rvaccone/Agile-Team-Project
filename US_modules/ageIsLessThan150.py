# [US07] - TaeSeo
def ageIsLessThan150(individual_list):
    for individual in individual_list:
        if individual['Age'] != 'N/A':
            assert(int(individual['Age']) < 150), "Individual is too old"