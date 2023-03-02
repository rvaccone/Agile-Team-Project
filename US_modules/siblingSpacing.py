# [#US13] - PA
#Birth dates of siblings should be more than 8 months apart or less than 2 days apart (twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
from US_modules.helpers import stringToDate, findKeyInArray
from datetime import date, datetime

def siblingSpacing (individual_list, family_list):
    for family in family_list:
        if family['Children'] != 'N/A':
            for child in family['Children']:
                foundChild = findKeyInArray(individual_list, child)
                if foundChild['Birthday'] != 'N/A':
                    for child2 in family['Children']:
                        sibling = findKeyInArray(individual_list, child2)
                        if sibling['Birthday'] != 'N/A':
                            if sibling['ID'] != foundChild['ID']:
                                if abs(stringToDate(foundChild['Birthday']) - stringToDate(sibling['Birthday'])).days > 2:
                                    if abs(stringToDate(foundChild['Birthday']) - stringToDate(sibling['Birthday'])).days < 240:
                                        assert False, f" ERROR: Sibling Spacing: {foundChild['ID']} and {sibling['ID']} are not greater than 8 months apart or less than 2 days"
    return True