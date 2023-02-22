# Mateusz
from datetime import datetime, date
def birth_before_death(individual_list):
    def check_date_format(date):
        return bool(datetime.strptime(date,'%d %b %Y'))
    
    for individual in individual_list:
            if(individual['Death'] != 'N/A' and individual['Birthday'] != 'N/A'):
                if(check_date_format(individual['Death']) and check_date_format((individual['Birthday']))):
                    BirthDate = datetime.strptime(individual['Birthday'], '%d %b %Y').date()
                    #Birthday, Birthmon, Birthyear = int(birthdate[0]), int(datetime.strptime(birthdate[1], "%b").month), int(birthdate[2])

                    DeathDate = datetime.strptime(individual['Death'], '%d %b %Y').date()
                    #Deathday, Deathmon, Deathyear = int(deathdate[0]), int(datetime.strptime(deathdate[1], "%b").month), int(deathdate[2])

                    assert(DeathDate > BirthDate)