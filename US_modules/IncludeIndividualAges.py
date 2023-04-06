# [US27] - Justus



def IncludeIndividualAges(individual_list):    
    for individual in individual_list:
        assert individual['Age'] != 'N/A', f"ERROR: individual {individual['ID']} does not have an age"
    return True


