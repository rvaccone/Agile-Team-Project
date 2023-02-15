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
    #US02
    birth_before_death(individual_list)
    for individual in individual_list:
        # [US07] - TaeSeo
        if individual['Age'] != 'N/A':
            assert(int(individual['Age']) < 150), "Individual is too old"

        # [US12] - Rocco 
        if individual['Age'] != 'N/A' and individual['Children'] != []:
            assert int(individual['Age']) < 150, "Individual is too old to be a parent"

        # [US10] - Rocco
        if individual['Age'] != 'N/A' and individual['Spouse'] != 'N/A':
            assert int(individual['Age']) >= 14, "Individual is too young to be married"

        # [US01] - Justus
        if individual['Birthday'] != 'N/A':
            date = individual['Birthday'].split()
            day, month, year = int(date[0]), int(
                datetime.strptime(date[1], "%b").month), int(date[2])
            curDay, curMonth, curYear = datetime.today().day, datetime.today().month, datetime.today().year
            assert(curYear > year or (year == curYear and curMonth > month) or (year == curYear and curMonth == month and day < curDay)), "Birth date is after today's date"

        # [US01] - Justus
        if individual['Death'] != 'N/A':
            date = individual['Death'].split()
            day, month, year = int(date[0]), int(
                datetime.strptime(date[1], "%b").month), int(date[2])
            curDay, curMonth, curYear = datetime.today().day, datetime.today().month, datetime.today().year
            assert(curYear > year or (year == curYear and curMonth > month) or (year == curYear and curMonth == month and day < curDay)), "Death date is after today's date"
    

# Error checking the families
def families_error_checking(family_list, individual_list):
    #US03
    birth_before_marriage(individual_list, family_list)
    for family in family_list:
        # [US06] - TaeSeo Um
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

        # [US01] - Justus
        if family['Marriage Date'] != 'N/A':
            date = datetime.strptime(family['Marriage Date'], '%d %b %Y').date()
            curDate = datetime.now()
            assert(date < curDate), "Marriage date is after today's date"
        if family['Divorce Date'] != 'N/A':
            date = datetime.strptime(family['Divorce Date'], '%d %b %Y').date()
            curDate = datetime.now()
            assert(date < curDate), "Divorce date is after today's date"

<<<<<<< HEAD
#Mateusz USER STORY 02
#If there are individuals in the list for whom birth and death dates are not both available, or all individuals were born after they died, the function will return False.
def birth_before_death(individuals):
    for individual in individuals:
        individual_values = {
            'ID': 'N/A',
            'Name': 'N/A',
            'Gender': 'N/A',
            'Birthday': 'N/A',
            'Age': 'N/A',
            'Alive': 'N/A',
            'Death': 'N/A',
            'Child': 'N/A',
            'Spouse': 'N/A'
        }

        for attributes in individual:
            individual_values[attributes[0]] = attributes[1]

        #if(individual_values['Death'] == 'N/A' and individual_values['Alive'] == 'True'):
        #    return True
        
        if(individual_values['Death'] == 'N/A' or individual_values['Birthday'] == 'N/A'):
            continue

        birthdate = individual_values['Birthday'].split()
        Birthday, Birthmon, Birthyear = birthdate[0], birthdate[1], birthdate[2]

        deathdate = individual_values['Death'].split()
        Deathday, Deathmon, Deathyear = deathdate[0], deathdate[1], deathdate[2]

        if(Deathyear > Birthyear):
            return True
        elif(Birthyear == Deathyear):
            if(datetime.strptime(Deathmon, '%b').month > datetime.strptime(Birthmon, '%b').month):
                return True
            if(datetime.strptime(Deathmon, '%b').month == datetime.strptime(Birthmon, '%b').month):
                if(Deathday >= Birthday):
                    return True
        else:
            print('ERR0R: Death was before birth')
            return False
        
    return False

=======
        # [US05] - Justus

    
    