def male_lname_same(individual_list):
    name_dict = {}
    for individual in individual_list:
        name_array = individual['Name'].split()
        last_name = name_array[-1]
        name_dict[individual['ID']] = last_name

    for individual in individual_list:
        if individual['Sex'] == 'M':
            children = individual['Children']
            father_last_name = name_dict.get(individual['ID'])
            for child in children:
                child_last_name = name_dict.get(child)
                assert child_last_name == father_last_name, f"{individual['ID']} and {child} dont have the same last name"


# def male_lname_same(individual_list):
#     def get_last_name(individual):
#         name_array = individual['Name'].split()
#         return name_array[-1]

#     for individual in individual_list:
#         members = individual['Children']
#         familyID = individual['Family']
#         lastName = get_last_name(individual)
#         for child in members:
#             for individuals in individual_list:
#                 if(individuals['ID'] == child and individuals['Sex'] == 'M'):
#                     assert(lastName == get_last_name(individuals)), "Dont have some last name"
                



    


                

    

        
     




    
                     
            
        
