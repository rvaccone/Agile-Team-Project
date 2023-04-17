# [US41] - Rocco
# List of months to reference
months = [
    "jan",
    "feb",
    "mar",
    "apr",
    "may",
    "jun",
    "jul",
    "aug",
    "sep",
    "oct",
    "nov",
    "dec",
]

def checkDate(date):
    if date == "N/A":
        return True

    # Splitting up the date to check for partial dates
    date = date.split()

    # Checking for full dates
    if len(date) == 3:
        # The first part of the date should be a number
        if not date[0].isdigit() or len(date[0]) > 2:
            return False

        # The second part of the date should be a month
        if date[1].lower() not in months:
            return False

        # The third part of the date should be a number
        if not date[2].isdigit() or len(date[2]) != 4:
            return False

    # Checking for partial dates without days
    if len(date) == 2:
        # The first part of the date should be a month
        if date[0].lower() not in months:
            return False

        # The second part of the date should be a number
        if not date[1].isdigit() or len(date[1]) != 4:
            return False

    # Checking for partial dates without days and months
    if len(date) == 1:
        # The first part of the date should be a number
        if not date[0].isdigit() or len(date[0]) != 4:
            return False

    # If the date passes all the checks, it is a legitimate date
    return True


# Accept and use dates without days or without days and months
def includePartialDates(individual_list, family_list):
    # For individual, we need to check birthday and death dates
    for ind in individual_list:
        if ind["Birthday"] != "N/A":
            assert checkDate(
                ind["Birthday"]
            ), "Individual's birthday is not a legitimate date"
        if ind["Death"] != "N/A":
            assert checkDate(
                ind["Death"]
            ), "Individual's death is not a legitimate date"

    # For family, we only need to check marriage and divorce dates
    for fam in family_list:
        if fam["Marriage Date"] != "N/A":
            assert checkDate(
                fam["Marriage Date"]
            ), "Family's marriage date is not a legitimate date"
        if fam["Divorce Date"] != "N/A":
            assert checkDate(
                fam["Divorce Date"]
            ), "Family's divorce date is not a legitimate date"
