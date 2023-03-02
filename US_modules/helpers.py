from datetime import datetime, date

def findKeyInArray(array, key):
        for i in range(len(array)):
            if array[i]['ID'] == key:
                return array[i]
        return -1

def stringToDate(date):
    # if date=='N/A':
    #     return datetime.now().date()
    # date = date.split()
    # day, month, year = int(date[0]), int(
    #     datetime.strptime(date[1], "%b").month), int(date[2])
    # return datetime(year, month, day)
    if date == 'N/A':
        return datetime.now().date()
    return datetime.strptime(date, "%d %b %Y").date()
    
    
def isOverlap(start1, end1, start2, end2):
    if start1<start2<end1:
        return True
    if start2<start1<end2:
        return True
    return False