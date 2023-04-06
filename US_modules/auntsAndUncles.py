#TaeSeo
def listAuntsAndUncles(person, individual_list, family_list):
    aunts_and_uncles = []
    for family in family_list:
        if person['ID'] in family['Children']:
            for individual in individual_list:
                if individual['ID'] == family['Husband']:
                    aunts_and_uncles.append(individual['ID'])
                elif individual['ID'] == family['Wife']:
                    aunts_and_uncles.append(individual['ID'])



def noMarriageToAuntsAndUncles(individual_list, family_list):
    for individual in individual_list:
        aunts_and_uncles = listAuntsAndUncles(individual, individual_list, family_list)
        assert(individual['Spouse'] not in aunts_and_uncles), "Error: Marriage to aunt/uncle"
