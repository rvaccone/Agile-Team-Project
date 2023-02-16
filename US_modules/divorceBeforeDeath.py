#[US06] - TaeSeo
import datetime 

def divorceBeforeDeath(family_list, individual_list):
    for family in family_list:
        if family['Divorce Date'] != 'N/A':
            for individual in individual_list:
                if individual['ID'] == family['Husband ID']:
                    if individual['Death'] != 'N/A':
                        divorceDate = datetime.strptime(family['Divorce Date'], '%d %b %Y').date()
                        husbandDeathDate = datetime.strptime(individual['Death'], '%d %b %Y').date()
                        assert(divorceDate < husbandDeathDate), "Divorce date is after husband's death date"
                

                if individual['ID'] == family['Wife ID']:
                    if individual['Death'] != 'N/A':
                        divorceDate = datetime.strptime(family['Divorce Date'], '%d %b %Y').date()
                        wifeDeathDate = datetime.strptime(individual['Death'], '%d %b %Y').date()
                        assert(divorceDate < wifeDeathDate), "Divorce date is after wife's death date"