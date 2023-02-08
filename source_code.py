# Phill Anerine, Justus Neumeister, Rocco Vaccone, TaeSeo Um
# I pledge my honor that I have abided by the Stevens Honor System.

# Imports
from prettytable import PrettyTable
import pandas as pd

# Open the test_gedcom.ged file
gedcom_file = open('./test_gedcom.ged', 'r')

# Create a list of all the lines in the file and removing the '\n' character
gedcom_lines = [line[:-1] for line in gedcom_file.readlines()]

# Creating a list of all valid tags
valid_tags = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']
exception_valid_tags = ['INDI', 'FAM']

# Creating a PrettyTable for individuals
individual_table = PrettyTable()
individual_table.field_names = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']

# Creating a PrettyTable for families
family_table = PrettyTable()
family_table.field_names = ['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']

# Creating a DataFrame for individuals
individual_dataframe = pd.DataFrame(columns = ['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'])



# Open the output file
with open('./output.txt', 'w') as output_file:
    # Iterate through the list of lines
    for line in gedcom_lines:
        # Writing the line to the output file
        output_file.write('--> ' + line + '\n')
        
        # Split the line into a list of words
        split_line = line.split(' ')

        # Check if there is a valid tag
        if len(split_line) > 1 and split_line[1] in valid_tags:
            split_line.insert(2, 'Y')
        
        # Check if there is an exception valid tag
        elif len(split_line) > 2 and split_line[2] in exception_valid_tags:
            split_line.insert(1, split_line.pop(2))
            split_line.insert(2, 'Y')
        
        # If there is no valid tag
        else:
            split_line.insert(2, 'N')

        # Formatting the line
        finalized_line = '|'.join(split_line[:3]) + '|' + ' '.join(split_line[3:])

        # Writing the finalized line to the output file
        output_file.write('<-- ' + finalized_line + '\n')

# Printing out the individual and family tables
print(individual_table)
print(family_table)
