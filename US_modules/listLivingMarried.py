#US30 List Living Married - TaeSeo
# 
def listLivingMarried(individual_list):
    living_married_list = [] 
    number_of_living_married = 0
    for individual in individual_list:
        if individual['Death'] == 'N/A' and individual['Spouse'] != 'N/A':
            number_of_living_married += 1
            living_married_list.append(individual['ID'])

    return number_of_living_married

    
