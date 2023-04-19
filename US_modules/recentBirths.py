# from datetime import datetime,timedelta
# #Lists all births within the past year
# def recent_Births(individual_list):
#         recentBirths = []
#         cnt = 0
#         for individual in individual_list:
#             print(datetime.now() - datetime.strptime(individual['Birthday'], '%d %b %Y').date())

#             if(datetime.now() - datetime.strptime(individual['Birthday'], '%d %b %Y').date() < timedelta(days=365)):
#                   recentBirths.append(individual['ID'])
#                   cnt+=1
#         print(recentBirths)
#         assert(len(recentBirths) == cnt)


from datetime import datetime, timedelta

def recent_Births(individual_list):
    recentBirths = []
    for individual in individual_list:
        days_since_birth = datetime.now().date() - datetime.strptime(individual['Birthday'], '%d %b %Y').date()
        if days_since_birth < timedelta(days=365):
              recentBirths.append(individual['ID'])
    print(recentBirths)
    assert(len(recentBirths) == len(recentBirths))