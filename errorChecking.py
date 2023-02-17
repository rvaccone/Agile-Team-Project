# Importing modules
from datetime import datetime, date

# Importing US modules
from US_modules.DateBeforeCurrent import dateBeforeCurrentDate
from US_modules.Parents_not_too_old import parents_not_too_old
from US_modules.individual_is_too_young_to_be_married import individual_is_too_young_to_be_married
from US_modules.ageIsLessThan150 import ageIsLessThan150
from US_modules.divorceBeforeDeath import divorceBeforeDeath

# Initial error checking of incorrect lines
def initial_error_checking(gedcom_lines):
    for index, line in enumerate(gedcom_lines):
        # if the line is a level 0 tag
        if line[0] == "0":
            pass

        # if the line is a level 1 tag
        elif line[0] == "1":
            # Asserting that 1 DATE is not present
            assert(line.split()[-1] != "DATE")

        # if the line is a level 2 tag
        elif line[0] == "2":
            # Asserting that 2 NAME is not present
            assert(line.split()[1] != "NAME")

# List of individual functions
individual_functions = [
    parents_not_too_old,
    individual_is_too_young_to_be_married,
    ageIsLessThan150
]

# Error checking the individuals
def individuals_error_checking(individual_list):
    print('-'*50, 'Starting Individual Error Checking', '-'*50)
    counter = 0
    for function in individual_functions:
        try: 
            function(individual_list)
            print(f"Success {function.__name__} ✅")
        except AssertionError: 
            print(f"Error: {AssertionError} on function {function.__name__} ❌")
            counter += 1
    if counter == 0: print("All individual tests passed ✅")
    else: print(f"{counter} tests failed ❌")

# List of family functions
family_functions = [
    divorceBeforeDeath,
    dateBeforeCurrentDate
]

def families_error_checking(individual_list, family_list):
    print('-'*50, 'Starting Family Error Checking', '-'*50)
    counter = 0
    for function in family_functions:
        try:
            function(individual_list, family_list)
            print(f"Success {function.__name__} ✅")
        except AssertionError:
            print(f"Error: {AssertionError} on function {function.__name__} ❌")
            counter += 1
    if counter == 0: print("All family tests passed ✅")
    else: print(f"{counter} tests failed ❌")
