# [US32] - Rocco
# List all living people over 30 who have never been married in a GEDCOM file
def listLivingSingle(ind_list, fam_list):
    # Creating a set of individuals to track who is married (defined by having a marriage date in their family)
    mar_inds = set()

    # iterating through the families to add the husband and wife to the set of married individuals
    for fam in fam_list:
        if fam["Marriage Date"] != "N/A":
            mar_inds.add(fam["Husband ID"])
            mar_inds.add(fam["Wife ID"])

    # Double list comprehension to return a list of individuals who are not married and are over 30
    return [
        ind['ID']
        for ind in [ind for ind in ind_list if ind["ID"] not in mar_inds]
        if ind["Age"] != "N/A" and ind["Age"] > 30
    ]
