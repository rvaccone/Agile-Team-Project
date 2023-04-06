# [US28] - Justus



def OrderSiblingsByAge(individual_list, family_list):    
    for family in family_list:
        if family['Children'] != 'N/A' and len(family['Children'] > 1):
            for i in range(1,len(family['Children'])):
                for individual in  individual_list:
                    if individual['ID'] == family['Children'][i]:
                        for otherIndividual in individual_list:
                            if otherIndividual['ID'] == family['Children'][i-1]:
                                assert int(individual['Age']) > int(otherIndividual['Age']), f"ERROR: Siblings {individual['ID']} and {otherIndividual['ID']} not ordered by age"
    return True


def test_OrderSiblingsByAge(self):
        individual = Individual()
        individual.create_individual(individual_dict)['ID'] = 'I7'
        individual.get_individual_list()[0]['Age'] = '10'

        individual.create_individual(individual_dict)['ID'] = 'I9'
        individual.get_individual_list()[1]['Age'] = '15'

        individual.create_individual(individual_dict)['ID'] = 'I10'
        individual.get_individual_list()[2]['Children'] = ['I9','I7']

        family = Family()
        family.create_family(family_dict)['Husband ID'] = 'I10'
        family.get_family_list()[0]['Children'] = ['I9,I7']


        try:
            OrderSiblingsByAge(individual.get_individual_list(), family.get_family_list())
            print("Passed: Siblings ordered by age")
        except AssertionError:
            print("Failed: Did not detect siblings ordered by age when they were")

        family.get_family_list()[0]['Children'] = ['I7,I9']

        try:
            OrderSiblingsByAge(individual.get_individual_list(), family.get_family_list())
            print("Failed: Detected siblings ordered by age when they were not")
        except AssertionError:
            print("Passed: Successfully detected siblings not ordered by age")