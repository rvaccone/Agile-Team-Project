from datetime import datetime, date
def dateBeforeCurrentDate (individual_list):
    for individual in individual_list:
        if individual['Birthday'] != 'N/A':
            date = individual['Birthday'].split()
            day, month, year = int(date[0]), int(
                datetime.strptime(date[1], "%b").month), int(date[2])
            curDay, curMonth, curYear = datetime.today().day, datetime.today().month, datetime.today().year
            assert(curYear > year or (year == curYear and curMonth > month) or (year == curYear and curMonth == month and day < curDay)), "Birth date is after today's date"