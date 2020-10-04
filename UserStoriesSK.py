from project3 import indi_list,fam_list,calculateAge
from datetime import datetime,date
from dateutil.relativedelta import relativedelta
import datetime
#import unittest



def husbandage(value,md,indi):
   
        for j in indi:
            
            if(value==j[0]):
             
                dateid=datetime.datetime.strptime(j[3],'%Y %b %d').strftime('%Y%m%d %H:%M:%S')
                dateiy=int(dateid[0:4])
                if(dateid[4]=='0'):
                    dateim=int(dateid[5])
                else:
                    dateim=int(dateid[4:6])
                dateidd=int(dateid[6: 8]) 
                          
                datemd=datetime.datetime.strptime(md,'%Y %b %d').strftime('%Y%m%d %H:%M:%S')
                datemy=int(datemd[0:4])
                if(dateid[4]=='0'):
                    datemm=int(dateid[5])
                else:
                    datemm=int(dateid[4:6])
                datemdd=int(datemd[6:8])

                d0 = datetime.datetime(dateiy, dateim, dateidd)

           
                d1 = datetime.datetime(datemy, datemm, datemdd)

                timehd=relativedelta(d1,d0).years
                return timehd



def wifeage(value1,md,indi):

    for j in indi:
        if(value1==j[0]):
                
                dateid=datetime.datetime.strptime(j[3],'%Y %b %d').strftime('%Y%m%d %H:%M:%S')
                dateiy=int(dateid[0:4])
                
                if(dateid[4]=='0'):
                    dateim=int(dateid[5])
                else:
                    dateim=int(dateid[4:6])
                
                dateidd=int(dateid[6: 8]) 
                          
                datemd=datetime.datetime.strptime(md,'%Y %b %d').strftime('%Y%m%d %H:%M:%S')
                
                datemy=int(datemd[0:4])
                if(dateid[4]=='0'):
                    datemm=int(dateid[5])
                else:
                    datemm=int(dateid[4:6])
                datemdd=int(datemd[6:8])

                d0 = datetime.datetime(dateiy, dateim, dateidd)
           
                d1 = datetime.datetime(datemy, datemm, datemdd)
                
                timewd=relativedelta(d1,d0).years
                return timewd

def us10(indi, fam):
    print("US 10 - Marriage should be after 14 years of age, Runnning")
    for f in fam:
        
        hd=husbandage(f[1],f[3],indi)
        wd=wifeage(f[2],f[3],indi)
        if hd>14 and wd>14:
            print("Parent age is greater than 14")
        else:
            print("Child marriage")

        #result=checkcondition(hd,wd)

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
                        
                





# def checkcondition(t1,t2):
#     if t1>14 and t2>14:
#         return True
#     else:
#         return False


# class TestCheck(unittest.TestCase):
#     def test_True(self):
#         self.assertTrue(checkcondition(18,18),True)

#     def test_True2(self):
#         self.assertFalse(checkcondition(18,5),True)
    
#     def test_false(self):
#         self.assertFalse(checkcondition(18,2),False)
#     def test_equal(self):
#         self.assertEqual(checkcondition(18,19),True)

#     def test_equal2(self):
#         self.assertEqual(checkcondition(13,13),False)
    
#     def test_NotEqual(self):
#         self.assertNotEqual(checkcondition(14,13),True)
    
   
  
    

        


def main()->None:
   
    us10(indi_list,fam_list)
    us08(indi_list,fam_list)

if __name__ == "__main__":
    main()