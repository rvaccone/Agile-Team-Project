# [US#14] Phillip Anerine
from US_modules.helpers import findKeyInArray

def more_than_5_births(individual_list, family_list):
    for family in family_list:
        if family['Children'] != []:
            birthDates = {}
            for child in family['Children']: 
                foundChild = findKeyInArray(individual_list, child)
                birthday = foundChild['Birthday']
                if (birthday in birthDates):
                    birthDates[birthday] += 1
                else: 
                    birthDates[birthday] = 1
            for date in birthDates:
                assert (birthDates[date] < 5), f" ERROR: More than 5 births: {family[family.id]} has more than 5 births on {date}"
    return True