#Justus
def SiblingsNotMarried (individual_list,family_list):
    for family in family_list:
        if len(family['Children']) > 1:
            children = family['Children']
            childIDS = []
            for child in children:
                for individual in individual_list:
                    if(individual['ID'] == child):
                        if(individual['Spouse'] != 'N/A'):
                            for otherChild in children:
                                assert(otherChild != individual['spouse']), "Siblings are married"


