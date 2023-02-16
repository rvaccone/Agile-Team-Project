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


