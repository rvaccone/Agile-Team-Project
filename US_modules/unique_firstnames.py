def unique_first(individual_list):
    name_dict = {}
    childarray = []

    for individual in individual_list:
        name_array = individual['Name'].split()
        first_name = name_array[0]
        name_dict[individual['ID']] = first_name

    for individual in individual_list:
        children = individual['Children']
        for child in children:
            childarray.append(name_dict.get(child))
        childset = set(childarray)
        assert len(childset) == len(childarray), f"At least two children have the same name"