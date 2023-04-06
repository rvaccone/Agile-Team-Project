#TaeSeo
def listAuntsAndUncles(person, individual_list, family_list):
    aunts_and_uncles = []
    if person['Parents']:
        for parent in person['Parents']:
            for family in family_list:
                if family['ID'] == parent:
                    siblings = [sibling for sibling in family['Children'] if sibling != person['ID']]
                    aunts_and_uncles.extend(siblings)
    return aunts_and_uncles



def noMarriageToAuntsAndUncles(individual_list, family_list):
    for individual in individual_list:
        aunts_and_uncles = listAuntsAndUncles(individual, individual_list, family_list)
        assert(individual['Spouse'] not in aunts_and_uncles), "Error: Marriage to aunt/uncle"
