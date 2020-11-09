import unittest
from prettytable import PrettyTable
from datetime import datetime
from project03 import gedcomRead

Families = gedcomRead("project02_gedcom.ged")

def get_anniversary_date(family):
    if "MARR" in family:
        marriage = datetime.strptime(family["MARR"], '%d %b %Y')
        return marriage
    else:
        return 0
	

def us_39_print_upcoming_anniversaries(Families):
    table = PrettyTable(["ID","Anniversary"])
    result = False 
    for family_id in Families:
        family = Families[family_id]
        today = datetime.today()
        family_marriage = get_anniversary_date(family)
        if family_marriage is not 0:
            family_current_anniversary = datetime(today.year, family_marriage.month, family_marriage.day)
            if 0 <= (abs(family_current_anniversary - today)).days <= 30:
                table.add_row([family["fam"], family_marriage])
                result = True
                return result
	

fam = {'F23': #birth date of Dick Smith and Jane Smith more than 8 months apart 
{'fam': 'F23', 'MARR': '7 AUG 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
	

class MyTest(unittest.TestCase):
    def test(self):
        us_39_print_upcoming_anniversaries(fam)
#        f=open("jeneleeOutput.txt","a+")
#        f.close()
	        
if __name__ == "__main__":
    unittest.main(exit=True, verbosity=2)
