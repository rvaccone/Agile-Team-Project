# [US22] - Rocco
def uniqueIDS(individual_list, family_list):
    individual_IDs, family_IDs = set(), set()
    for individual in individual_list:
        assert individual["ID"] not in individual_IDs, "Individual ID is not unique"
        individual_IDs.add(individual["ID"])

    for family in family_list:
        assert (
            family["ID"] not in family_IDs and family["ID"] not in individual_IDs
        ), "Family ID is not unique"
        family_IDs.add(family["ID"])
    return True
