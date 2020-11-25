from datetime import datetime
from datetime import date
from prettytable import PrettyTable
from project03 import indi_list,fam_list

def us28(indi, fam):
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
    return flag

us28(indi_list, fam_list)