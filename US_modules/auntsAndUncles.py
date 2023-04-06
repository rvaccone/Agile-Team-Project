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

def noMarriageToAuntsAndUncles(individual_list, family_list):
    for individual in individual_list:
        aunts_and_uncles = listAuntsAndUncles(individual, individual_list, family_list)
        if individual['Spouse'] in aunts_and_uncles:
            print("Error: Marriage to aunt or uncle")
            return False
