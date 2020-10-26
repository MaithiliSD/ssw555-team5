import unittest 
from us14 import toParse, multipleBirthslessThan5 
from us16 import maleLastNames

class TestStringMethods(unittest.TestCase):
    def test14(self):
        indiList, famList = toParse("project02_gedcom.ged")
        ans = multipleBirthslessThan5(indiList, famList)
        lenOfList = len(ans)
        self.assertEqual(lenOfList, 0, "Should be 0")
        
    def test16(self):
        indiList, famList = toParse("project02_gedcom.ged")
        ans = maleLastNames(indiList, famList)
        lenOfList = len(ans)
        self.assertEqual(lenOfList, 0, "Should be 0")
        
        		
unittest.main()