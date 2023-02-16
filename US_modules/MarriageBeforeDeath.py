#Justus
from datetime import datetime, date
def MarriageBeforeDeath (individual_list,family_list):
    for family in family_list:
        if family['Marriage Date'] != 'N/A':
                for individual in individual_list:
                    if individual['ID'] == family['Husband ID']:
                        if individual['Death'] != 'N/A':
                            marriageDate = datetime.strptime(family['Marriage Date'], '%d %b %Y').date()
                            husbandDeathDate = datetime.strptime(individual['Death'], '%d %b %Y').date()
                            assert(marriageDate < husbandDeathDate), "Marriage date is after husband's death date"
                    

                    if individual['ID'] == family['Wife ID']:
                        if individual['Death'] != 'N/A':
                            marriageDate = datetime.strptime(family['Marriage Date'], '%d %b %Y').date()
                            wifeDeathDate = datetime.strptime(individual['Death'], '%d %b %Y').date()
                            assert(marriageDate < wifeDeathDate), "Marriage date is after wife's death date"