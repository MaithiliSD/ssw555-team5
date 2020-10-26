import unittest
import us13, us27

class TestSiblingsSpacing(unittest.TestCase):
    
    def test_siblings_spacing_1(self):
        indiListData, famListData = us13.gedcomParse("project02_gedcom.ged")
        indiListData.sort()
        famListData.sort()
        outputList = us13.SiblingsSpacing(indiListData, famListData)
        lenOutput = len(outputList);
        self.assertEqual(lenOutput, 0, "Should be 0")
        
    def test_siblings_spacing_2(self):
        indiListData, famListData = us13.gedcomParse("project02_gedcom.ged")
        indiListData.sort()
        famListData.sort()
        outputList = us13.SiblingsSpacing(indiListData, famListData)
        lenOutput = len(outputList);
        self.assertTrue((lenOutput==0), "Should be True")
        
    def test_siblings_spacing_3(self):
        indiListData, famListData = us13.gedcomParse("project02_gedcom.ged")
        indiListData.sort()
        famListData.sort()
        outputList = us13.SiblingsSpacing(indiListData, famListData)
        lenOutput = len(outputList);
        self.assertFalse((lenOutput>0), "Should be False")
        
    def test_siblings_spacing_4(self):
        indiListData, famListData = us13.gedcomParse("project02_gedcom.ged")
        indiListData.sort()
        famListData.sort()
        outputList = us13.SiblingsSpacing(indiListData, famListData)
        lenOutput = len(outputList);
        self.assertIs(lenOutput, 0, "Should be 0")
        
class TestAges(unittest.TestCase):
    
    def test_age_1(self):
        list_individual = us27.gedcomParse("project02_gedcom.ged")
        list_individual.sort()
        outputList = us27.individualAges(list_individual)
        lenOutput = len(outputList);
        self.assertNotEqual(lenOutput, 0, "Should not be 0")
        
    def test_age_2(self):
        list_individual = us27.gedcomParse("project02_gedcom.ged")
        list_individual.sort()
        outputList = us27.individualAges(list_individual)
        lenOutput = len(outputList);
        self.assertTrue((lenOutput==0), "Should be True")
        
    def test_age_3(self):
        list_individual = us27.gedcomParse("project02_gedcom.ged")
        list_individual.sort()
        outputList = us27.individualAges(list_individual)
        lenOutput = len(outputList);
        self.assertFalse((lenOutput>0), "Should be False")
        
    def test_age_4(self):
        list_individual = us27.gedcomParse("project02_gedcom.ged")
        list_individual.sort()
        outputList = us27.individualAges(list_individual)
        lenOutput = len(outputList);
        self.assertIs(lenOutput, 0, "Should be 0")