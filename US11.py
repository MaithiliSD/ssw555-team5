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


# No Bigamy
fam = {'F23':
           {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
       'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}

indi = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                'DEAT': '31 DEC 2013'},
        'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
        'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
        'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
        'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
        'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
        'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

# bigamy (same husband)
fam2 = {'F23':
            {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
        'F16': {'fam': 'F16', 'MARR': '12 DEC 2007', 'HUSB': 'I01'}}

indi2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                 'DEAT': '31 DEC 2013'},
         'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
         'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
         'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
         'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
         'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
         'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

# bigamy (same wife)
fam3 = {'F23': 
            {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
        'F16': {'fam': 'F16', 'MARR': '12 DEC 2007', 'WIFE': 'I07'}}

indi3 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                 'DEAT': '31 DEC 2013'},
         'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
         'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
         'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
         'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
         'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
         'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}


class gedComTestCases(unittest.TestCase):
    """Unit test suite"""
    def test_checkBigamy(self):
        """Test cases for bigamy"""
        
      
        file = open("output1.txt", "a+")
        checkBigamy(fam, file)
        self.assertTrue(('I01' in indi))
        self.assertTrue(('I01' == fam['F23']['HUSB']))
        checkBigamy(fam2, file)
        self.assertTrue(('I01' in indi2))
        self.assertTrue(('I01' in fam2['F23']['HUSB']))
        checkBigamy(fam3, file)
        self.assertTrue(('I07' in indi3))
        self.assertTrue(('WIFE' in fam3['F23']))
        file.close()


if __name__ == "__main__":
    unittest.main(exit=True, verbosity=2)
