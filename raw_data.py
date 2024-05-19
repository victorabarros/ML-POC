import random
from datetime import datetime

def getRawData():
    """return array of tuples (dayOfWeek, hour, nofEntries)"""
    day_hour_count = []

    # monday
    d = 6
    day_hour_count.extend([(d, 8, 3),(d,9, 5),(d,10, 4),(d,11, 7),(d,16, 7),(d,17, 8)])
    # tuesday
    d=7
    day_hour_count.extend([(d, 11, 3),(d, 12, 9),(d, 13, 6)])
    # wednesday
    d=8
    day_hour_count.extend([(d, 8, 8),(d, 9, 4),(d, 10, 3),(d, 16, 3),(d, 17, 5)])
    # thursday
    d=9
    day_hour_count.extend([(d, 8, 4),(d, 9, 2),(d, 10, 3),(d, 11, 5),(d, 16, 4),(d, 17, 7)])
    # friday
    d=10
    day_hour_count.extend([(d, 8, 7),(d, 9, 5),(d, 10, 8),(d, 11, 7),(d, 16, 9),(d, 17, 5)])
    # saturday
    d=11
    day_hour_count.extend([(d, 9, 1),(d, 10, 1)])
    # sunday
    d=12
    day_hour_count.extend([(d, 14, 1),(d, 15, 2)])

    return day_hour_count

## return a full week of user behaviour
def getDataSet():
    """return array datetime of entries from May 6 2024 to May 12 2024"""
    year = 2024
    month = 5

    data_set = []
    for d, h, c in getRawData():
        for i in range(c):
            ts = datetime(year, month, d, h, random.randint(0, 59), random.randint(0, 59))
            data_set.append(ts)
    return data_set
