# [US11] - Phillip
from datetime import datetime, date

def noBigamy(family_list, individual_list):
    def stringToDate(date):
        if date=='N/A':
            return datetime.now().date()
        date = date.split()
        day, month, year = int(date[0]), int(
            datetime.strptime(date[1], "%b").month), int(date[2])
        return datetime(year, month, day)
    def isOverlap(start1, end1, start2, end2):
        if start1<start2<end1:
            return False
        if start2<start1<end2:
            return False
        return True

    marriedTimes = {}
    for family in family_list:
        if family['Marriage Date'] != 'N/A':
            if family['Husband ID'] in marriedTimes:
                marriedTimes[family['Husband ID']].push(family['ID'])
            else:
                marriedTimes[family['Husband ID']] = [family['ID']]
            if family['Wife ID'] in marriedTimes:
                marriedTimes[family['Wife ID']].push(family['ID'])
            else:
                marriedTimes[family['Wife ID']] = [family['ID']]
    for key in marriedTimes:
        if len(marriedTimes[key]) > 1:
            for i in marriedTimes[key]:
                for j in marriedTimes[key]:
                    if i != j:
                        assert isOverlap(stringToDate(family_list[i]['Marriage Date']), stringToDate(family_list[i]['Divorce Date']), stringToDate(family_list[j]['Marriage Date']), stringToDate(family_list[j]['Divorce Date'])), f" ERROR: Bigamy: {family_list[i]['ID']} + and {family_list[j]['ID']} are overlapping marriages"
    return True
