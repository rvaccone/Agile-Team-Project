# [US04] - Phillip
from datetime import datetime, date
from US_modules.helpers import stringToDate


def MarriageBeforeDivorce(individual_list, family_list):    
    for family in family_list:
        if family['Marriage Date'] == 'N/A' and family['Divorce Date'] != 'N/A':
            assert False, f" ERROR: Marriage before divorce: {family['ID']} has a divorce date but no marriage date"
        if family['Marriage Date'] != 'N/A' and family['Divorce Date'] != 'N/A':
            if stringToDate(family['Marriage Date']) > stringToDate(family['Divorce Date']):
                assert False, f" ERROR: Marriage before divorce: {family['ID']} has a marriage date after its divorce date"
    return True
