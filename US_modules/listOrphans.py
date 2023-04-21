from datetime import datetime
from US_modules.helpers  import findKeyInArray
#US[33] - Phillip Anerine
#List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
def listOrphans(individual_list,family_list):
    orphans=[]
    today=datetime.now()
    for family in family_list:
        Husband, Wife = None, None
        for item in individual_list:
            if item['ID']==family['Husband ID']:
                Husband=item
            if item['ID']==family['Wife ID']:
                Wife=item
        if (not (Husband['Alive'] or Wife['Alive'])):
          for child_id in family['Children']:
              for individual in individual_list:
                  if (individual['ID']==child_id and individual['Age']<18): 
                      orphans.append(individual)
    return orphans