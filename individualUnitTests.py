# Imported packages
import unittest

# Imported files
from projectDictionaries import *
import errorChecking as ec
from US_modules.ageIsLessThan150 import ageIsLessThan150
from US_modules.birth_before_death import birth_before_death

class Individual():
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

class IndividualTests(unittest.TestCase):
    def checkIndividualNotTooOld(self):
        individual = Individual()
        individual.create_individual(individual_dict)['Age'] = 110
        try:
            ageIsLessThan150(individual.get_individual_list())
            print('Individual is not too old:' + str(individual.get_individual_list()[0]['Age']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Age']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Age'] = 160
        try:
            ageIsLessThan150(individual.get_individual_list())
            print('Individual is not too old:' + str(individual.get_individual_list()[0]['Age']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Age']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Age'] = 200
        try:
            ageIsLessThan150(individual.get_individual_list())
            print('Individual is not too old:' + str(individual.get_individual_list()[0]['Age']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Age']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Age'] = 30
        try:
            ageIsLessThan150(individual.get_individual_list())
            print('Individual is not too old:' + str(individual.get_individual_list()[0]['Age']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Age']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Age'] = 67
        try:
            ageIsLessThan150(individual.get_individual_list())
            print('Individual is not too old:' + str(individual.get_individual_list()[0]['Age']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Age']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '15 JUL 1990'
        individual.get_individual_list()[0]['Death'] = '16 JUL 1992'
        try:
            birth_before_death(individual.get_individual_list())
            print('Birth is Before Death:' + str(individual.get_individual_list()[0]['Birthday']) + ' | '+ str(individual.get_individual_list()[0]['Death']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) + ' | '+ str(individual.get_individual_list()[0]['Death']))

    def checkParentsNotTooOld(self):
        individual = Individual()
        individual.create_individual(individual_dict)['Age'] = 84
        individual.get_individual_list()[0]['Children'] = ['@I2@', '@I3@']
        try:
            us.Parents_not_too_old(individual.get_individual_list())
            print('Correctly passed with age:' + str(individual.get_individual_list()[0]['Age']))
        except AssertionError:
            print('Incorrectly submitted an error of: ')
        
        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '15 MAR 2002'
        individual.get_individual_list()[0]['Death'] = '17 MAR 2002'
        try:
            assert (individual.get_individual_list()[0]['Age'] < 150), 'Error: Individual is too old to be a parent'
        except AssertionError:
            print('Unsuccessfully errored with:')

        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '31 AUG 2005'
        individual.get_individual_list()[0]['Death'] = '30 AUG 2005'
        try:
            us.Parents_not_too_old(individual.get_individual_list())
            print('Individual is not too old to be a parent:' + str(individual.get_individual_list()[0]['Age']))
        except AssertionError:
            print('Failed successfully with error:')
        
        try:
            assert (individual.get_individual_list()[0]['Age'] < 150), 'Error: Individual is too old to be a parent'
        except AssertionError:
            print('Successfully errored with:' )

        try:
            assert (individual.get_individual_list()[0]['Age'] == 200), 'Error: Individual is too old to be a parent'
        except AssertionError:
            print('Ages do not align:')

# def outputTestResults(function):
#     with open('./output.txt', 'w') as f:
#         sys.stdout = open("./output.txt", "w")
#         try:
#             function()
#             f.write(f"{function.__name__} Unit Test Success ✅\n")
#         except AssertionError:
#             f.write(f"Error: {AssertionError} on function {function.__name__} ❌\n")

# individual_tests = IndividualTests()
# outputTestResults(individual_tests.checkIndividualNotTooOld)

if __name__ == '__main__':
    unittest.main()
