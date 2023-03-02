# Imported packages
import unittest
import sys

# Imported files
from projectDictionaries import *
from individualUnitTests import *
from US_modules.DateBeforeCurrent import dateBeforeCurrentDate
from US_modules.MarriageBeforeDivorce import MarriageBeforeDivorce
from US_modules.divorceBeforeDeath import divorceBeforeDeath
from US_modules.NoBigamy import noBigamy
from US_modules.birth_before_marriage import birth_before_marriage
from US_modules.MarriageBeforeDeath import MarriageBeforeDeath
from US_modules.NoBigamy import noBigamy
from US_modules.more_than_5_births import more_than_5_births
from US_modules.siblingSpacing import siblingSpacing
from US_modules.uniqueIDs import uniqueIDS
from US_modules.correctGenderRole import correctGenderRole
from US_modules.SiblingsNotMarried import SiblingsNotMarried
from US_modules.NoMarriageToDescendants import noMarriageToAncestors
from US_modules.fewer_than_fifteen import fewer_than_fifteen

class Family:
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
            "Marriage Date": "1 JAN 2000",
            "Divorce Date": "N/A",
            "Husband ID": "I1",
            "Husband Name": "Richard /Ens/",
            "Wife ID": "I2",
            "Wife Name": "Mary /Ens/",
            "Children": [],
        }[attribute] = value
        assert len(family_dict) == len(
            test_family
        ), "Error: dictionary length of test family does not match original family dictionary"
        try:
            function(family.get_family_list())
            print(f"{function.__name__} Unit Test Success ✅")
        except AssertionError:
            print(f"Error: {AssertionError} on function {function.__name__} ❌")

    # Creating a function to return the list of families
    def get_family_list(self):
        return self.family_list

    # Creating a family with given attributes
    def create_modified_family(self, family_dict, mods):
        family = self.create_family(family_dict)
        for key in mods:
            family[key] = mod[key]
        return family


class FamilyTests(unittest.TestCase):
    def setUp(self):
        # Adding a line to separate unit test cases
        print("-" * 100)

        # Printing the name of the unit test function
        print(self.id().split('.')[-1].replace('test_', '') + ' Unit Test(s)\n')

    def test_noMarriageToDescendants(self):
        individual = Individual()
        individual.create_individual(individual_dict)['ID'] = 'I7'
        individual.get_individual_list()[0]['Spouse'] = 'I9'

        individual.create_individual(individual_dict)['ID'] = 'I9'
        individual.get_individual_list()[1]['Spouse'] = 'I7'

        individual.create_individual(individual_dict)['ID'] = 'I10'
        individual.get_individual_list()[1]['Children'] = ['I10']
        individual.get_individual_list()[0]['Children'] = ['I10']

        family = Family()
        family.create_family(family_dict)['Husband ID'] = 'I7'
        family.get_family_list()[0]['Wife ID'] = 'I9'
        family.get_family_list()[0]['Children'] = ['I10']

        try:
            noMarriageToAncestors(individual.get_individual_list(),family.get_family_list())
            print("No marriages to descendants")
        except AssertionError:
            print("Failed: Detected as married descendants")

        family.get_family_list()[0]['Wife ID'] = 'I10'
        individual.get_individual_list()[0]['Spouse'] = 'I10'

        try:
            noMarriageToAncestors(individual.get_individual_list(),family.get_family_list())
            print("Failed to detect married Descendants")
        except AssertionError:
            print("Passed: Correctly detected married descendants")

        family.get_family_list()[0]['Wife ID'] = 'I9'
        individual.get_individual_list()[0]['Spouse'] = 'I9'

        individual.create_individual(individual_dict)['ID'] = 'I11'
        individual.get_individual_list()[3]['Spouse'] = 'I10'
        individual.get_individual_list()[2]['Spouse'] = 'I11'

        family.create_family(family_dict)['Husband ID'] = 'I10'
        family.get_family_list()[1]['Wife ID'] = 'I11'

        individual.create_individual(individual_dict)['ID'] = 'I12'
        individual.get_individual_list()[3]['Children'] = ['I12']
        individual.get_individual_list()[2]['Children'] = ['I12']
        family.get_family_list()[1]['Wife ID'] = ['I10']
        family.get_family_list()[1]['Husband'] = ['I11']

        try:
            noMarriageToAncestors(individual.get_individual_list(),family.get_family_list())
            print("No marriages to descendants")
        except AssertionError:
            print("Failed: Detected as married descendants")

        individual.get_individual_list()[4]['Spouse'] = 'I9'
        individual.get_individual_list()[1]['Spouse'] = 'I12'
        family.create_family(family_dict)['Husband ID'] = 'I12'
        

        try:
            noMarriageToAncestors(individual.get_individual_list(),family.get_family_list())
            print("Failed to detect marriage to descendants")
        except AssertionError:
            print("Passed: Detected as married descendants")



    def test_siblingsNotMarried(self):
        individual = Individual()
        individual.create_individual(individual_dict)['ID'] = 'I7'
        individual.get_individual_list()[0]['Spouse'] = 'I9'
        individual.create_individual(individual_dict)['ID'] = 'I9'
        individual.get_individual_list()[1]['Spouse'] = 'I7'
        family = Family()
        family.create_family(family_dict)['Husband ID'] = 'I7'
        family.get_family_list()[0]['Wife ID'] = 'I9'

        try:
            SiblingsNotMarried(individual.get_individual_list(), family.get_family_list())
            print("Siblings are not married")
        except AssertionError:
            print("Failed: Detected as siblings")

        family.get_family_list()[0]['Children'] = ['I7','I9']

        try:
            SiblingsNotMarried(individual.get_individual_list(), family.get_family_list())
            print("Failed: Did not detect married siblings")
        except AssertionError:
            print("Passed: Correctly detected married siblings")

    def test_test_checkDatesBeforeCurrent(self):
        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "1 JAN 2025"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "3 DEC 2010"
        try:
            dateBeforeCurrentDate(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Individual birthday is before current date:"
                + str(individual.get_individual_list()[0]["Birthday"])
            )
        except AssertionError:
            print("Failed successfully with error:")

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "1 JAN 1990"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "3 DEC 2030"
        try:
            dateBeforeCurrentDate(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Marriage date is before current date:"
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except AssertionError:
            print("Failed successfully with error:")

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "1 JAN 1990"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "3 DEC 2010"
        try:
            dateBeforeCurrentDate(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Marriage and birth date is before current date:"
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except AssertionError:
            print("Failed successfully with error:")

        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "1 JAN 2050"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "3 DEC 2010"
        try:
            dateBeforeCurrentDate(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Marriage and death date is before current date:"
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except AssertionError:
            print("Failed successfully with error:")

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "1 JAN 2050"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "3 DEC 2030"
        try:
            dateBeforeCurrentDate(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Marriage date is before current date:"
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except AssertionError:
            print("Failed successfully with error:")

    def test_checkMarriageBeforeDeath(self):
        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "1 JAN 2005"
        individual.get_individual_list()[0]["ID"] = "I9"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "3 DEC 2010"
        family.get_family_list()[0]["Husband ID"] = "I9"
        try:
            divorceBeforeDeath(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Marriage date is before death date: "
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except:
            print(
                "Failed successfully with error: Marriage is after death, Married: "
                + str(family.get_family_list()[0]["Marriage Date"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "1 JAN 2010"
        individual.get_individual_list()[0]["ID"] = "I9"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "3 DEC 2050"
        family.get_family_list()[0]["Husband ID"] = "I9"
        try:
            MarriageBeforeDeath(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Marriage date is before death date: "
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except:
            print(
                "Failed successfully with error: Marriage is after death, Married: "
                + str(family.get_family_list()[0]["Marriage Date"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "1 JAN 2019"
        individual.get_individual_list()[0]["ID"] = "I9"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "3 DEC 2052"
        family.get_family_list()[0]["Husband ID"] = "I9"
        try:
            MarriageBeforeDeath(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Marriage date is before death date: "
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except:
            print(
                "Failed successfully with error: Marriage is after death, Married: "
                + str(family.get_family_list()[0]["Marriage Date"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "1 JAN 2000"
        individual.get_individual_list()[0]["ID"] = "I9"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "3 DEC 2053"
        family.get_family_list()[0]["Husband ID"] = "I9"
        try:
            MarriageBeforeDeath(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Marriage date is before death date: "
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except:
            print(
                "Failed successfully with error: Marriage is after death, Married: "
                + str(family.get_family_list()[0]["Marriage Date"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "1 JAN 2008"
        individual.get_individual_list()[0]["ID"] = "I9"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "3 DEC 2009"
        family.get_family_list()[0]["Husband ID"] = "I9"
        try:
            MarriageBeforeDeath(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Marriage date is before death date: "
                + str(family.get_family_list()[0]["Divorce Date"])
            )
        except:
            print(
                "Failed successfully with error: Marriage is after death, Married: "
                + str(family.get_family_list()[0]["Marriage Date"])
            )

    def test_checkMarriageBeforeDivorce(self):
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "1 JAN 2000"
        family.get_family_list()[0]["Divorce Date"] = "1 JAN 1990"
        # test 1
        try:
            MarriageBeforeDivorce([], family.get_family_list())
            print(
                f"Didn't detect Marriage date {str(family.get_family_list()[0]['Marriage Date'])} is after divorce date: {str(family.get_family_list()[0]['Divorce Date'])} ❌"
            )
        except:
            print(
                f"Failed successfully with error, Marriage Date {str(family.get_family_list()[0]['Marriage Date'])} is after divorce date: {str(family.get_family_list()[0]['Divorce Date'])}✅"
            )
        # test 2
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "1 JAN 2000"
        family.get_family_list()[0]["Divorce Date"] = "N/A"
        try:
            MarriageBeforeDivorce([], family.get_family_list())
            print(
                f"Marriage date {str(family.get_family_list()[0]['Marriage Date'])} is before divorce date: {str(family.get_family_list()[0]['Divorce Date'])} ✅"
            )
        except:
            print(
                f"Failed with error, Marriage date {str(family.get_family_list()[0]['Marriage Date'])} is before divorce date: {str(family.get_family_list()[0]['Divorce Date'])} ❌"
            )
        # test 3
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "6 JAN 2010"
        family.get_family_list()[0]["Divorce Date"] = "1 JAN 2000"
        try:
            MarriageBeforeDivorce([], family.get_family_list())
            print(
                f"Didn't detect Marriage date {str(family.get_family_list()[0]['Marriage Date'])} is after divorce date: {str(family.get_family_list()[0]['Divorce Date'])} ❌"
            )
        except:
            print(
                f"Failed successfully with error, Marriage Date {str(family.get_family_list()[0]['Marriage Date'])} is after divorce date: {str(family.get_family_list()[0]['Divorce Date'])}✅"
            )
        # test 4
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "18 JAN 2013"
        family.get_family_list()[0]["Divorce Date"] = "19 AUG 2000"
        try:
            MarriageBeforeDivorce([], family.get_family_list())
            print(
                f"Didn't detect Marriage date {str(family.get_family_list()[0]['Marriage Date'])} is after divorce date: {str(family.get_family_list()[0]['Divorce Date'])} ❌"
            )
        except:
            print(
                f"Failed successfully with error, Marriage Date {str(family.get_family_list()[0]['Marriage Date'])} is after divorce date: {str(family.get_family_list()[0]['Divorce Date'])}✅"
            )
        # test 5
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "1 JAN 2000"
        family.get_family_list()[0]["Divorce Date"] = "28 DEC 1999"
        try:
            MarriageBeforeDivorce([], family.get_family_list())
            print(
                f"Didn't detect Marriage date {str(family.get_family_list()[0]['Marriage Date'])} is after divorce date: {str(family.get_family_list()[0]['Divorce Date'])} ❌"
            )
        except:
            print(
                f"Failed successfully with error, Marriage Date {str(family.get_family_list()[0]['Marriage Date'])} is after divorce date: {str(family.get_family_list()[0]['Divorce Date'])}✅"
            )

    def test_checkDivorceBeforeDeath(self):
        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "1 JAN 2005"
        individual.get_individual_list()[0]["ID"] = "I1"
        family = Family()
        family.create_family(family_dict)["Divorce Date"] = "3 DEC 2010"
        family.get_family_list()[0]["Husband ID"] = "I1"
        try:
            divorceBeforeDeath(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Divorce date is before death date: "
                + str(family.get_family_list()[0]["Divorce Date"])
            )
        except:
            print(
                "Failed successfully with error: Divorce is after death, Divorced: "
                + str(family.get_family_list()[0]["Divorce Date"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "1 JAN 2010"
        individual.get_individual_list()[0]["ID"] = "I1"
        family = Family()
        family.create_family(family_dict)["Divorce Date"] = "3 DEC 2050"
        family.get_family_list()[0]["Husband ID"] = "I1"
        try:
            divorceBeforeDeath(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Divorce date is before death date: "
                + str(family.get_family_list()[0]["Divorce Date"])
            )
        except:
            print(
                "Failed successfully with error: Divorce is after death, Divorced: "
                + str(family.get_family_list()[0]["Divorce Date"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "1 JAN 2019"
        individual.get_individual_list()[0]["ID"] = "I1"
        family = Family()
        family.create_family(family_dict)["Divorce Date"] = "3 DEC 2052"
        family.get_family_list()[0]["Husband ID"] = "I1"
        try:
            divorceBeforeDeath(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Divorce date is before death date: "
                + str(family.get_family_list()[0]["Divorce Date"])
            )
        except:
            print(
                "Failed successfully with error: Divorce is after death, Divorced: "
                + str(family.get_family_list()[0]["Divorce Date"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "1 JAN 2000"
        individual.get_individual_list()[0]["ID"] = "I1"
        family = Family()
        family.create_family(family_dict)["Divorce Date"] = "3 DEC 2053"
        family.get_family_list()[0]["Husband ID"] = "I1"
        try:
            divorceBeforeDeath(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Divorce date is before death date: "
                + str(family.get_family_list()[0]["Divorce Date"])
            )
        except:
            print(
                "Failed successfully with error: Divorce is after death, Divorced: "
                + str(family.get_family_list()[0]["Divorce Date"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Death"] = "1 JAN 2008"
        individual.get_individual_list()[0]["ID"] = "I1"
        family = Family()
        family.create_family(family_dict)["Divorce Date"] = "3 DEC 2009"
        family.get_family_list()[0]["Husband ID"] = "I1"
        try:
            divorceBeforeDeath(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Divorce date is before death date: "
                + str(family.get_family_list()[0]["Divorce Date"])
            )
        except:
            print('Failed successfully with error: Divorce is after death, Divorced: ' + str(family.get_family_list()[0]['Divorce Date']) )

    def test_fewer_than_fifteen(self):
        individual = Individual()
        individual.create_individual(individual_dict)['ID'] = 'I1'
        family = Family()
        family.create_family(family_dict)['Children'] = ['I1']
        family.get_family_list()[0]['Children'].append(individual.get_individual_list()[0]['ID'])
        for i in range(13):
            individual = Individual()
            individual.create_individual(individual_dict)['ID'] = 'I'+str(i+2)
            family.get_family_list()[0]['Children'].append(individual.get_individual_list()[0]['ID'])
        
        try:
            fewer_than_fifteen(individual.get_individual_list(), family.get_family_list())
            print("Fewer than Fifteen Siblings**********************************")
        except:
            print("More than Fifteen Sibling**********************************")

        individual = Individual()
        individual.create_individual(individual_dict)['ID'] = 'I1'
        family = Family()
        family.create_family(family_dict)['Children'] = ['I1']
        family.get_family_list()[0]['Children'].append(individual.get_individual_list()[0]['ID'])
        for i in range(14):
            individual = Individual()
            individual.create_individual(individual_dict)['ID'] = 'I'+str(i+2)
            family.get_family_list()[0]['Children'].append(individual.get_individual_list()[0]['ID'])

        try:
            fewer_than_fifteen(individual.get_individual_list(), family.get_family_list())
            print("Fewer than Fifteen Siblings**********************************")
        except:
            print("More than Fifteen Sibling**********************************")


    def test_birth_before_marriage(self):
        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '1 JAN 2002' 
        individual.get_individual_list()[0]['ID'] = 'I1'
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '5 DEC 2019'
        family.get_family_list()[0]['Husband ID'] = 'I1'
        try:
            birth_before_marriage(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Individual birthday is after Marriage Date:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(family.get_family_list()[0]["Marriage Date"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "3 DEC 2020"
        individual.get_individual_list()[0]["ID"] = "I1"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "1 JAN 2000"
        family.get_family_list()[0]["Husband ID"] = "I1"
        try:
            birth_before_marriage(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Individual birthday is after Marriage Date:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(family.get_family_list()[0]["Marriage Date"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "3 AUG 2020"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "1 JAN 1990"
        try:
            birth_before_marriage(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Individual birthday is after Marriage Date:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(family.get_family_list()[0]["Marriage Date"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "30 JAN 2022"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "15 AUG 2010"
        try:
            birth_before_marriage(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Individual birthday is after Marriage Date:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(family.get_family_list()[0]["Marriage Date"])
            )

        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "15 AUG 2010"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "10 FEB 1999"
        try:
            birth_before_marriage(
                individual.get_individual_list(), family.get_family_list()
            )
            print(
                "Individual birthday is after Marriage Date:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(family.get_family_list()[0]["Marriage Date"])
            )
        except:
            print(
                "Failed successfully with error:"
                + str(individual.get_individual_list()[0]["Birthday"])
                + " | "
                + str(family.get_family_list()[0]["Marriage Date"])
            )

    def test_checkBigamy(self):

        # test1
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "13 JAN 2000"
        family.get_family_list()[0]["ID"] = "F1"
        family.get_family_list()[0]["Divorce Date"] = "6 JAN 2001"
        family.get_family_list()[0]["Husband ID"] = "I1"
        family.get_family_list()[0]["Wife ID"] = "I2"

        family.create_family(family_dict)["Marriage Date"] = "13 JUN 2002"
        family.get_family_list()[1]["ID"] = "F2"
        family.get_family_list()[1]["Divorce Date"] = "N/A"
        family.get_family_list()[1]["Husband ID"] = "I1"
        family.get_family_list()[1]["Wife ID"] = "I3"
        try:
            noBigamy([], family.get_family_list())
            print(f"Bigamy is not present: {str(family.get_family_list())} ✅")
        except:
            print(f"Failed with error {str(family.get_family_list())} ❌")

        # test2
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "13 JAN 2000"
        family.get_family_list()[0]["ID"] = "F1"
        family.get_family_list()[0]["Divorce Date"] = "6 JAN 2001"
        family.get_family_list()[0]["Husband ID"] = "I1"
        family.get_family_list()[0]["Wife ID"] = "I2"
        family.create_family(family_dict)["Marriage Date"] = "23 DEC 2000"
        family.get_family_list()[1]["ID"] = "F2"
        family.get_family_list()[1]["Divorce Date"] = "N/A"
        family.get_family_list()[1]["Husband ID"] = "I1"
        family.get_family_list()[1]["Wife ID"] = "I3"
        try:
            noBigamy([], family.get_family_list())
            print(f"Bigamy went undetected: {str(family.get_family_list())} ❌")
        except:
            print(f"Failed successfully with error {str(family.get_family_list())} ✅")

        # test3
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "13 JAN 2000"
        family.get_family_list()[0]["ID"] = "F1"
        family.get_family_list()[0]["Divorce Date"] = "6 JAN 2001"
        family.get_family_list()[0]["Husband ID"] = "I1"
        family.get_family_list()[0]["Wife ID"] = "I2"
        family.create_family(family_dict)["Marriage Date"] = "23 OCT 1998"
        family.get_family_list()[1]["ID"] = "F2"
        family.get_family_list()[1]["Divorce Date"] = "N/A"
        family.get_family_list()[1]["Husband ID"] = "I3"
        family.get_family_list()[1]["Wife ID"] = "I4"
        try:
            noBigamy([], family.get_family_list())
            print(f"Bigamy is not present: {str(family.get_family_list())} ✅")
        except:
            print(f"Failed with error {str(family.get_family_list())} ❌")

        # test4
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "13 JAN 2000"
        family.get_family_list()[0]["ID"] = "F1"
        family.get_family_list()[0]["Divorce Date"] = "6 JAN 2001"
        family.get_family_list()[0]["Husband ID"] = "I1"
        family.get_family_list()[0]["Wife ID"] = "I2"

        family.create_family(family_dict)["Marriage Date"] = "13 JUN 2002"
        family.get_family_list()[1]["ID"] = "F2"
        family.get_family_list()[1]["Divorce Date"] = "N/A"
        family.get_family_list()[1]["Husband ID"] = "I3"
        family.get_family_list()[1]["Wife ID"] = "I1"
        try:
            noBigamy([], family.get_family_list())
            print(f"Bigamy is not present: {str(family.get_family_list())} ✅")
        except:
            print(f"Failed with error {str(family.get_family_list())} ❌")

        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "13 JAN 2000"
        family.get_family_list()[0]["ID"] = "F1"
        family.get_family_list()[0]["Divorce Date"] = "6 JAN 2001"
        family.get_family_list()[0]["Husband ID"] = "I1"
        family.get_family_list()[0]["Wife ID"] = "I2"
        family.create_family(family_dict)["Marriage Date"] = "23 DEC 2000"
        family.get_family_list()[1]["ID"] = "F2"
        family.get_family_list()[1]["Divorce Date"] = "N/A"
        family.get_family_list()[1]["Husband ID"] = "I3"
        family.get_family_list()[1]["Wife ID"] = "I1"
        try:
            noBigamy([], family.get_family_list())
            print(f"Bigamy went undetected: {str(family.get_family_list())} ❌")
        except:
            print(f"Failed successfully with error {str(family.get_family_list())} ✅")

    def test_more_than_5_births(self):
        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '5 DEC 2019' 
        individual.get_individual_list()[0]['ID'] = 'I1'
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '1 JAN 2002'
        family.get_family_list()[0]['Husband ID'] = 'I1'
        family.get_family_list()[0]['Children'] = ['I2', 'I3', 'I4', 'I5', 'I6', 'I7']
        for i in range(2,9):
            individual.create_individual(individual_dict)['Birthday'] = '5 DEC 2019' 
            individual.get_individual_list()[-1]['ID'] = 'I'+str(i)
        try:
            more_than_5_births(individual.get_individual_list(), family.get_family_list())
            print(f"More than 5 births were not detected: {str(family.get_family_list())} ❌")
        except:
            print(f"Failed successfully with error {str(family.get_family_list())} ✅")
        
        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '5 DEC 2019' 
        individual.get_individual_list()[0]['ID'] = 'I1'
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '1 JAN 2002'
        family.get_family_list()[0]['Husband ID'] = 'I1'
        family.get_family_list()[0]['Children'] = ['I2', 'I3']
        for i in range(2,4):
            individual.create_individual(individual_dict)['Birthday'] = '5 DEC 2019' 
            individual.get_individual_list()[-1]['ID'] = 'I'+str(i)
        try:
            more_than_5_births(individual.get_individual_list(), family.get_family_list())
            print(f"Less than 5 births were not detected: {str(family.get_family_list())} ✅")
        except:
            print(f"Failed unsuccessfully with error {str(family.get_family_list())} ❌")
        

    def test_sibling_spacing(self):
        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '5 JUN 1998'
        individual.get_individual_list()[0]['ID'] = 'I1'
        individual.create_individual(individual_dict)['Birthday'] = '13 FEB 1998'
        individual.get_individual_list()[1]['ID'] = 'I2'
        individual.create_individual(individual_dict)['Birthday'] = '5 JUN 2020'
        individual.get_individual_list()[2]['ID'] = 'I3'
        individual.create_individual(individual_dict)['Birthday'] = '13 FEB 2018'
        individual.get_individual_list()[3]['ID'] = 'I4'
        family=Family()
        family.create_family(family_dict)['Marriage Date'] = '1 JAN 2002'
        family.get_family_list()[0]['Husband ID'] = 'I1'
        family.get_family_list()[0]['Wife ID'] = 'I2'
        family.get_family_list()[0]['Children'] = ['I3', 'I4']
        try:
            siblingSpacing(individual.get_individual_list(), family.get_family_list())
            print(f"Siblings are spaced correctly: {str(individual.get_individual_list())} ✅")
        except:
            print(f"Failed with error {str(individual.get_individual_list())} ❌")
        individual.get_individual_list()[3]['Birthday'] = '13 FEB 2020'
        try:
            siblingSpacing(individual.get_individual_list(), family.get_family_list())
            print(f"Siblings are spaced incorrectly: {str(individual.get_individual_list())} ❌")
        except:
            print(f"Failed successfully with error {str(individual.get_individual_list())} ✅")
        individual.get_individual_list()[3]['Birthday'] = '5 JUN 2020'
        try:
            siblingSpacing(individual.get_individual_list(), family.get_family_list())
            print(f"Siblings are spaced correctly: {str(individual.get_individual_list())} ✅")
        except:
            print(f"Failed with error {str(individual.get_individual_list())} ❌")
        individual.get_individual_list()[3]['Birthday'] = '13 FEB 2018'
        individual.create_individual(individual_dict)['Birthday'] = '5 JUN 2020'
        individual.get_individual_list()[4]['ID'] = 'I5'
        family.get_family_list()[0]['Children'] = ['I3', 'I4', 'I5']
        try:
            siblingSpacing(individual.get_individual_list(), family.get_family_list())
            print(f"Siblings are spaced correctly: {str(individual.get_individual_list())} ✅")
        except:
            print(f"Failed with error {str(individual.get_individual_list())} ❌")
        
        individual.get_individual_list()[4]['Birthday'] = '5 SEP 2020'
        try:
            siblingSpacing(individual.get_individual_list(), family.get_family_list())
            print(f"Siblings are spaced incorrectly: {str(individual.get_individual_list())} ❌")
        except:
            print(f"Failed successfully with error {str(individual.get_individual_list())} ✅")

def main(out = sys.stderr, verbosity = 2):
    def test_uniqueIDs(self):
        # Adding two individuals with different IDs
        ind = Individual()
        ind1 = ind.create_individual(individual_dict)
        ind.get_individual_list()[-1]["ID"] = "@I1@"
        ind2 = ind.create_individual(individual_dict)
        ind.get_individual_list()[-1]["ID"] = "@I2@"

        # Adding a family with another ID
        fam = Family()
        fam1 = fam.create_family(family_dict)
        fam.get_family_list()[-1]["ID"] = "@F1@"

        # Unit case 1
        try:
            uniqueIDS(ind.get_individual_list(), fam.get_family_list())
            print("uniqueIDs: Passed successfully ✅")
        except:
            print("uniqueIDs: Failed unsuccessfully ❌")

        # Adding an individual with the same ID as the first
        ind3 = ind.create_individual(individual_dict)
        ind.get_individual_list()[-1]["ID"] = "@I1@"

        # Unit case 2
        try:
            uniqueIDS(ind.get_individual_list(), fam.get_family_list())
            print("uniqueIDs: Passed unsuccessfully ❌")
        except:
            print("uniqueIDs: Failed successfully ✅")

    def test_checkGenderRole(self):
        # Creating a family
        fam = Family()
        fam1 = fam.create_family(family_dict)
        fam.get_family_list()[-1]["ID"] = "@F1@"

        # Creating a husband
        ind = Individual()
        ind1 = ind.create_individual(individual_dict)
        ind.get_individual_list()[-1]["ID"] = "@I1@"
        ind.get_individual_list()[-1]["Sex"] = "M"
        ind.get_individual_list()[-1]["Family"] = "@F1@"
        fam.get_family_list()[-1]["Husband ID"] = "@I1@"

        # Creating a wife
        ind2 = ind.create_individual(individual_dict)
        ind.get_individual_list()[-1]["ID"] = "@I2@"
        ind.get_individual_list()[-1]["Sex"] = "F"
        ind.get_individual_list()[-1]["Family"] = "@F1@"
        fam.get_family_list()[-1]["Wife ID"] = "@I2@"

        # Unit case 1 - Should pass
        try:
            correctGenderRole(ind.get_individual_list(), fam.get_family_list())
            print("correctGenderRole: passed successfully ✅")
        except:
            print("correctGenderRole: failed unsuccessfully ❌")

        # Unit case 2 (making the wife male) should fail
        ind.get_individual_list()[-1]["Sex"] = "M"
        try:
            correctGenderRole(ind.get_individual_list(), fam.get_family_list())
            print("correctGenderRole: passed unsuccessfully ❌")
        except:
            print("correctGenderRole: failed successfully ✅")
        ind.get_individual_list()[-1]["Sex"] = "F"

        # Unit case 3 (making the husband undefined) should fail
        ind.get_individual_list()[0]["Sex"] = "idk"
        try:
            correctGenderRole(ind.get_individual_list(), fam.get_family_list())
            print("correctGenderRole: passed unsuccessfully ❌")
        except:
            print("correctGenderRole: failed successfully ✅")

def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == "__main__":
    with open("./family_tests.out", "w") as f:
        main(f)
