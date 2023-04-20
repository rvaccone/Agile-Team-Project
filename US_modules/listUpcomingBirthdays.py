#Justus US38
from datetime import datetime, date
def listUpcomingBirthdays(individual_list,family_list):
    for individual in individual_list:
        if individual['Birthday'] != 'N/A':
            date = individual['Birthday'].split()
            day, month, year = int(date[0]), int(
                datetime.strptime(date[1], "%b").month), int(date[2])
            curDay, curMonth, curYear = datetime.today().day, datetime.today().month, datetime.today().year
            if(month == curMonth and day > curDay):
                print("Upcoming Birthday - ID: ", individual['ID'], " - Birthday: ", date)
            
   
        

