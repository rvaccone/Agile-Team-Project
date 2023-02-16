# Imported packages
import unittest

# Imported files
from projectDictionaries import *
from individualUnitTests import *
import errorChecking as ec
from US_modules.DateBeforeCurrent import dateBeforeCurrentDate
from US_modules.MarriageBeforeDeath import MarriageBeforeDeath
from US_modules.divorceBeforeDeath import divorceBeforeDeath

class Family():
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
            "Children": []
        }[attribute] = value
        assert len(family_dict) == len(test_family), 'Error: dictionary length of test family does not match original family dictionary'
        try: 
            function(family.get_family_list())
            print(f"{function.__name__} Unit Test Success ✅")
        except AssertionError:
            print(f"Error: {AssertionError} on function {function.__name__} ❌")

    # Creating a function to return the list of families
    def get_family_list(self):
        return self.family_list


class FamilyTests(unittest.TestCase):
    def checkDatesBeforeCurrent(self):
        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '1 JAN 2025'
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '3 DEC 2010'
        try:
            dateBeforeCurrentDate(individual.get_individual_list(), family.get_family_list())
            print('Individual birthday is before current date:' + str(individual.get_individual_list()[0]['Birthday']))
        except AssertionError:
            print('Failed successfully with error:'  )

        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '1 JAN 1990'
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '3 DEC 2030'
        try:
            dateBeforeCurrentDate(individual.get_individual_list(), family.get_family_list())
            print('Marriage date is before current date:' + str(family.get_family_list()[0]['Marriage Date']))
        except AssertionError:
            print('Failed successfully with error:'  )

        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '1 JAN 1990'
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '3 DEC 2010'
        try:
            dateBeforeCurrentDate(individual.get_individual_list(), family.get_family_list())
            print('Marriage and birth date is before current date:' + str(family.get_family_list()[0]['Marriage Date']))
        except AssertionError:
            print('Failed successfully with error:'  )

        individual = Individual()
        individual.create_individual(individual_dict)['Death'] = '1 JAN 2050'
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '3 DEC 2010'
        try:
            dateBeforeCurrentDate(individual.get_individual_list(), family.get_family_list())
            print('Marriage and death date is before current date:' + str(family.get_family_list()[0]['Marriage Date']))
        except AssertionError:
            print('Failed successfully with error:' )
        
        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '1 JAN 2050'
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '3 DEC 2030'
        try:
            dateBeforeCurrentDate(individual.get_individual_list(), family.get_family_list())
            print('Marriage date is before current date:' + str(family.get_family_list()[0]['Marriage Date']))
        except AssertionError:
            print('Failed successfully with error:' )

    def checkMarriageBeforeDivorce():
        family=Family()
        family.create_family(family_dict)['Marriage Date'] = '1 JAN 2000'
        family['Divorced'] = '1 JAN 1990'
        #test 1
        try:
            marriageBeforeDivorce(family.get_family_list())
            print(f"Marriage date is after divorce date: {str(family.get_family_list()[0]['Married'])} ❌")
        except:
            print(f"Failed successfully with error {str(family.get_family_list()[0]['Married'])} ✅") 
        #test 2
        family=Family()
        family.create_family(family_dict)['Marriage Date'] = '1 JAN 2000'
        family.get_family_list()[0]['Divorce Date'] = 'N/A'
        try:
            marriageBeforeDivorce(family.get_family_list())
            print(f"Marriage date is before divorce date: {str(family.get_family_list()[0]['Married'])} ✅")
        except:
            print(f"Failed with error {str(family.get_family_list()[0]['Married'])} ❌")
        #test 3
        family=Family()
        family.create_family(family_dict)['Marriage Date'] = '6 JAN 2010'
        family.get_family_list()[0]['Divorce Date'] = '1 JAN 2000'
        try:
            marriageBeforeDivorce(family.get_family_list())
            print(f"Marriage date is before divorce date: {str(family.get_family_list()[0]['Married'])} ✅")
        except:
            print(f"Failed with error {str(family.get_family_list()[0]['Married'])} ❌")
        #test 4
        family=Family()
        family.create_family(family_dict)['Marriage Date'] = '18 JAN 2013'
        family.get_family_list()[0]['Divorce Date'] = '19 AUG 2000'
        try:
            marriageBeforeDivorce(family.get_family_list())
            print(f"Marriage date is after divorce date: {str(family.get_family_list()[0]['Married'])} ❌")
        except:
            print(f"Failed successfully with error {str(family.get_family_list()[0]['Married'])} ✅")
        #test 5
        family=Family()
        family.create_family(family_dict)['Marriage Date'] = '1 JAN 2000'
        family.get_family_list()[0]['Divorce Date'] = '28 DEC 1999'
        try:
            marriageBeforeDivorce(family.get_family_list())
            print(f"Marriage date is after divorce date: {str(family.get_family_list()[0]['Married'])} ❌")
        except:
            print(f"Failed successfully with error {str(family.get_family_list()[0]['Married'])} ✅")

        

    def checkDivorceBeforeDeath(self):
        individual = Individual()
        individual.create_individual(individual_dict)['Death'] = '1 JAN 2005'
        individual.get_individual_list()[0]['ID'] = "I1"
        family = Family()
        family.create_family(family_dict)['Divorce Date'] = '3 DEC 2010'
        family.get_family_list()[0]['Husband ID'] = "I1"
        try:
            divorceBeforeDeath(individual.get_individual_list(), family.get_family_list())
            print('Divorce date is before death date: ' + str(family.get_family_list()[0]['Divorce Date']))
        except:
            print('Failed successfully with error: Divorce is after death, Divorced: ' + str(family.get_family_list()[0]['Divorce Date']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Death'] = '1 JAN 2010'
        individual.get_individual_list()[0]['ID'] = "I1"
        family = Family()
        family.create_family(family_dict)['Divorce Date'] = '3 DEC 2050'
        family.get_family_list()[0]['Husband ID'] = "I1"
        try:
            divorceBeforeDeath(individual.get_individual_list(), family.get_family_list())
            print('Divorce date is before death date: ' + str(family.get_family_list()[0]['Divorce Date']))
        except:
            print('Failed successfully with error: Divorce is after death, Divorced: ' + str(family.get_family_list()[0]['Divorce Date']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Death'] = '1 JAN 2019'
        individual.get_individual_list()[0]['ID'] = "I1"
        family = Family()
        family.create_family(family_dict)['Divorce Date'] = '3 DEC 2052'
        family.get_family_list()[0]['Husband ID'] = "I1"
        try:
            divorceBeforeDeath(individual.get_individual_list(), family.get_family_list())
            print('Divorce date is before death date: ' + str(family.get_family_list()[0]['Divorce Date']))
        except:
            print('Failed successfully with error: Divorce is after death, Divorced: ' + str(family.get_family_list()[0]['Divorce Date']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Death'] = '1 JAN 2000'
        individual.get_individual_list()[0]['ID'] = "I1"
        family = Family()
        family.create_family(family_dict)['Divorce Date'] = '3 DEC 2053'
        family.get_family_list()[0]['Husband ID'] = "I1"
        try:
            divorceBeforeDeath(individual.get_individual_list(), family.get_family_list())
            print('Divorce date is before death date: ' + str(family.get_family_list()[0]['Divorce Date']))
        except:
            print('Failed successfully with error: Divorce is after death, Divorced: ' + str(family.get_family_list()[0]['Divorce Date']) )

        individual = Individual()
        individual.create_individual(individual_dict)['Death'] = '1 JAN 2008'
        individual.get_individual_list()[0]['ID'] = "I1"
        family = Family()
        family.create_family(family_dict)['Divorce Date'] = '3 DEC 2009'
        family.get_family_list()[0]['Husband ID'] = "I1"
        try:
            divorceBeforeDeath(individual.get_individual_list(), family.get_family_list())
            print('Divorce date is before death date: ' + str(family.get_family_list()[0]['Divorce Date']))
        except:
            print('Failed successfully with error: Divorce is after death, Divorced: ' + str(family.get_family_list()[0]['Divorce Date']) )


    def birth_before_marriage():
        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '5 DEC 2019' 
        individual.get_individual_list()[0]['ID'] = 'I1'
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '1 JAN 2002'
        family.get_family_list()[0]['Husband ID'] = 'I1'
        try:
            birth_before_marriage(family.get_family_list(), individual.get_individual_list())
            print('Individual birthday is after Marriage Date:' + str(individual.get_individual_list()[0]['Birthday']) + ' | ' + str(family.get_family_list()[0]['Marriage Date']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) + ' | ' + str(family.get_family_list()[0]['Marriage Date']))

        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '3 DEC 2020' 
        individual.get_individual_list()[0]['ID'] = 'I1'
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '1 JAN 2000'
        family.get_family_list()[0]['Husband ID'] = 'I1'
        try:
            birth_before_marriage(family.get_family_list(), individual.get_individual_list())
            print('Individual birthday is after Marriage Date:' + str(individual.get_individual_list()[0]['Birthday']) + ' | ' + str(family.get_family_list()[0]['Marriage Date']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) + ' | ' + str(family.get_family_list()[0]['Marriage Date']))

        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '3 AUG 2020' 
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '1 JAN 1990'
        try:
            birth_before_marriage(family.get_family_list(), individual.get_individual_list())
            print('Individual birthday is after Marriage Date:' + str(individual.get_individual_list()[0]['Birthday']) + ' | ' + str(family.get_family_list()[0]['Marriage Date']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) + ' | ' + str(family.get_family_list()[0]['Marriage Date']))

        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '30 JAN 2022'
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '15 AUG 2010' 
        try:
            birth_before_marriage(family.get_family_list(), individual.get_individual_list())
            print('Individual birthday is after Marriage Date:' + str(individual.get_individual_list()[0]['Birthday']) + ' | ' + str(family.get_family_list()[0]['Marriage Date']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) + ' | ' + str(family.get_family_list()[0]['Marriage Date']))

        individual = Individual()
        individual.create_individual(individual_dict)['Birthday'] = '15 AUG 2010' 
        family = Family()
        family.create_family(family_dict)['Marriage Date'] = '10 FEB 1999'
        try:
            birth_before_marriage(family.get_family_list(), individual.get_individual_list())
            print('Individual birthday is after Marriage Date:' + str(individual.get_individual_list()[0]['Birthday']) + ' | ' + str(family.get_family_list()[0]['Marriage Date']))
        except:
            print('Failed successfully with error:' + str(individual.get_individual_list()[0]['Birthday']) + ' | ' + str(family.get_family_list()[0]['Marriage Date']))    


runner = unittest.TextTestRunner()
runner.run(FamilyTests('checkDivorceBeforeDeath'))
        
    