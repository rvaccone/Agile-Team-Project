# Imported packages
import unittest

# Imported files
from projectDictionaries import *
from individualUnitTests import *
import errorChecking as ec
>>>>>>> 04b7f61c36e15184f61b74e427ac5e3efe5eb713

class FamilyTests(unittest.TestCase):
    # Initializing an empty list to contain all the families
    def __init__(self):
        self.family_list = []
        
    # Creating a function to add a family to the list
    def create_family(self, family_dict):
        family = family_dict.copy()
        self.family_list.append(family)
        return family

    # Creating a function to return the list of families
    def get_family_list(self):
        return self.family_list
