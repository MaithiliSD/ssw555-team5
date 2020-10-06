from project3 import indi_list,fam_list,calculateAge
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
import datetime

def us08(indi,fam):
    
    print("US- 08- Birth before marriage of parents, running")
    for f in fam:
        marriagedate=datetime.datetime.strptime(f[3],'%Y %b %d').strftime('%Y%m%d')
        if f[4]!= 0:
            divorcedate=datetime.datetime.strptime(f[4],'%Y %b %d').strftime('%Y%m%d')
        else:
            divorcedate=datetime.date.today()
            divorcedate=divorcedate.strftime('%Y%m%d')
            
            

        for c in f[5]:
            for ind in indi:
                if c == ind[0]:
                   
                    birthdate=datetime.datetime.strptime(ind[3],'%Y %b %d').strftime('%Y%m%d')
                    if birthdate>marriagedate and birthdate<divorcedate:
                        print("Child was born after marriage")
                    else:
                        print("Child was born before marriage ")
                        
def main()->None:
   
    us10(indi_list,fam_list)
    us08(indi_list,fam_list)

if __name__ == "__main__":
    main()