from datetime import datetime
from US_modules.helpers  import stringToDate
def listLargeAgeGaps(individual_list,family_list):
  couples=[]
  for family in family_list:
    Husband, Wife = None, None
    for individual in individual_list:
      if individual['ID']==family['Husband ID']:
        Husband=individual
      if individual['ID']==family['Wife ID']:
        Wife=individual
    marriage_date = stringToDate(family['Marriage Date'])
    husband_age_at_marriage = (marriage_date - stringToDate(Husband['Birthday'])).days//365
    wife_age_at_marriage = (marriage_date - stringToDate(Wife['Birthday'])).days//365
    if husband_age_at_marriage > 2 * wife_age_at_marriage or wife_age_at_marriage > 2 * husband_age_at_marriage:
        couples.append((Husband, Wife, family))

  return couples