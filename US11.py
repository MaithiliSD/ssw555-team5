import unittest
from typing import List, Dict
from typing import List, Dict, TextIO

from project03 import gedcomRead

indi_list, fam_list = gedcomRead("project02_gedcom.ged")

def checkBigamy(fam: Dict, file: TextIO):
     
    for f in fam:
        if 'HUSB' in fam[f]:
            hus_id = fam[f]['HUSB']
            if 'WIFE' in fam[f]:
                wife_id = fam[f]['WIFE']

        wife_count = 0
        husb_count = 0

        for f in fam:
            if 'HUSB' in fam[f]:
                hus_id2: List = fam[f]['HUSB']
                if hus_id == hus_id2:
                    husb_count += 1
                if 'WIFE' in fam[f]:
                    wife_id2: List = fam[f]['WIFE']
                    if wife_id == wife_id2:
                        wife_count += 1
            else:
                continue


            if husb_count > 1:
                
                file.write("US11: Marriage should not occur during marriage to another spouse\n")
                fam.pop(hus_id, None)
                indi.pop(hus_id, None)
                break
            if wife_count > 1:
                file.write("US11: Marriage should not occur during marriage to another spouse\n")
                fam.pop(hus_id, None)
                indi.pop(hus_id, None)
                break

def popped(lst: str):
    
    fam.pop(lst, None)
    indi.pop(lst, None)

      
if __name__ == "__main__":
    unittest.main(exit=True, verbosity=2)
