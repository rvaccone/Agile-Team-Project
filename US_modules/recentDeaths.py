#Lists all Deaths within the past year
from datetime import datetime, timedelta

def recent_Death(individual_list):
    recentDeath = []
    for individual in individual_list:
        days_since_death = datetime.now().date() - datetime.strptime(individual['Death'], '%d %b %Y').date()
        if days_since_death < timedelta(days=365):
              recentDeath.append(individual['ID'])
    print(recentDeath)
    assert(len(recentDeath) == len(recentDeath))
                
        
    
        
    