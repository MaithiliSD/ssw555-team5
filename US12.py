import unittest
from datetime import datetime
from typing import Dict, TextIO
from typing import Union

from project03 import gedcomRead

individual, Families = gedcomRead("project02_gedcom.ged")


def getAge(born):
    """returns age of individual"""
    born = datetime.strptime(born, '%d %b %Y')
    today = datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def checkForOldParents(fam: Dict, ind: Dict, file: TextIO):
    """check the age of individuals and return boolean value if parent are old"""
    result: bool = True
    for f in fam:
        if "CHIL" in fam[f]:
            wife: str = "0"
            husb: str = "0"
            if "HUSB" in fam[f]:
                husb: str = fam[f]["HUSB"]
            if "WIFE" in fam[f]:
                wife: str = fam[f]["WIFE"]
            wifeAge: int = 0
            husbAge: int = 0
            if wife in ind and "BIRT" in ind[wife]:
                wifeAge: Union[int, bool] = getAge(ind[wife]["BIRT"])
            if husb in ind and "BIRT" in ind[husb]:
                husbAge: Union[int, bool] = getAge(ind[husb]["BIRT"])
            for c in fam[f]["CHIL"]:
                childAge: int = 0
                if "BIRT" in ind[c]:
                    childAge: Union[int, bool] = getAge(ind[c]["BIRT"])
                if wifeAge - childAge > 60:  # throw wife error
                    file.write(
                        "US12: Mother " + wife + " is older than their child, " + c + " by over 60 years\n")
                    result: bool = False
                if husbAge - childAge > 80:  # throw husb error
                    file.write(
                        "US12: Father " + husb + " is older than their child, " + c + " by over 80 years\n")
                    result: bool = False
    return result


class TestCases(unittest.TestCase):
    def test_checkForOldParents(self):
    
        f = open("Output.txt", "a+")
        fam: Dict = {'F23':
                         {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07',
                          'CHIL': ['I19', 'I26', 'I30']},
                     'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
        fam2: Dict = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19']}}

        ind1: Dict = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1900', 'sex': 'M', 'family': 'F23',
                              'DEAT': '31 DEC 2013'},
                      'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1902', 'sex': 'F',
                              'family': 'F23',
                              'DEAT': '31 DEC 2013'},
                      'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1999', 'sex': 'M', 'family': 'F23',
                              'DEAT': '31 DEC 2013'}}

        ind2: Dict = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23',
                              'DEAT': '31 DEC 2013'},
                      'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F',
                              'family': 'F23'},
                      'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
                      'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
                      'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
                      'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
                      'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F',
                              'family': 'F23'}}

        self.assertTrue(checkForOldParents(fam, ind2, f))
        self.assertFalse(checkForOldParents(fam2, ind1, f))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)