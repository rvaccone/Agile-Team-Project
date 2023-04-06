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
