from project3 import indi_list,fam_list,calculateAge
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
import datetime
from prettytable import PrettyTable

def getIndiByID(indi, iD):
    return next((dictionary for dictionary in indi if dictionary[0] == iD), None)

def calculateage(birth, death):
    from datetime import date
    latest = date.today()
    if death != "NA":
        latest = death.date()

    days_in_year = 365.2425
    age = int((latest - birth.date()).days / days_in_year)
    return str(age)



def us33(indi, fam):
    print("User Story 33 - List orphans, running")
    orphans = list()
    for family in fam:
        children_ids = family[5]
        if children_ids == 0:
            continue
        husb = getIndiByID(indi, family[1])
        wife = getIndiByID(indi, family[2])
        print(husb)
        print("below wife")
        print(wife)
        print("below child")
        if husb[4] == 0 or wife[4] == 0:
            continue
        # both parents are dead
        for i in children_ids:
            child = getIndiByID(indi, i)
            print(child)
            if child[4] != 0:
                continue

            #a = calculateage(child[3], 0)
            if int(calculateage(child[3], 0)) < 18:
                orphans.append(child)
    if not orphans:
        print("no orphan")
    else:
        print(orphans)
        

def main()->None:
   
   
    us33(indi_list,fam_list)

if __name__ == "__main__":
    main()