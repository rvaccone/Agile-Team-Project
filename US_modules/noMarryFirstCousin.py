#TaeSeo
def listAuntsAndUncles(person, individual_list, family_list):
    auntsAndUncles = []
    for family in family_list:
        for individual in individual_list:
            if person['ID'] == individual['ID']:
                if family['Husband ID'] == individual['ID']:
                    auntsAndUncles.append(family['Wife ID'])
                elif family['Wife ID'] == individual['ID']:
                    auntsAndUncles.append(family['Husband ID'])
    return auntsAndUncles  # Add this line to return the list



def listFirstCousins(person, individual_list, family_list):
    first_cousins = []
    aunts_and_uncles = listAuntsAndUncles(person, individual_list, family_list)
    for aunt_or_uncle in aunts_and_uncles:
        for individual in individual_list:
            if individual['ID'] == aunt_or_uncle:
                first_cousins.extend(individual['Children'])

    return first_cousins


def noMarriageToFirstCousins(individual_list, family_list):
    for individual in individual_list:
        first_cousins = listFirstCousins(individual, individual_list, family_list)
        assert(individual['Spouse'] not in first_cousins), "Error: Marriage to first cousin"
