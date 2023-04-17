# [US42] - Rocco
# All dates should be legitimate dates for the months specified (e.g., 2/30/2015 is not legitimate)
# We are mainly verifying that the day is not greater than the month allows

from US_modules.includePartialDates import checkDate

# List of months to reference
months = {
    "jan": 31,
    "feb": 29,
    "mar": 31,
    "apr": 30,
    "may": 31,
    "jun": 30,
    "jul": 31,
    "aug": 31,
    "sep": 30,
    "oct": 31,
    "nov": 30,
    "dec": 31,
}

# Helper function to check if a date is legitimate
def checkIllegitimate(date):
    if  not checkDate(date):
        raise ValueError("Date violates partial date rules")
    
    # Splitting up the date to check for partial dates
    date = date.split()

    if len(date) == 3:
        # Verify that the day is not greater than the month allows
        if int(date[0]) > months[date[1].lower()]:
            raise ValueError("The day number is greater than the month allows")
    
    # Checking if the month is valid is done in checkDate

    return True




def rejectIllegitimateDates(individual_list, family_list):
    # The only dates are:
        # Individuals- Birthday, Death
        # Families- Marriage Date, Divorce Date
    
    # Checking the individuals
    for ind in individual_list:
        # Checking the birthday
        checkIllegitimate(ind["Birthday"])

        # Checking the death
        checkIllegitimate(ind["Death"])

    # Checking the families
    for fam in family_list:
        # Checking the marriage date
        checkIllegitimate(fam["Marriage Date"])

        # Checking the divorce date
        checkIllegitimate(fam["Divorce Date"])
    