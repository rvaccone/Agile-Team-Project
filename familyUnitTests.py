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
from US_modules.uniqueIDs import uniqueIDS
from US_modules.correctGenderRole import correctGenderRole


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


class FamilyTests(unittest.TestCase):
    def test_checkDatesBeforeCurrent(self):
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
        print("am i able to get here")
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
            print(
                "Failed successfully with error: Divorce is after death, Divorced: "
                + str(family.get_family_list()[0]["Divorce Date"])
            )

    def test_birth_before_marriage(self):
        individual = Individual()
        individual.create_individual(individual_dict)["Birthday"] = "5 DEC 2019"
        individual.get_individual_list()[0]["ID"] = "I1"
        family = Family()
        family.create_family(family_dict)["Marriage Date"] = "1 JAN 2002"
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
            print("how far am i able to get in?")
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

        print("-" * 50)

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
        # Creating a line to make the test case more visible
        print("-" * 50)

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

        # Creating a line to make the test case more visible
        print("-" * 50)


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == "__main__":
    with open("./family_tests.out", "w") as f:
        main(f)
