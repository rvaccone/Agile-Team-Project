#No more than one family with the same spouses by name and the same marriage date should appear in a GEDCOM file
def uniqueFamilyBySpouses(family_list, individual_list):
    # print(family_list)
    spouseAndMarriage = set()
    for family in family_list:
        assert (family["Husband Name"], family["Wife Name"], family["Marriage Date"]) not in spouseAndMarriage, "Family has the same spouses and marriage date as another family"
        spouseAndMarriage.add((family["Husband Name"], family["Wife Name"], family["Marriage Date"]))