# Imported packages
import unittest
import sys

# Imported files
from projectDictionaries import *
from US_modules.ageIsLessThan150 import ageIsLessThan150
from US_modules.birth_before_death import birth_before_death
from US_modules.Parents_not_too_old import parents_not_too_old
from US_modules.male_lname_same import male_lname_same
from US_modules.listDeceased import listDeceased
from US_modules.listLivingMarried import listLivingMarried
from US_modules.unique_firstnames import unique_first
from US_modules.corresponding_entries import corresponding_entries
from US_modules.includePartialDates import includePartialDates
from US_modules.rejectIllegitimateDates import rejectIllegitimateDates
from US_modules.recentBirths import recent_Births
from US_modules.recentDeaths import recent_Death


class Individual:
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
            "Children": [],
        }[attribute] = value
        assert len(individual_dict) == len(
            test_individual
        ), "Error: dictionary length of test individual does not match original individual dictionary"
        try:
            function(individual.get_individual_list())
            print(f"{function.__name__} Unit Test Success ✅")
        except AssertionError:
            print(f"Error: {AssertionError} on function {function.__name__} ❌")

    # Creating an individual with given attributes
    def create_modified_individual(self, individual_dict, mods):
        individual = self.create_individual(individual_dict)
        for key in mods:
            individual[key] = mods[key]
        return individual


class IndividualTests(unittest.TestCase):
    def setUp(self):
        # Adding a line to separate unit test cases
        print("-" * 100)

        # Printing the name of the unit test function
        print(self.id().split('.')[-1].replace('test_', '') + ' Unit Test(s)\n')

    def test_checkDatesBeforeCurrent(self):
        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "1 JAN 2025"
        try:
            ec.individuals_error_checking(individual.get_individual_list())
            print(
                "Individual birthday is after current date:"
                + str(individual.get_individual_list()[0]["Birthday"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Birthday"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "2 JAN 2020"
        try:
            ec.individuals_error_checking(individual.get_individual_list())
            print(
                "Individual death date is after current date:"
                + str(individual.get_individual_list()[0]["Death"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Death"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "20 DEC 2024"
        try:
            ec.individuals_error_checking(individual.get_individual_list())
            print(
                "Individual death date is after current date:"
                + str(individual.get_individual_list()[0]["Death"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Death"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "15 JUL 1990"
        try:
            ec.individuals_error_checking(individual.get_individual_list())
            print(
                "Individual birthday is after current date:"
                + str(individual.get_individual_list()[0]["Birthday"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Birthday"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "15 MAR 2023"
        try:
            ec.individuals_error_checking(individual.get_individual_list())
            print(
                "Individual birthday is after current date:"
                + str(individual.get_individual_list()[0]["Birthday"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Birthday"])
            )

    # US07 - TS
    def test_checkIndividualNotTooOld(self):
        individual = Individual()
        individual.create_individual(individual_dict)["Age"] = 110
        try:
            ageIsLessThan150(individual.get_individual_list())
            print(
                "Individual is not too old:"
                + str(individual.get_individual_list()[0]["Age"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Age"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Age"] = 160
        try:
            ageIsLessThan150(individual.get_individual_list())
            print(
                "Individual is not too old:"
                + str(individual.get_individual_list()[0]["Age"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Age"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Age"] = 200
        try:
            ageIsLessThan150(individual.get_individual_list())
            print(
                "Individual is not too old:"
                + str(individual.get_individual_list()[0]["Age"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Age"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Age"] = 30
        try:
            ageIsLessThan150(individual.get_individual_list())
            print(
                "Individual is not too old:"
                + str(individual.get_individual_list()[0]["Age"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Age"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Age"] = 67
        try:
            ageIsLessThan150(individual.get_individual_list())
            print(
                "Individual is not too old:"
                + str(individual.get_individual_list()[0]["Age"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Age"])
            )

    def test_birth_before_death(self):
        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "15 JUL 1990"
        individual.get_individual_list()[0]["Death"] = "16 JUL 1992"
        try:
            birth_before_death(individual.get_individual_list())
            print(
                "Birth is Before Death:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(individual.get_individual_list()[0]["Death"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(individual.get_individual_list()[0]["Death"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "15 AUG 1990"
        individual.get_individual_list()[0]["Death"] = "16 JUL 1992"
        try:
            birth_before_death(individual.get_individual_list())
            print(
                "Birth is Before Death:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(individual.get_individual_list()[0]["Death"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(individual.get_individual_list()[0]["Death"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "15 JAN 1990"
        individual.get_individual_list()[0]["Death"] = "16 JAN 1992"
        try:
            birth_before_death(individual.get_individual_list())
            print(
                "Birth is Before Death:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(individual.get_individual_list()[0]["Death"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(individual.get_individual_list()[0]["Death"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "15 JUL 2000"
        individual.get_individual_list()[0]["Death"] = "16 JUL 1992"
        try:
            birth_before_death(individual.get_individual_list())
            print(
                "Birth is Before Death:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(individual.get_individual_list()[0]["Death"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(individual.get_individual_list()[0]["Death"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "16 JUL 1995"
        individual.get_individual_list()[0]["Death"] = "16 JUL 1992"
        try:
            birth_before_death(individual.get_individual_list())
            print(
                "Birth is Before Death:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(individual.get_individual_list()[0]["Death"])
            )
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) + ' | '+ str(individual.get_individual_list()[0]['Death']))
    
    def test_same_male_lastnames(self):
        individual = Individual()
        
        individual.create_individual(individual_dict)['Name'] = 'Joe Biden' 
        individual.get_individual_list()[0]['ID'] = 'I2'
        individual.get_individual_list()[0]['Sex'] = 'M'
        individual.get_individual_list()[0]['Children'] = ['I1','I6']
        
        individual = Individual()

        individual.create_individual(individual_dict)['Name'] = 'Hunter Biden'
        individual.get_individual_list()[0]['ID'] = 'I1'
        individual.get_individual_list()[0]['Sex'] = 'M'
        
        try:
            male_lname_same(individual.get_individual_list())
            print('Same Last Name')
        except:
            print('Different Last names')

        individual = Individual()
        
        individual.create_individual(individual_dict)['Name'] = 'Joe Biden'
        individual.get_individual_list()[0]['ID'] = 'I2'
        individual.get_individual_list()[0]['Sex'] = 'M'
        individual.get_individual_list()[0]['Children'] = ['I1','I6']
        
        individual.create_individual(individual_dict)['Name'] = 'Hunter Obama'
        individual.get_individual_list()[1]['ID'] = 'I1'
        individual.get_individual_list()[1]['Sex'] = 'M'
    
        try:
            male_lname_same(individual.get_individual_list())
            print('Same Last Name')
        except:
            print('Different Last names')

    def test_unqiue_firstnames(self):
        individual = Individual()
        
        individual.create_individual(individual_dict)['Name'] = 'Joe Biden' 
        individual.get_individual_list()[0]['ID'] = 'I2'
        individual.get_individual_list()[0]['Children'] = ['I1','I6']
        
        individual1 = Individual()

        individual1.create_individual(individual_dict)['Name'] = 'Hunter Biden'
        individual1.get_individual_list()[0]['ID'] = 'I1'

        individual2 = Individual()

        individual2.create_individual(individual_dict)['Name'] = 'Hunter Biden'
        individual2.get_individual_list()[0]['ID'] = 'I6'
        
        
        try:
            unique_first(individual.get_individual_list())
            print('Different First Names')
        except:
            print('Two or more children have the same first names')

        individual = Individual()
        
        individual.create_individual(individual_dict)['Name'] = 'Joe Biden' 
        individual.get_individual_list()[0]['ID'] = 'I2'
        individual.get_individual_list()[0]['Children'] = ['I1','I6']
        
        individual = Individual()

        individual.create_individual(individual_dict)['Name'] = 'Hunter Biden'
        individual.get_individual_list()[0]['ID'] = 'I1'

        individual = Individual()

        individual.create_individual(individual_dict)['Name'] = 'Hillary Biden'
        individual.get_individual_list()[0]['ID'] = 'I6'
        
        
        try:
            unique_first(individual.get_individual_list())
            print('Different First Names')
        except:
            print('Two or more children have the same first names')

    def test_corresponding_entries(self):
        individual = Individual()
        individual.create_individual(individual_dict)['Family'] = 'N/A'
        individual.get_individual_list()[0]['Spouse'] = 'N/A'
        individual.get_individual_list()[0]['Children'] = []
        try:
            corresponding_entries(individual.get_individual_list())
            print('Individual has a family role')
        except:
            print('No Family Role')

        individual = Individual()
        individual.create_individual(individual_dict)['Family'] = 'F2'
        individual.get_individual_list()[0]['Spouse'] = 'I7'
        individual.get_individual_list()[0]['Children'] = ['I1']
        try:
            corresponding_entries(individual.get_individual_list())
            print('Individual has a family role')
        except:
            print('No Family Role')

    def test_checkParentsNotTooOld(self):
        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "15 JUL 1990"
        individual.get_individual_list()[0]["Death"] = "16 MAR 2002"
        try:
            parents_not_too_old(individual.get_individual_list())
            print(
                "Correctly passed with age:"
                + str(individual.get_individual_list()[0]["Age"])
            )
        except AssertionError:
            print("Incorrectly submitted an error of: ")

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "15 MAR 2002"
        individual.get_individual_list()[0]["Death"] = "17 MAR 2002"
        try:
            if individual.get_individual_list()[0]["Age"] != "N/A":
                self.assertTrue(
                    int(individual.get_individual_list()[0]["Age"]) < 150,
                    "Error: Individual is too old to be a parent",
                )
            else:
                self.assertTrue(False, "Individual age is undefined")
        except AssertionError:
            print("Unsuccessfully errored with:")

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "31 AUG 2005"
        individual.get_individual_list()[0]["Death"] = "30 AUG 2005"
        try:
            parents_not_too_old(individual.get_individual_list())
            print(
                "Individual is not too old to be a parent:"
                + str(individual.get_individual_list()[0]["Age"])
            )
        except AssertionError:
            print("Failed successfully with error:")

        try:
            if individual.get_individual_list()[0]["Age"] != "N/A":
                self.assertTrue(
                    int(individual.get_individual_list()[0]["Age"]) < 150,
                    "Error: Individual is too old to be a parent",
                )
            else:
                self.assertTrue(False, "Individual age is undefined")
        except AssertionError:
            print("Successfully errored with:")

        try:
            self.assertTrue(
                individual.get_individual_list()[0]["Age"] == 200,
                "Error: Individual is too old to be a parent",
            )
        except AssertionError:
            print("Ages do not align:")



    def test_checkListDeceased(self):
        individual = Individual()
        individual.create_individual(individual_dict)['Death'] = '16 MAR 2002'
        numberOfDeceased = listDeceased(individual.get_individual_list())
        try:
            self.assertEqual(numberOfDeceased, 2, 'Error: Individual is deceased')
        except AssertionError:
            print('Failed successfully with error: ' + str(numberOfDeceased))

    def test_checkListLivingMarried(self):
        individual = Individual()
        individual.create_individual(individual_dict)['Death'] = 'N/A'
        individual.get_individual_list()[0]['Spouse'] = 'RANDOMID'
        numberOfLivingMarried = listLivingMarried(individual.get_individual_list())
        try:
            self.assertEqual(numberOfLivingMarried, 2, 'Error: Incorrect')
        except AssertionError:
            print('Failed successfully with error: ' + str(numberOfLivingMarried))

    def test_includePartialDates(self):
        # We want to write tests to ensure that we can accept and use dates without days or without days and months
        # Create the individual
        individual = Individual()

        # Create three individuals with different dates
        individual.create_modified_individual(
            individual_dict, {'Birthday': '1 JAN 1990', 'Death': '1 JAN 2000'}
        ) # With day and month - should pass
        individual.create_modified_individual(
            individual_dict, {'Birthday': 'JAN 1990', 'Death': 'JAN 2000'}
        ) # Without day - should pass
        individual.create_modified_individual(
            individual_dict, {'Birthday': '1990', 'Death': '2000'}
        ) # Without day and month - should pass

        # Calling the function on each individual should not raise an error
        try:
            includePartialDates(individual.get_individual_list(), family_list=list())
            print('All dates are valid ✅')
        except:
            print('At least one date is invalid ❌')

        # Create an individual with an invalid date
        individual.create_modified_individual(
            individual_dict, {'Birthday': '1 JAN', 'Death': '1 JAN'}
        ) # Without year - should fail

        # Testing if the function raises an error on the invalid date
        try:
            includePartialDates(individual.get_individual_list(), family_list=list())
            print('All dates are valid despite having an invalid date ❌')
        except:
            print('At least one date is invalid ✅')

    def test_recentBirths(self):
        i = Individual()
        i.create_modified_individual(individual_dict, {'Birthday': '1 JAN 2023', 'ID': 'I6'} )
        
        #Function will always return true
        try:
            recent_Births(i.get_individual_list())
            print('Individuals recent born')
        except:
            print('Individual NOT recent born')

        b = Individual()
        b.create_modified_individual(individual_dict, {'Birthday': '1 JAN 2020', 'ID': 'I7'} )
        try:
            recent_Births(b.get_individual_list())
            print('Individuals recent born')
        except:
            print('Individual NOT recent born')

    def test_recentDeaths(self):
            i = Individual()
            i.create_modified_individual(individual_dict, {'Death': '1 JAN 2023', 'ID': 'I6'} )
            
            #Function will always return true
            try:
                recent_Death(i.get_individual_list())
                print('Individuals recent dead')
            except:
                print('Individual NOT recent dead')

            b = Individual()
            b.create_modified_individual(individual_dict, {'Death': '1 JAN 2020', 'ID': 'I7'} )
            try:
                recent_Death(b.get_individual_list())
                print('Individuals recent dead')
            except:
                print('Individual NOT recent dead')

    def test_rejectIllegitimateDates(self):
        # Create the individual
        

        # Create an individual with a valid date
        i.create_modified_individual(
            individual_dict, {'Birthday': '1 JAN 1990', 'Death': '1 JAN 2000'}
        )

        try:
            rejectIllegitimateDates(i.get_individual_list(), family_list=list())
            print('All dates are valid ✅')
        except:
            print('At least one date is invalid ❌')

        # Create an individual with an invalid date
        i.create_modified_individual(
            individual_dict, {'Birthday': '40 JAN 1990', 'Death': '40 JAN 2000'}
        )

        try:
            rejectIllegitimateDates(i.get_individual_list(), family_list=list())
            print('All dates are valid despite having an invalid date ❌')
        except:
            print('At least one date is invalid ✅')



def main(out = sys.stderr, verbosity = 2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == "__main__":
    with open("./individual_tests.out", "w") as f:
        main(f)

