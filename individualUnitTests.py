# Imported packages
import unittest

# Imported files
from projectDictionaries import *

class IndividualTests(unittest.TestCase):
    # Initializing an empty list to contain all the individuals
    def __init__(self):
        self.individual_list = []

    # Creating a function to add an individual to the list
    def create_individual(self, individual_dict):
        self.individual_list.append(individual_dict.copy())

    # Creating a function to return the list of individuals
    def get_individual_list(self):
        return self.individual_list

# ProjectIndividualTests = IndividualTests()