# [US11] - Phillip
from datetime import datetime, date

def noBigamy(individual_list, family_list):
    def stringToDate(date):
        if date=='N/A':
            return datetime.now().date()
        date = date.split()
        day, month, year = int(date[0]), int(
            datetime.strptime(date[1], "%b").month), int(date[2])
        return datetime(year, month, day)
    
    def isOverlap(start1, end1, start2, end2):
        if start1<start2<end1:
            return True
        if start2<start1<end2:
            return True
        return False

    def findKeyInArray(array, key):
        for i in range(len(array)):
            if array[i]['ID'] == key:
                return array[i]
        return -1

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
