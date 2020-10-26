from datetime import datetime
from datetime import date
from prettytable import PrettyTable

def us28(indi, fam, f):
    print("Starting User Story 28 - List siblings in families by decreasing age, i.e. oldest siblings first")
    flag = True
    days_in_year = 365.2425
    x=PrettyTable()
    x.field_names=["Names"]
    for fa in fam:
        n=len(fa["CHIL"])
        val={}
        if(n>1 and fa["CHIL"]!="NA"):
            for i in range(n):
                for j in indi:
                    if(fa["CHIL"][i]==j["INDI"]):
                        latest = date.today()
                        if(j["DEAT"]!="NA"):
                            latest=j["DEAT"].date()
                        age = int((latest - j["BIRT"].date()).days / days_in_year)
                        name=j["NAME"]
                        name1=name.replace('/',' ')
                        val.update({name1:age})
            result = sorted(val.items() , key=lambda t : t[1] , reverse=True)
            x.add_row([result])
    print(x)
    f.write(str(x))
    print("User Story 28 Completed")
    return flag