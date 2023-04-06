# [US27] - Justus



def IncludeIndividualAges(individual_list):    
    for individual in individual_list:
        assert individual['Age'] != 'N/A', f"ERROR: individual {individual['ID']} does not have an age"
    return True


def test_IncludeIndividualAges(self):
        individual = Individual()
        individual.create_individual(individual_dict)['ID'] = 'I7'
        individual.get_individual_list()[0]['Age'] = '10'

        individual.create_individual(individual_dict)['ID'] = 'I9'
        individual.get_individual_list()[1]['Age'] = '15'

        try:
            IncludeIndividualAges(individual.get_individual_list())
            print("Passed: All individuals have ages.")
        except AssertionError:
            print("Failed: Did not detect all ages when they were present.")


        individual.create_individual(individual_dict)['ID'] = 'I5'

        try:
            IncludeIndividualAges(individual.get_individual_list())
            print("Failed: Did not detect missing age")
        except AssertionError:
            print("Passed: Successfully detected missing age")