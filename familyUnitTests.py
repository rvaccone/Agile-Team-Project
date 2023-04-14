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
from US_modules.listLivingSingle import listLivingSingle
from US_modules.listMultipleBirths import listMultipleBirths, MultipleBirth

from US_modules.uniqueNameAndBirthday import uniqueNameAndBirthday
from US_modules.uniqueFamilyBySpouses import uniqueFamilyBySpouses
from US_modules.auntsAndUncles import noMarriageToAuntsAndUncles
from US_modules.auntsAndUncles import listAuntsAndUncles
from US_modules.noMarryFirstCousin import noMarriageToFirstCousins
from US_modules.noMarryFirstCousin import listFirstCousins
from US_modules.uniqueNameAndBirthday import uniqueNameAndBirthday
from US_modules.uniqueFamilyBySpouses import uniqueFamilyBySpouses
from US_modules.IncludeIndividualAges import IncludeIndividualAges
from US_modules.OrderSiblingsByAge import OrderSiblingsByAge
from US_modules.upcomingAnniversary import is_spouse_alive
from US_modules.upcomingAnniversary import upcoming_anniversary

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
            family[key] = mods[key]
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
    
    def test_checkUniqueNameAndBirthday(self):
        individual = Individual()
        #Test 1 should pass
        individual.create_individual(individual_dict)['Birthday'] = '27 AUG 2002'
        individual.get_individual_list()[0]['Name'] = 'Taeseo Um'
        individual.get_individual_list()[0]['ID'] = 'I1'
        individual.create_individual(individual_dict)['Birthday'] = '10 FEB 2002'
        individual.get_individual_list()[1]['Name'] = 'Rocco Vaccone'
        individual.get_individual_list()[1]['ID'] = 'I2'
        try: 
            uniqueNameAndBirthday(individual.get_individual_list())
            print(f"Unique name and birthday: {str(individual.get_individual_list())} ✅")
        except:
            print(f"Failed with error {str(individual.get_individual_list())} ❌")
        #Test 2 should fail
        individual.get_individual_list()[0]['Name'] = 'Rocco Vaccone'
        individual.get_individual_list()[0]['Birthday'] = '10 FEB 2002'
        try:
            uniqueNameAndBirthday(individual.get_individual_list())
            print(f"Unique name and birthday: {str(individual.get_individual_list())} ❌")
        except:
            print(f"Failed successfully with error {str(individual.get_individual_list())} ✅")
    def test_checkUniqueFamilyBySpouses(self):
        #No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file
        individual=Individual()
        family=Family()
        family.create_family(family_dict)['Marriage Date'] = '1 JAN 2002'
        family.get_family_list()[0]['Husband ID'] = 'I1'
        family.get_family_list()[0]['Wife ID'] = 'I2'
        family.get_family_list()[0]['Husband Name'] = 'Rocco Vaccone'
        family.get_family_list()[0]['Wife Name'] = 'Aaliyah Bridges'
        family.create_family(family_dict)['Marriage Date'] = '6 JUN 1998'
        family.get_family_list()[1]['Husband ID'] = 'I3'
        family.get_family_list()[1]['Wife ID'] = 'I4'
        family.get_family_list()[1]['Husband Name'] = 'Taesoe Um'
        family.get_family_list()[1]['Wife Name'] = 'Trae Young'
        individual.create_individual(individual_dict)['Birthday'] = '27 AUG 2002'
        individual.get_individual_list()[0]['Name'] = 'Rocco Vaccone'
        individual.get_individual_list()[0]['ID'] = 'I1'
        individual.create_individual(individual_dict)['Birthday'] = '27 AUG 2002'
        individual.get_individual_list()[1]['Name'] = 'Aaliyah Bridges'
        individual.get_individual_list()[1]['ID'] = 'I2'
        individual.create_individual(individual_dict)['Birthday'] = '27 AUG 2002'
        individual.get_individual_list()[2]['Name'] = 'Taesoe Um'
        individual.get_individual_list()[2]['ID'] = 'I3'
        individual.create_individual(individual_dict)['Birthday'] = '27 AUG 2002'
        individual.get_individual_list()[3]['Name'] = 'Trae Young'
        individual.get_individual_list()[3]['ID'] = 'I4'
        try:
            uniqueFamilyBySpouses(family.get_family_list(), individual.get_individual_list())
            print(f"Unique family by spouse: {str(family.get_family_list())} ✅")
        except AssertionError:
            print(f"Failed with error {str(family.get_family_list())} ❌")
        family.get_family_list()[1]['Husband Name'] = 'Rocco Vaccone'
        family.get_family_list()[1]['Wife Name'] = 'Aaliyah Bridges'
        family.get_family_list()[1]['Marriage Date'] = '1 JAN 2002'
        try:
            uniqueFamilyBySpouses(family.get_family_list(), individual.get_individual_list())
            print(f"Unique family by spouse: {str(individual.get_individual_list())} ❌")
        except:
            print(f"Failed successfully with error {str(individual.get_individual_list())} ✅")

    def test_IncludeIndividualAges(self):
        individual = Individual()
        individual.create_individual(individual_dict)['ID'] = 'I7'
        individual.get_individual_list()[0]['Age'] = '10'

        individual.create_individual(individual_dict)['ID'] = 'I9'
        individual.get_individual_list()[1]['Age'] = '15'

        try:
            IncludeIndividualAges(individual.get_individual_list())
            print("Passed: All individuals have ages.")
        except AssertionError:
            print("Failed: Did not detect all ages when they were present.")


        individual.create_individual(individual_dict)['ID'] = 'I5'

        try:
            IncludeIndividualAges(individual.get_individual_list())
            print("Failed: Did not detect missing age")
        except AssertionError:
            print("Passed: Successfully detected missing age")


    def test_OrderSiblingsByAge(self):
        individual = Individual()
        individual.create_individual(individual_dict)['ID'] = 'I7'
        individual.get_individual_list()[0]['Age'] = '10'

        individual.create_individual(individual_dict)['ID'] = 'I9'
        individual.get_individual_list()[1]['Age'] = '15'

        individual.create_individual(individual_dict)['ID'] = 'I10'
        individual.get_individual_list()[2]['Children'] = ['I9','I7']

        family = Family()
        family.create_family(family_dict)['Husband ID'] = 'I10'
        family.get_family_list()[0]['Children'] = ['I9','I7']


        try:
            OrderSiblingsByAge(individual.get_individual_list(),family.get_family_list())
            print("Passed: Siblings ordered by age")
        except AssertionError:
            print("Failed: Did not detect siblings ordered by age when they were")

        family.get_family_list()[0]['Children'] = ['I7','I9']

        try:
            OrderSiblingsByAge(individual.get_individual_list(),family.get_family_list())
            print("Failed: Detected siblings ordered by age when they were not")
        except AssertionError:
            print("Passed: Successfully detected siblings not ordered by age")

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
    
    def test_listLivingSingle(self):
        # Creating all individuals such that only @I3@ should return
        ind = Individual()
        ind1 = ind.create_modified_individual(individual_dict, {'ID': '@I1@','Age': 35, 'Spouse': '@I2@'})
        ind2 = ind.create_modified_individual(individual_dict, {'ID': '@I2@','Age': 33, 'Spouse': '@I1@'})
        ind3 = ind.create_modified_individual(individual_dict, {'ID': '@I3@','Age': 33})
        ind4 = ind.create_modified_individual(individual_dict, {'ID': '@I4@','Age': 24})
        ind5 = ind.create_modified_individual(individual_dict, {'ID': '@I5@','Age': 45})
        ind5 = ind.create_modified_individual(individual_dict, {'ID': '@I6@','Age': 44})
        ind5 = ind.create_modified_individual(individual_dict, {'ID': '@I7@'})

        # Creating all families such that only @I3@ should return
        fam = Family()
        fam1 = fam.create_modified_family(family_dict, {'Marriage Date': '1 JAN 2010', 'Husband ID': '@I1@', 'Wife ID': '@I2@'})
        fam2 = fam.create_modified_family(family_dict, {'Marriage Date': '1 JAN 2010', 'Divorce Date': '1 JAN 2015', 'Husband ID': '@I5@', 'Wife ID': '@I6@'})

        output = listLivingSingle(ind.get_individual_list(), fam.get_family_list())

        try:
            self.assertTrue(output == ['@I3@'], f'The return value is incorrect, expected: [@I3@], got: {output} ❌')
            print("Passed successfully ✅")
        except AssertionError as warn:
            print(warn)

    def test_listMultipleBirths(self):
        # Creating all individuals such that two MultipleBirth classes should return
        ind = Individual()
        ind1 = ind.create_modified_individual(individual_dict, {'ID': '@I1@', 'Birthday': '1 JAN 2010'}) # Start of F1
        ind2 = ind.create_modified_individual(individual_dict, {'ID': '@I2@', 'Birthday': '1 JAN 2010'})
        ind3 = ind.create_modified_individual(individual_dict, {'ID': '@I3@', 'Birthday': '3 FEB 2008'})
        ind4 = ind.create_modified_individual(individual_dict, {'ID': '@I4@', 'Birthday': '11 NOV 2012'}) # Start of F2
        ind5 = ind.create_modified_individual(individual_dict, {'ID': '@I5@', 'Birthday': '3 DEC 2010'})
        ind6 = ind.create_modified_individual(individual_dict, {'ID': '@I6@', 'Birthday': '3 DEC 2010'})
        ind7 = ind.create_modified_individual(individual_dict, {'ID': '@I7@', 'Birthday': '1 JAN 2010'}) # Start of F3

        # Creating all families such that two MultipleBirth classes should return
        fam = Family()
        fam1 = fam.create_modified_family(family_dict, {'ID': '@F1@', 'Children': ['@I1@', '@I2@', '@I3@']})
        fam2 = fam.create_modified_family(family_dict, {'ID': '@F2@', 'Children': ['@I4@', '@I5@', '@I6@']})
        fam3 = fam.create_modified_family(family_dict, {'ID': '@F3@', 'Children': ['@I7@']})

        expected_output = [MultipleBirth('@F1@', '1 JAN 2010', ['@I1@', '@I2@']), MultipleBirth('@F2@', '3 DEC 2010', ['@I5@', '@I6@'])]

        output = listMultipleBirths(ind.get_individual_list(), fam.get_family_list())

        try:
            self.assertTrue([out.compare() for out in output] == [out.compare() for out in expected_output], f'The return value is incorrect, expected: {expected_output}, got: {output} ❌')
            print("Passed successfully ✅")
        except AssertionError as warn:
            print(warn)

        # Removing the common birthdays from familes F1 and F2
        ind.get_individual_list()[0]["Birthday"] = "N/A"
        ind.get_individual_list()[4]["Birthday"] = "N/A"

        output = listMultipleBirths(ind.get_individual_list(), fam.get_family_list())

        try:
            self.assertTrue(output == [], f'Will not return an empty list if there are no multiple births ❌')
            print("Passed successfully ✅")
        except AssertionError as warn:
            print(warn)



    def test_checkAuntsAndUnclesDoNotMarryNieceOrNewphew(self):
        individual = Individual()
    
        # Create individuals for the test case
        individual.create_individual(individual_dict)['ID'] = 'I1'
        individual.create_individual(individual_dict)['ID'] = 'I2'
        individual.create_individual(individual_dict)['ID'] = 'I3'
        individual.create_individual(individual_dict)['ID'] = 'I4'
        individual.create_individual(individual_dict)['ID'] = 'I5'

        # Create families for the test case
        family = Family()
        family.create_family(family_dict)['Husband ID'] = 'I1'
        family.get_family_list()[0]['Wife ID'] = 'I2'
        family.get_family_list()[0]['Children'] = ['I3']

        family.create_family(family_dict)['Husband ID'] = 'I3'
        family.get_family_list()[1]['Wife ID'] = 'I4'
        family.get_family_list()[1]['Children'] = ['I5']

        # Test no marriage to aunts and uncles (normal case)
        try:
            noMarriageToAuntsAndUncles(individual.get_individual_list(), family.get_family_list())
            print("No marriages to aunts and uncles")
        except AssertionError:
            print("Failed: Detected as married to aunts or uncles")

        # Test marriage to uncle (negative case)
        individual.get_individual_list()[4]['Spouse'] = 'I1'
        family.get_family_list()[1]['Wife ID'] = 'I1'

        try:
            noMarriageToAuntsAndUncles(individual.get_individual_list(), family.get_family_list())
            print("Failed to detect married to uncle")
        except AssertionError:
            print("Passed: Correctly detected married to uncle")

        # Reset the test case
        individual.get_individual_list()[4]['Spouse'] = None
        family.get_family_list()[1]['Wife ID'] = 'I4'

        # Test marriage to aunt (negative case)
        individual.get_individual_list()[4]['Spouse'] = 'I2'
        family.get_family_list()[1]['Wife ID'] = 'I2'

        try:
            noMarriageToAuntsAndUncles(individual.get_individual_list(), family.get_family_list())
            print("Failed to detect married to aunt")
        except AssertionError:
            print("Passed: Correctly detected married to aunt")


   
    def test_noMarriageToFirstCousins(self):
        individual = Individual()

        # Create individuals for the test case
        individual.create_individual(individual_dict)['ID'] = 'I1'
        individual.create_individual(individual_dict)['ID'] = 'I2'
        individual.create_individual(individual_dict)['ID'] = 'I3'
        individual.create_individual(individual_dict)['ID'] = 'I4'
        individual.create_individual(individual_dict)['ID'] = 'I5'
        individual.create_individual(individual_dict)['ID'] = 'I6'

        # Create families for the test case
        family = Family()
        family.create_family(family_dict)['Husband ID'] = 'I1'
        family.get_family_list()[0]['Wife ID'] = 'I2'
        family.get_family_list()[0]['Children'] = ['I3', 'I4']

        family.create_family(family_dict)['Husband ID'] = 'I3'
        family.get_family_list()[1]['Wife ID'] = 'I5'
        family.get_family_list()[1]['Children'] = ['I6']

        # Test no marriage to first cousins (normal case)
        try:
            noMarriageToFirstCousins(individual.get_individual_list(), family.get_family_list())
            print("No marriages to first cousins")
        except AssertionError:
            print("Failed: Detected as married to first cousins")

        # Test marriage to first cousin (negative case)
        individual.get_individual_list()[5]['Spouse'] = 'I4'
        family.get_family_list()[1]['Wife ID'] = 'I4'

        try:
            noMarriageToFirstCousins(individual.get_individual_list(), family.get_family_list())
            print("Failed to detect married to first cousin")
        except AssertionError:
            print("Passed: Correctly detected married to first cousin")

    def test_upcoming_anniversary(self):
        individual_list = [
            {'ID': '@I1@', 'Alive': True},
            {'ID': '@I2@', 'Alive': True},
            {'ID': '@I3@', 'Alive': True},
            {'ID': '@I4@', 'Alive': True},
            {'ID': '@I5@', 'Alive': False},
            {'ID': '@I6@', 'Alive': True},
        ]

        family_list = [
            {'Marriage Date': '15 APR 2000', 'Divorce Date': 'N/A', 'Husband ID': '@I1@', 'Wife ID': '@I2@'},
            {'Marriage Date': 'N/A', 'Divorce Date': 'N/A', 'Husband ID': '@I3@', 'Wife ID': '@I4@'},
            {'Marriage Date': '12 MAY 2015', 'Divorce Date': '12 MAY 2020', 'Husband ID': '@I5@', 'Wife ID': '@I6@'},
        ]

        output = upcoming_anniversary(individual_list, family_list)
        expected_output = ['2000-04-15']

        try:
            self.assertEqual(output, expected_output, f"The return value is incorrect, expected: {expected_output}, got: {output} ❌")
            print("Passed successfully ✅")
        except AssertionError as warn:
            print(warn)
        

def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == "__main__":
    with open("./family_tests.out", "w") as f:
        main(f)
