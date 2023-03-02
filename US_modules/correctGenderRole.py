# [US21] - Rocco
def correctGenderRole(individual_list, family_list):
    for family in family_list:
        # Checking the husband's gender first
        if family["Husband ID"] != "N/A":
            husband = next(
                filter(lambda x: x["ID"] == family["Husband ID"], individual_list)
            )
            assert husband["Sex"] == "M", "Husband in family is not male"

        # Checking the wife's gender now
        if family["Wife ID"] != "N/A":
            wife = next(filter(lambda x: x["ID"] == family["Wife ID"], individual_list))
            assert wife["Sex"] == "F", "Husband in family is not female"
    return True
