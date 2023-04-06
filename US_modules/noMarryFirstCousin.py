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
