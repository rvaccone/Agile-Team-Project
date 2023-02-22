#[US06] - TaeSeo
import datetime 

import datetime 

def is_divorce_before_death(person_id, death_date, divorce_date):
    if death_date != 'N/A':
        death_date = datetime.strptime(death_date, '%d %b %Y').date()
        divorce_date = datetime.strptime(divorce_date, '%d %b %Y').date()
        assert(divorce_date < death_date), f"Divorce date is after {person_id}'s death date"

def divorceBeforeDeath(individual_list, family_list):
    for family in family_list:
        if family['Divorce Date'] != 'N/A':
            for individual in individual_list:
                if individual['ID'] == family['Husband ID']:
                    is_divorce_before_death('husband', individual['Death'], family['Divorce Date'])

                if individual['ID'] == family['Wife ID']:
                    is_divorce_before_death('wife', individual['Death'], family['Divorce Date'])
