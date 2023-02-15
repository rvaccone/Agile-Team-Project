from datetime import datetime, date

# Initial error checking of incorrect lines
def initial_error_checking(gedcom_lines):
    for index, line in enumerate(gedcom_lines):
        # if the line is a level 0 tag
        if line[0] == "0":
            pass

        # if the line is a level 1 tag
        elif line[0] == "1":
            # Asserting that 1 DATE is not present
            assert(line.split()[-1] != "DATE")

        # if the line is a level 2 tag
        elif line[0] == "2":
            # Asserting that 2 NAME is not present
            assert(line.split()[1] != "NAME")

# Error checking the individuals
def individuals_error_checking(individual_list):
    for individual in individual_list:
        # [US07] - TaeSeo
        if individual['Age'] != 'N/A':
            assert(int(individual['Age']) < 150)

        # [US12] - Rocco 
        if individual['Age'] != 'N/A' and individual['Children'] != []:
            assert(int(individual['Age']) < 150, 'Individual is too old to be a parent')

        # [US10] - Rocco
        if individual['Age'] != 'N/A' and individual['Spouse'] != 'N/A':
            assert(int(individual['Age']) >= 14, 'Individual is too young to be married')

        # [US01] - Justus
        if individual['Birthday'] != 'N/A':
            date = individual['Birthday'].split()
            day, month, year = int(date[0]), int(
                datetime.strptime(date[1], "%b").month), int(date[2])
            curDay, curMonth, curYear = datetime.today().day, datetime.today().month, datetime.today().year
            assert(curYear > year or (year == curYear and curMonth > month) or (year == curYear and curMonth == month and day < curDay))

        # [US01] - Justus
        if individual['Death'] != 'N/A':
            date = individual['Death'].split()
            day, month, year = int(date[0]), int(
                datetime.strptime(date[1], "%b").month), int(date[2])
            curDay, curMonth, curYear = datetime.today().day, datetime.today().month, datetime.today().year
            assert(curYear > year or (year == curYear and curMonth > month) or (year == curYear and curMonth == month and day < curDay))
    

# Error checking the families
def families_error_checking(family_list, individual_list):
    for family in family_list:
        # [US06] - TaeSeo
        if family['Marriage Date'] != 'N/A' and family['Divorce Date'] and family['Husband ID'] != 'N/A' and family['Wife ID'] != 'N/A':
            for individual in individual_list:
                if individual['ID'] == family['Husband ID']:
                    divorceDate = datetime.strptime(family['Divorce Date'], '%d %b %Y')
                    husbandDeathDate = datetime.strptime(individual['Death'], '%d %b %Y')
                    assert(divorceDate < husbandDeathDate)

                if individual['ID'] == family['Wife ID']:
                    divorceDate = datetime.strptime(family['Divorce Date'], '%d %b %Y')
                    wifeDeathDate = datetime.strptime(individual['Death'], '%d %b %Y')
                    assert(divorceDate < wifeDeathDate)

        # [US05] - Justus
        
    
    