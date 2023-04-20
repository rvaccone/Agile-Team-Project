
from datetime import datetime, timedelta

def recent_Births(individual_list):
    recent_birth_array = []
    for individual in individual_list:
        #Checks if the recent birth is within 365 days of today
        days_since_birth = datetime.now().date() - datetime.strptime(individual['Birthday'], '%d %b %Y').date()
        if days_since_birth < timedelta(days=365):
              #adds individual id to array
              recent_birth_array.append(individual['ID'])
    #prints list of recently born
    print(recent_birth_array)
    assert(len(recent_birth_array) == len(recent_birth_array))