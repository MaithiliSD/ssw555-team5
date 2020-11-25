from project03 import indi_list,fam_list,calculateAge
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
import datetime
from prettytable import PrettyTable

def us37(indi,fam):
    
    x=PrettyTable()
    x.field_names=["Name","HUSBAND/WIFE/CHILDREN","FAMILY_ID","GENDER"]
    for family in fam:
        count=0
        for inv in indi:
            if(family[1]==inv[0] and inv[4]==0):
                count=count+1
                name=inv[1].replace('/', ' ')
                val="HUSBAND"
                fid=family[0]
                gen=inv[3]
            if(family[2]==inv[0] and inv[4]==0):
                count=count+1
                name=inv[1].replace('/', ' ')
                val="WIFE"
                fid=family[0]
                gen=inv[3]
        if(count==1):
            x.add_row([name,val,fid,gen])
            if(family[5]!='NA'):
                for i in range(len(family[5])):
                    for invd in indi:
                        if(family[5][i]==invd[0] and invd[4]==0):
                            name1=invd[1]
                            val="CHILDREN"
                            fid=family[0]
                            gen=inv[3]
                            x.add_row([name1,val,fid,gen])
    print(x)
              
def main()->None:
    us37(indi_list,fam_list)

if __name__ == "__main__":
    main()