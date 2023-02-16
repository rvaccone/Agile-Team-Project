# Imported packages
import unittest

# Imported files
from projectDictionaries import *
from individualUnitTests import *
import errorChecking as ec
from US_modules.DateBeforeCurrent import dateBeforeCurrentDate

class Family():
    # Initializing an empty list to contain all the families
    def __init__(self):
        self.family_list = []
        
    # Creating a function to add a family to the list
    def create_family(self, family_dict):
        family = family_dict.copy()
        self.family_list.append(family)
        return family

    def create_test_families(self, attribute, value, function):
        family = FamilyTests() 
        test_family = {
            "ID": "F",
            "Married": "1 JAN 2000",
            "Divorced": "N/A",
            "Husband ID": "I1",
            "Husband Name": "Richard /Ens/",
            "Wife ID": "I2",
            "Wife Name": "Mary /Ens/",
            "Children": []
        }[attribute] = value
        assert len(family_dict) == len(test_family), 'Error: dictionary length of test family does not match original family dictionary'
        try: 
            function(family.get_family_list())
            print(f"{function.__name__} Unit Test Success ✅")
        except AssertionError:
            print(f"Error: {AssertionError} on function {function.__name__} ❌")

    # Creating a function to return the list of families
    def get_family_list(self):
        return self.family_list


class FamilyTests(unittest.TestCase):
    def checkDatesBeforeCurrent():
        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '1 JAN 2025'
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '3 DEC 2010'
        try:
            dateBeforeCurrentDate(individual.get_individual_list(), family.get_family_list())
            print('Individual birthday is after current date:' + str(individual.get_individual_list()[0]['Birthday']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Death'] = '2 JAN 2020'
        try:
            ec.individuals_error_checking(individual.get_individual_list())
            print('Individual death date is after current date:' + str(individual.get_individual_list()[0]['Death']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Death']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Death'] = '20 DEC 2024'
        try:
            ec.individuals_error_checking(individual.get_individual_list())
            print('Individual death date is after current date:' + str(individual.get_individual_list()[0]['Death']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Death']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '15 JUL 1990'
        try:
            ec.individuals_error_checking(individual.get_individual_list())
            print('Individual birthday is after current date:' + str(individual.get_individual_list()[0]['Birthday']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '15 MAR 2023'
        try:
            ec.individuals_error_checking(individual.get_individual_list())
            print('Individual birthday is after current date:' + str(individual.get_individual_list()[0]['Birthday']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) )

