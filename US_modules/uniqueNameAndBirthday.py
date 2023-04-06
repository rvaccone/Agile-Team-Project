#No more than one individual with the same name and birth date should appear in a GEDCOM file
def uniqueNameAndBirthday(individual_list):
    individual_pair = set()
    for individual in individual_list:
        assert (individual["Name"], individual["Birthday"]) not in individual_pair, "Individual has the same name and birthday as another individual"
        individual_pair.add((individual["Name"], individual["Birthday"]))
    


    # for individual in individual_list:
    #     for individual2 in individual_list:
    #         if individual['Name'] == individual2['Name'] and individual['Birthday'] == individual2['Birthday']:
    #             2+2
                # assert(individual['ID'] != individual2['ID']), "Individual has the same name and birthday as another individual"
