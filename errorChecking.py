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
            assert(int(individual['Age']) < 150)

        # [US10] - Rocco
        if individual['Age'] != 'N/A' and individual['Spouse'] != 'N/A':
            assert(int(individual['Age']) >= 14)

    

# Error checking the families
def families_error_checking(family_list, individual_list):
    for family in family_list:
        # if marriage date is after death date of either spouse, assert false
        if family['Marriage Date'] != 'N/A' and family['Divorce Date'] and family['Husband ID'] != 'N/A' and family['Wife ID'] != 'N/A':
            for individual in individual_list:
                
