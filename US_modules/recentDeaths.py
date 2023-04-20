#Lists all Deaths within the past year
from datetime import datetime, timedelta

def recent_Death(individual_list):
    recent_death_array = []
    for individual in individual_list:
        #Checks if the recent death is within 365 days of today
        days_since_death = datetime.now().date() - datetime.strptime(individual['Death'], '%d %b %Y').date()
        if days_since_death < timedelta(days=365):
              #adds individual id to array
              recent_death_array.append(individual['ID'])
    #prints list of recently deceased
    print(recent_death_array)
    assert(len(recent_death_array) == len(recent_death_array))
                
        
    
        
    