# Imported packages
import unittest

# Imported files
from projectDictionaries import *
import errorChecking as ec
from US_modules.ageIsLessThan150 import ageIsLessThan150

class IndividualTests(unittest.TestCase):
    # Initializing an empty list to contain all the individuals
    def __init__(self):
        self.individual_list = []

    # Creating a function to add an individual to the list
    def create_individual(self, individual_dict):
        individual = individual_dict.copy()
        self.individual_list.append(individual)
        return individual

    # Creating a function to return the list of individuals
    def get_individual_list(self):
        return self.individual_list
        
    def create_test_individuals(self, attribute, value, function):
        individual = IndividualTests() 
        test_individual = {
            "ID": "I",
            "Name": "Richard /Ens/",
            "Sex": "M",
            "Birthday": "1 JAN 2000",
            "Age": "40",
            "Alive": True,
            "Death": "N/A",
            "Family": "F1",
            "Spouse": "I2",
            "Children": []
        }[attribute] = value
        assert len(individual_dict) == len(test_individual), 'Error: dictionary length of test individual does not match original individual dictionary'
        try: 
            function(individual.get_individual_list())
            print(f"{function.__name__} Unit Test Success ✅")
        except AssertionError:
            print(f"Error: {AssertionError} on function {function.__name__} ❌")


def checkIndividualNotTooOld():
    individual = IndividualTests()
    individual.create_individual(individual_dict)['Age'] = 200
    try:
        ec.individuals_error_checking(individual.get_individual_list())
        print('Individual is not too old:' + str(individual.get_individual_list()[0]['Age']))
    except:
        print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Age']) )

    individual = IndividualTests()
    individual.create_individual(individual_dict)['Age'] = 100
    try:
        ec.individuals_error_checking(individual.get_individual_list())
        print('Individual is not too old:' + str(individual.get_individual_list()[0]['Age']))
    except:
        print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Age']) )

    individual = IndividualTests()
    individual.create_individual(individual_dict)['Age'] = 70
    try:
        ec.individuals_error_checking(individual.get_individual_list())
        print('Individual is not too old:' + str(individual.get_individual_list()[0]['Age']))
    except:
        print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Age']) )

    individual = IndividualTests()
    individual.create_individual(individual_dict)['Age'] = 300
    try:
        ec.individuals_error_checking(individual.get_individual_list())
        print('Individual is not too old:' + str(individual.get_individual_list()[0]['Age']))
    except:
        print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Age']) )


    individual = IndividualTests()
    individual.create_individual(individual_dict)['Age'] = 10
    try:
        ec.individuals_error_checking(individual.get_individual_list())
        print('Individual is not too old:' + str(individual.get_individual_list()[0]['Age']))
    except:
        print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Age']) )

def checkDatesBeforeCurrent():
    individual = IndividualTests()
    individual.create_individual(individual_dict)['Birthday'] = '1 JAN 2025'
    try:
        ec.individuals_error_checking(individual.get_individual_list())
        print('Individual birthday is after current date:' + str(individual.get_individual_list()[0]['Birthday']))
    except:
        print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) )

    individual = IndividualTests()
    individual.create_individual(individual_dict)['Death'] = '2 JAN 2020'
    try:
        ec.individuals_error_checking(individual.get_individual_list())
        print('Individual death date is after current date:' + str(individual.get_individual_list()[0]['Death']))
    except:
        print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Death']) )

    individual = IndividualTests()
    individual.create_individual(individual_dict)['Death'] = '20 DEC 2024'
    try:
        ec.individuals_error_checking(individual.get_individual_list())
        print('Individual death date is after current date:' + str(individual.get_individual_list()[0]['Death']))
    except:
        print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Death']) )

    individual = IndividualTests()
    individual.create_individual(individual_dict)['Birthday'] = '15 JUL 1990'
    try:
        ec.individuals_error_checking(individual.get_individual_list())
        print('Individual birthday is after current date:' + str(individual.get_individual_list()[0]['Birthday']))
    except:
        print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) )

    individual = IndividualTests()
    individual.create_individual(individual_dict)['Birthday'] = '15 MAR 2023'
    try:
        ec.individuals_error_checking(individual.get_individual_list())
        print('Individual birthday is after current date:' + str(individual.get_individual_list()[0]['Birthday']))
    except:
        print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) )