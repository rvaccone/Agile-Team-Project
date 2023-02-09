# Phill Anerine, Justus Neumeister, TaeSeo Um, Rocco Vaccone
# I pledge my honor that I have abided by the Stevens Honor System.

# Imports
from prettytable import PrettyTable
from datetime import datetime

# Open the test_gedcom.ged file
gedcom_file = open('./test_gedcom1.ged', 'r')

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
family_table.field_names = ['ID', 'Married', 'Divorced',
                            'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children']

individuals = []
curAssoc = ""
hasStarted = False
curIndi = []

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
        if (tag == "SEX" or tag == "FAMC" or tag == "HUSB" or tag == "WIFE"):
            if (tag == "SEX"):
                attribute = ["Gender", elements[2].strip()]
                curIndi.append(attribute)
            elif (tag == "FAMC"):
                attribute = ["Child", elements[2].strip()]
                curIndi.append(attribute)
            elif (tag == "HUSB"):
                attribute = ["Husband", elements[2].strip()]
                curIndi.append(attribute)
            elif (tag == "WIFE"):
                attribute = ["Wife", elements[2].strip()]
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
            attribute = [curAssoc, elements[2] +
                         " " + elements[3] + " " + elements[4]]
            curIndi.append(attribute)
            curAssoc = ""

    elif (hasStarted):
        if (tag == "BIRT" or tag == "DEAT"):
            if (tag == "BIRT"):
                curAssoc = "Birthday"
            elif (tag == "DEAT"):
                curAssoc = "Death"
        elif (tag == "DATE" and curAssoc != ""):
            attribute = [curAssoc, elements[2] +
                         " " + elements[3] + " " + elements[4]]
            curIndi.append(attribute)
            curAssoc = ""


# print(individuals)

def calculate_age(birthday):
    today = date.today()
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


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

    if individual_values['Birthday'] != 'N/A':
        if individual_values['Death'] == 'N/A':
            death_year = datetime.today().year
        else:
            death_year = int(individual_values['Death'].split()[-1])
        birth_year = int(individual_values['Birthday'].split()[-1])
        age = death_year - birth_year
        individual_values['Age'] = age

    # Adding the individual to the PrettyTable
    individual_table.add_row(individual_values.values())

# Printing the PrettyTable
print(individual_table)
