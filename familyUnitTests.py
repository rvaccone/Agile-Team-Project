# Imported packages
import unittest

# Imported files
from projectDictionaries import *

class FamilyTests(unittest.TestCase):
    # Initializing an empty list to contain all the families
    def __init__(self):
        self.family_list = []
        
    # Creating a function to add a family to the list
    def create_family(self, family_dict):
        self.family_list.append(family_dict.copy())

    # Creating a function to return the list of families
    def get_family_list(self):
        return self.family_list
