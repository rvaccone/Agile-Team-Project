# [US33] - Rocco
# List all multiple births in a GEDCOM file

from US_modules.helpers import findAttribute

# We should store the information in a class because we can then easily pass around the information and have many fields
class MultipleBirth:
        def __init__(self, fam_id, birthday, individuals=set()):
            self.fam_id = fam_id
            self.birthday = birthday
            self.individuals = individuals
        
        def add(self, child):
            self.children.add(child)

        # We need to define a function to make a consistent, comparable output
        def compare(self):
            return self.fam_id, self.birthday, self.individuals

def listMultipleBirths(ind_list, fam_list):
    # Considering multiple births to be 2 or more children born on the same day to the same parents

    # We are going to return a list with classes that contain the family id, birthday, and individuals
    multiple_births = []

    for fam in fam_list:
        # If there are less than 2 children in the family, we can skip it
        if (len(fam['Children']) < 2):
            continue

        # Computing a list of birthdays for the children in the family
        birthdays = [findAttribute(child, ind_list, 'Birthday') for child in fam['Children'] if findAttribute(child, ind_list, 'Birthday') != 'N/A']

        # Computing a set of birthdays that occur more than once
        common_birthdays = set([birthday for birthday in birthdays if birthdays.count(birthday) > 1])

        for birthday in common_birthdays:
            # Computing a list of children born on the same day
            children = [child_id for child_id in fam['Children'] if findAttribute(child_id, ind_list, 'Birthday') == birthday]

            # Adding the multiple birth to the list of multiple births
            multiple_births.append(MultipleBirth(fam['ID'], birthday, children))

    # Returning the list of multiple births
    return multiple_births

