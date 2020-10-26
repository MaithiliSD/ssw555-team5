import unittest
import us02, us03

class TestBirthBeforeMarriage(unittest.TestCase):
    
    def test_birth_marriage(self):
        indiListData, famListData = us02.gedcomParse("project02_gedcom.ged")
        indiListData.sort()
        famListData.sort()
        outputList = us02.birthBeforeMarriage(indiListData, famListData)
        lenOutput = len(outputList);
        self.assertEqual(lenOutput, 0, "Should be 0")
        
    def test_birth_marriage_2(self):
        indiListData, famListData = us02.gedcomParse("project02_gedcom.ged")
        indiListData.sort()
        famListData.sort()
        outputList = us02.birthBeforeMarriage(indiListData, famListData)
        lenOutput = len(outputList);
        self.assertTrue((lenOutput==0), "Should be True")
        
    def test_birth_marriage_3(self):
        indiListData, famListData = us02.gedcomParse("project02_gedcom.ged")
        indiListData.sort()
        famListData.sort()
        outputList = us02.birthBeforeMarriage(indiListData, famListData)
        lenOutput = len(outputList);
        self.assertFalse((lenOutput>0), "Should be False")
        
    def test_birth_marriage_4(self):
        indiListData, famListData = us02.gedcomParse("project02_gedcom.ged")
        indiListData.sort()
        famListData.sort()
        outputList = us02.birthBeforeMarriage(indiListData, famListData)
        lenOutput = len(outputList);
        self.assertIs(lenOutput, 0, "Should be 0")
        
class TestDeathBeforeBirth(unittest.TestCase):
    
    def test_death_birth(self):
        list_individual = us03.gedcomParse("project02_gedcom.ged")
        list_individual.sort()
        outputList = us03.birthBeforeDeath(list_individual)
        lenOutput = len(outputList);
        self.assertEqual(lenOutput, 0, "Should be 0")
        
    def test_death_birth_2(self):
        list_individual = us03.gedcomParse("project02_gedcom.ged")
        list_individual.sort()
        outputList = us03.birthBeforeDeath(list_individual)
        lenOutput = len(outputList);
        self.assertTrue((lenOutput==0), "Should be True")
        
    def test_death_birth_3(self):
        list_individual = us03.gedcomParse("project02_gedcom.ged")
        list_individual.sort()
        outputList = us03.birthBeforeDeath(list_individual)
        lenOutput = len(outputList);
        self.assertFalse((lenOutput>0), "Should be False")
        
    def test_death_birth_4(self):
        list_individual = us03.gedcomParse("project02_gedcom.ged")
        list_individual.sort()
        outputList = us03.birthBeforeDeath(list_individual)
        lenOutput = len(outputList);
        self.assertIs(lenOutput, 0, "Should be 0")