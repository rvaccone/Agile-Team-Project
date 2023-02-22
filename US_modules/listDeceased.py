#US29 List Deceased - TaeSeo 

def listDeceased(individual_list):
    deceased_list = []
    number_of_deceased = 0
    for individual in individual_list:
        if individual['Death'] != 'N/A':
            number_of_deceased += 1
            deceased_list.append(individual['ID'])

    return deceased_list, number_of_deceased

    
