#Justus US37
from datetime import datetime, date
def listRecentSurvivors(individual_list,family_list):
    for individual in individual_list:
        if individual['Death'] != 'N/A':
            date = individual['Death'].split()
            day, month, year = int(date[0]), int(
                datetime.strptime(date[1], "%b").month), int(date[2])
            curDay, curMonth, curYear = datetime.today().day, datetime.today().month, datetime.today().year
            if(year > curYear or (year == curYear and month > curMonth) or (year == curYear and month==curMonth and day > curDay)):
                print("Recent Survivor - ID: ", individual['ID'])
            
            
        else:
            print("Recent Survivor - ID: ", individual['ID'])
            
    
    assert(True)
        

