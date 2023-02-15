# Imported packages
import unittest

# Imported files
from projectDictionaries import *

import errorChecking as ec

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
    


checkIndividualNotTooOld()


