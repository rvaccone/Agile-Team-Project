# [US28] - Justus



def OrderSiblingsByAge(individual_list,family_list):    
    for family in family_list:

        if family['Children'] != 'N/A':

            for i in range(1,len(family['Children'])):

                for individual in  individual_list:

                    if individual['ID'] == family['Children'][i]:
                        for otherIndividual in individual_list:
                            if otherIndividual['ID'] == family['Children'][i-1]:
                                assert int(individual['Age']) < int(otherIndividual['Age']), f"ERROR: Siblings {individual['ID']} and {otherIndividual['ID']} not ordered by age"
    return True


