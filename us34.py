from project03 import indi_list,fam_list,calculateAge,splitBdate,isAlive
import datetime




def recentBirthList(list_individual):
    recentBirthList = []
    for i in list_individual:
        if(i[3] != 0):
            dateOfBirth = i[3]
            dateB = datetime.strptime(dateOfBirth, "%Y-%m-%d")
            delta = datetime.date(datetime.now()) - datetime.date(dateB)
        if delta.days < 30 and delta.days >= 0:
            recentBirthList.add(i[0])
            print("User story 35, the individual"+ i[0] + "is born recently ")
    if (len(recentBirthList) != 0):
        print("User story 34, the following individuals are born recently")
        print(recentBirthList)
    else:
        print("User story 34,there are no individuals who are born recently")     