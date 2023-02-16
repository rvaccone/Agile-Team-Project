from datetime import datetime, date
def birth_before_death(individual_list):
    for individual in individual_list:
        if individual['Death'] != 'N/A' and individual['Birthday'] != 'N/A':
                birthdate = individual['Birthday'].split()
                Birthday, Birthmon, Birthyear = int(birthdate[0]), int(datetime.strptime(birthdate[1], "%b").month), int(birthdate[2])

                deathdate = individual['Death'].split()
                Deathday, Deathmon, Deathyear = int(deathdate[0]), int(datetime.strptime(deathdate[1], "%b").month), int(deathdate[2])

                assert(Deathyear > Birthyear or (Deathyear == Birthyear and Deathmon > Birthmon) or (Deathyear == Birthyear and Deathmon == Birthmon and Deathday > Birthday)), "Birth is before Death"