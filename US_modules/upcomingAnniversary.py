#TaeSeo 

# list any upcoming anniversaries for the next 365 days if both spouses are alive


import datetime

def is_spouse_alive(spouse_id, individual_list):
    for individual in individual_list:
        if individual["ID"] == spouse_id:
            return individual["Alive"]
    return False

def upcoming_anniversary(individual_list, family_list):
    today = datetime.date.today()
    upcoming = []
    
    for family in family_list:
        if family["Marriage Date"] == "N/A" or family["Divorce Date"] != "N/A":
            continue
        
        husband_alive = is_spouse_alive(family["Husband ID"], individual_list)
        wife_alive = is_spouse_alive(family["Wife ID"], individual_list)

        if husband_alive and wife_alive:
            upcoming.append(family["Marriage Date"])
    
    upcoming.sort()
    return upcoming
