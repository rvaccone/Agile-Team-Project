# Creating a dictionary to contain values for each individual
individual_dict = {
    "ID": "N/A",
    "Name": "N/A",
    "Sex": "N/A",
    "Birthday": "N/A",
    "Age": "N/A",
    "Alive": True,
    "Death": "N/A",
    "Family": "N/A",
    "Spouse": "N/A",
    "Children": []
}

# Creating a dictionary to contain values for each family
family_dict = {
    "ID": "N/A",
    "Marriage Date": "N/A",
    "Divorce Date": "N/A",
    "Husband ID": "N/A",
    "Wife ID": "N/A",
    "Children": [],
}

# Creating a dictionary to map the individual tags to the dictionary keys
gedcom_individual_map = {
    "NAME": "Name",
    "SEX": "Sex",
    "FAMS": "Spouse",
}

# Creating a dictionary to map the family tags to the dictionary keys
gedcom_family_map = {
    "HUSB": "Husband ID",
    "WIFE": "Wife ID",
}
