def families_error_checking(family_list, individual_list):
    
     for family in family_list:
        # [US03] - Mateusz
         if family['Marriage Date'] != 'N/A':
             for individual in individual_list:
                 if individual['ID'] == family['Husband ID']:
                     if individual['Birthday'] != 'N/A':
                         MarriageDate = datetime.strptime(family['Marriage Date'], '%d %b %Y').date()
                         husbandBirthDate = datetime.strptime(individual['Birthday'], '%d %b %Y').date()
                         assert(husbandBirthDate < MarriageDate), "Husband birth date is after husband's Marriage date"
                

                 if individual['ID'] == family['Wife ID']:
                     if individual['Birthday'] != 'N/A':
                         MarriageDate = datetime.strptime(family['Marriage Date'], '%d %b %Y').date()
                         wifeBirthDate = datetime.strptime(individual['Birthday'], '%d %b %Y').date()
                         assert(wifeBirthDate < MarriageDate), "Wife birth date is after husband's Marriage date"