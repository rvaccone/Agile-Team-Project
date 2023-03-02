def fewer_than_fifteen(individual_list, family_list):
    for individual in individual_list:
        individualID = individual['ID']
        sibling_count = 0
        for family in family_list:
            if(individualID in family['Children']):
                sibling_count += len(family['Children'])-1
        assert(sibling_count < 15), "Has more than 15 siblings"

            

