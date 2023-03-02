

def listAncestors(person, individual_list, family_list):
    ancestors = []

    if(len(person['Children']) >0 ):
        for child in person['Children']:
            ancestors.append(child)
            for individual in individual_list:
                if(individual['ID'] == child):
                    if(len(individual['Children']) > 0):
                        return ancestors.append(listAncestors(individual, individual_list, family_list))
                    else:
                        return ancestors
    else:
        return ancestors




def noMarriageToAncestors(individual_list, family_list):
    for individual in individual_list:
        ancestors = listAncestors(individual, individual_list, family_list)
        if individual['Spouse'] in ancestors:
            print("Error: Individual", individual['ID'], "is married to their ancestor", individual['Spouse'])
            return False    