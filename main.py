# Imported packages
from prettytable import PrettyTable
from datetime import datetime, date

# Imported files
import errorChecking as ec
from projectDictionaries import *

# Open the test_gedcom.ged file as a read-only
gedcom_file = open("./test_gedcom.ged", "r")

# Create a list of all the lines in the file and removing the '\n' character
gedcom_lines = [line[:-1] for line in gedcom_file.readlines()]

# Initial error checking of incorrect lines
ec.initial_error_checking(gedcom_lines)

# Creating lists to contain all the individuals and families
individual_list, family_list = [], []

# Creating tables to contain the individuals and families
individual_table, family_table = PrettyTable(), PrettyTable()
individual_table.field_names, family_table.field_names = individual_dict.keys(), family_dict.keys()

# Iterating through the lines in the gedcom file
for index, line in enumerate(gedcom_lines):
    #  If the line is a level 0 tag
    if line[0] == "0":
        # If the line is an individual, add a new individual to the list
        if line.split()[-1] == "INDI":
            individual_list.append(individual_dict.copy())
            individual_list[-1]["ID"] = line.split()[1]

        # If the line is a family, add a new family to the list
        elif line.split()[-1] == "FAM":
            family_list.append(family_dict.copy())
            family_list[-1]["ID"] = line.split()[1]

    # if the line is a level 1 tag
    elif line[0] == "1":
        # Adding values to the individual dictionary that are in the individual map
        try:
            tag = gedcom_individual_map[line.split()[1]]
            individual_list[-1][tag] = line.split()[2]
        except:
            pass

        # Determining the individual's family
        if line.split()[1] == "FAMC":
            individual_list[-1]["Family"] = line.split()[2]

        # Adding values to the family dictionary that are in the family map
        try:
            tag = gedcom_family_map[line.split()[1]]
            family_list[-1][tag] = line.split()[2]
        except:
            pass

    # If the line is a level 2 tag
    elif line[0] == "2":
        # If there is a date
        if line.split()[1] == "DATE":
            date = line[7:]
            # If the date corresponds to a birthday
            if gedcom_lines[index - 1].split()[-1] == "BIRT":
                individual_list[-1]["Birthday"] = date

            # If the date corresponds to a death
            elif gedcom_lines[index - 1].split()[1] == "DEAT":
                individual_list[-1]["Death"] = date
                individual_list[-1]["Alive"] = False

            # If the date corresponds to a marriage
            elif gedcom_lines[index - 1].split()[-1] == "MARR":
                family_list[-1]["Marriage Date"] = date

            # If the date corresponds to a divorce
            elif gedcom_lines[index - 1].split()[-1] == "DIV":
                family_list[-1]["Divorce Date"] = date

# Calculating attributes of the individuals
for individual in individual_list:
    # Calculating the age of each individual
    if individual['Birthday'] != 'N/A':
            if individual['Death'] == 'N/A':
                death_year = datetime.today().year
            else:
                death_year = int(individual['Death'].split()[-1])
            birth_year = int(individual['Birthday'].split()[-1])
            individual['Age'] = death_year - birth_year

# Calculating attributes of the families
for family in family_list:
    # Calculating the children of each family
    family_children = [individual['ID'] for individual in individual_list if individual['Family'] == family['ID']]
    family['Children'] = family_children
    # For convenience, adding the children to the parents
    for parent in [individual for individual in individual_list if (individual['ID'] == family['Wife ID'] or individual['ID'] == family['Husband ID'])]:
        parent['Children'] = parent['Children'] + family_children

# Error checking the individuals
ec.individuals_error_checking(individual_list)

# Error checking the families
ec.families_error_checking(family_list, individual_list)

# Adding the individuals to the individual table
for individual in individual_list:
    individual_table.add_row(individual.values())

# Adding the families to the family table
for family in family_list:
    family_table.add_row(family.values())

print(individual_table)
print(family_table)
