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
        # Check that each parent is not too old
        if individual['Age'] != 'N/A' and individual['Children'] != []:
            assert(int(individual['Age']) < 150, 'Individual is too old to be a parent')

        # Checking that each marriage is after when the individual is 14
        if individual['Age'] != 'N/A' and individual['Spouse'] != 'N/A':
            assert(int(individual['Age']) >= 14, 'Individual is too young to be married')

# Error checking the families
def families_error_checking(family_list):
    for family in family_list:
        pass