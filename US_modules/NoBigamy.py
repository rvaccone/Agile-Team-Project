# [US11] - Phillip
from datetime import datetime, date
from US_modules.helpers import stringToDate, isOverlap, findKeyInArray


def noBigamy(individual_list, family_list):
    marriedTimes = {}
    for family in family_list:
        if family['Marriage Date'] != 'N/A':
            if family['Husband ID'] in marriedTimes:
                marriedTimes[family['Husband ID']].append(family['ID'])
            else:
                marriedTimes[family['Husband ID']] = [family['ID']]
            if family['Wife ID'] in marriedTimes:
                marriedTimes[family['Wife ID']].append(family['ID'])
            else:
                marriedTimes[family['Wife ID']] = [family['ID']]
    for key in marriedTimes:
        if len(marriedTimes[key]) > 1:
            for i in range(len(marriedTimes[key])):
                for j in range(len(marriedTimes[key])):
                    if i != j:
                        fam1=findKeyInArray(family_list, marriedTimes[key][i])
                        fam2=findKeyInArray(family_list, marriedTimes[key][j])
                        if (isOverlap(stringToDate(fam1['Marriage Date']), stringToDate(fam1['Divorce Date']), stringToDate(fam2['Marriage Date']), stringToDate(fam2['Divorce Date']))):
                            assert False, f" ERROR: Bigamy: {fam1['ID']} + and {fam2['ID']} are overlapping marriages"
    return True
