from project3 import indi_list,fam_list,calculateAge
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
import datetime
from prettytable import PrettyTable

def us38(indi,fam):
    for individual in indi:
        todays_date = datetime.date.today()
        birth_day=datetime.datetime.strptime(individual[3],'%Y %b %d')
        birth_day=birth_day.date()
        birth_day=birth_day.replace(year=2020)
        diff=(birth_day-todays_date).days
        if 0< diff<30:
            print(birth_day, individual[1])

def main()->None:
   
    
    us38(indi_list,fam_list)
    

if __name__ == "__main__":
    main()