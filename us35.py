from project03 import indi_list,fam_list,calculateAge,splitBdate,isAlive
import datetime

def recentDeaths(listIndi):
    recentDeathList = []
    current=datetime.now()
    for i in listIndi:
        if(i[4] != 0):
            deathDate = i[4]
            dateOfDeath = datetime.strptime(deathDate, "%Y-%m-%d")
            if (current.year - dateOfDeath.year == 0 ):
                if (current.month - dateOfDeath.month == 0 and current.day-dateOfDeath.day > 0):
                    recentDeathList.add(i[0])
                    print("User story 36: The individual with ID"+ i[0] + "died recently ")
    if (len(recentDeathList) == 0):
        print("User story 35: No individual died recently")       
    else:
        print("User story 35: The individual who died recently are as follows:")
        print(recentDeathList)