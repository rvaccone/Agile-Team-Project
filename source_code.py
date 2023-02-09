# Phill Anerine, Mateusz Marciniak, Justus Neumeister, TaeSeo Um, Rocco Vaccone
# I pledge my honor that I have abided by the Stevens Honor System.

# Imports
from prettytable import PrettyTable
from datetime import datetime, date

# Open the test_gedcom.ged file
gedcom_file = open('./test_gedcom.ged', 'r')

# Create a list of all the lines in the file and removing the '\n' character
gedcom_lines = [line[:-1] for line in gedcom_file.readlines()]

# Creating a list of all valid tags
valid_tags = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR',
              'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD', 'TRLR', 'NOTE']
exception_valid_tags = ['INDI', 'FAM']

# Creating a PrettyTable for individuals
individual_table = PrettyTable()
individual_table.field_names = [
    'ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse']

# Creating a PrettyTable for families
family_table = PrettyTable()
family_table.field_names = ['ID', 'Marriage Date', 'Divorce Date',
                            'Husband ID', 'Wife ID', 'Children']

# for line in gedcom_lines:
#     assert line[0] != '', 'Error: Invalid level'

individuals = []
curAssoc = ""
hasStarted = False
curIndi = []

families = []
curFam = []

for line in gedcom_lines:
    # Splitting the line into a list of elements
    elements = line.split(" ")

    if (elements[0] == "0" and hasStarted == False and len(elements) > 2 and elements[2] == "INDI"):
        hasStarted = True

    if (hasStarted and elements[0] == "0" and len(elements) > 2 and elements[2] == "INDI"):
        hasStarted = True
        if (len(curIndi) > 0):
            individuals.append(curIndi)
            curIndi = []
        attribute = ["ID", elements[1].strip()]
        curIndi.append(attribute)
    elif (hasStarted and len(elements) > 1):
        tag = elements[1].strip()
        if (tag == "SEX" or tag == "FAMC" or tag == "FAMS"):
            if (tag == "SEX"):
                attribute = ["Gender", elements[2].strip()]
                curIndi.append(attribute)
            elif (tag == "FAMC"):
                attribute = ["Child", elements[2].strip()]
                curIndi.append(attribute)
            elif (tag == "FAMS"):
                attribute = ["Spouse", elements[2].strip()]
                curIndi.append(attribute)
        elif (tag == "NAME"):
            if (len(elements) > 3):
                attribute = ["Name", elements[2] + " /" + elements[3].strip()]
                curIndi.append(attribute)
            else:
                attribute = ["Name", elements[2].strip()]
                curIndi.append(attribute)
        elif (tag == "BIRT" or tag == "DEAT"):
            if (tag == "BIRT"):
                curAssoc = "Birthday"
            elif (tag == "DEAT"):
                curAssoc = "Death"
        elif (tag == "DATE" and curAssoc != ""):
            if (curAssoc == "Birthday" or curAssoc == "Death"):
                attribute = [curAssoc, elements[2] +
                             " " + elements[3] + " " + elements[4]]
                curIndi.append(attribute)
                curAssoc = ""
            else:
                attribute = [curAssoc, elements[2] +
                             " " + elements[3] + " " + elements[4]]
                curFam.append(attribute)
                curAssoc = ""
        elif (elements[0] == "0" and len(elements) > 2 and elements[2] == "FAM"):
            if (len(curFam) > 0):
                families.append(curFam)
                curFam = []
            attribute = ["Family ID", elements[1].strip()]
            curFam.append(attribute)
        elif (tag == "HUSB"):
            attribute = ["Husband ID", elements[2].strip()]
            curFam.append(attribute)
        elif (tag == "WIFE"):
            attribute = ["Wife ID", elements[2].strip()]
            curFam.append(attribute)
        elif (tag == "CHIL"):
            attribute = ["Children ID(s)", elements[2].strip()]
            curFam.append(attribute)
        if (tag == "MARR" or tag == "DIV"):
            if (tag == "MARR"):
                curAssoc = "Marriage Date"
            elif (tag == "DIV"):
                curAssoc = "Divorce Date"
        elif (tag == "DATE" and curAssoc != ""):
            if (curAssoc == "Birthday" or curAssoc == "Death"):
                attribute = [curAssoc, elements[2] +
                             " " + elements[3] + " " + elements[4]]
                curIndi.append(attribute)
                curAssoc = ""
            else:
                attribute = [curAssoc, elements[2] +
                             " " + elements[3] + " " + elements[4]]
                curFam.append(attribute)
                curAssoc = ""

    elif (hasStarted):
        if (tag == "BIRT" or tag == "DEAT"):
            if (tag == "BIRT"):
                curAssoc = "Birthday"
            elif (tag == "DEAT"):
                curAssoc = "Death"
        if (tag == "MARR" or tag == "DIV"):
            if (tag == "MARR"):
                curAssoc = "Marriage Date"
            elif (tag == "DIV"):
                curAssoc = "Divorce Date"
        elif (tag == "DATE" and curAssoc != ""):
            if (curAssoc == "Birthday" or curAssoc == "Death"):
                attribute = [curAssoc, elements[2] +
                             " " + elements[3] + " " + elements[4]]
                curIndi.append(attribute)
                curAssoc = ""
            else:
                attribute = [curAssoc, elements[2] +
                             " " + elements[3] + " " + elements[4]]
                curFam.append(attribute)
                curAssoc = ""

if (len(curIndi) != 0):
    individuals.append(curIndi)
if (len(curFam) != 0):
    families.append(curFam)


# Iterating through the individuals list and adding them to the PrettyTable
for individual in individuals:
    # Creating a dictionary of all the values for the individual
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

    # Iterating through the attributes of the individual
    for attributes in individual:
        individual_values[attributes[0]] = attributes[1]

    individual_values['Alive'] = True if individual_values['Death'] == 'N/A' else False

    # Calculating the age of the individual
    if individual_values['Birthday'] != 'N/A':
        if individual_values['Death'] == 'N/A':
            death_day, death_month, death_year = datetime.today(
            ).day, datetime.today().month, datetime.today().year
        else:
            death_split = individual_values['Death'].split()
            death_day, death_month, death_year = int(death_split[0]), int(
                datetime.strptime(death_split[1], "%b").month), int(death_split[2])

        # Getting the birthday information
        birthday_split = individual_values['Birthday'].split()
        birth_day, birth_month, birth_year = int(birthday_split[0]), int(
            datetime.strptime(birthday_split[1], "%b").month), int(birthday_split[2])

        # Calculating the age using an equation
        age = death_year - birth_year - \
            ((death_month, death_day) < (birth_month, birth_day))

    if individual_values['Birthday'] != 'N/A':
        if individual_values['Death'] == 'N/A':
            death_year = datetime.today().year
            # print(datetime.today().month + (datetime.today().day / 100))
        else:
            death_year = int(individual_values['Death'].split()[-1])
        birth_year = int(individual_values['Birthday'].split()[-1])
        age = death_year - birth_year

        individual_values['Age'] = age

    # Adding the individual to the PrettyTable
    individual_table.add_row(individual_values.values())

# Adding the families to the PrettyTable
for family in families:
    family_values = {
        'Family ID': 'N/A',
        'Marriage Date': 'N/A',
        'Divorce Date': 'N/A',
        'Husband ID': 'N/A',
        'Wife ID': 'N/A',
        'Children ID(s)': ['N/A']
    }

    for attributes in family:
        if attributes[0] == 'Children ID(s)':
            family_values['Children ID(s)'].append(attributes[1])
        else:
            family_values[attributes[0]] = attributes[1]

    if len(family_values['Children ID(s)']) > 1:
        family_values['Children ID(s)'] = family_values['Children ID(s)'][1:]

    family_table.add_row(family_values.values())

# Printing the PrettyTable
print(individual_table)
print(family_table)

# Writing the PrettyTable to an output file
with open('./output.txt', 'w') as output_file:
    output_file.write(str(individual_table) + '\n')
    output_file.write(str(family_table) + '\n')
