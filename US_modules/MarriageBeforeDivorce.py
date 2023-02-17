# [US04] - Phillip
from datetime import datetime, date

def MarriageBeforeDivorce(individual_list, family_list):
    def stringToDate(date):
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
    
    for family in family_list:
        if family['Marriage Date'] == 'N/A' and family['Divorce Date'] != 'N/A':
            assert False, f" ERROR: Marriage before divorce: {family['ID']} has a divorce date but no marriage date"
        if family['Marriage Date'] != 'N/A' and family['Divorce Date'] != 'N/A':
            if stringToDate(family['Marriage Date']) > stringToDate(family['Divorce Date']):
                assert False, f" ERROR: Marriage before divorce: {family['ID']} has a marriage date after its divorce date"
    return True
