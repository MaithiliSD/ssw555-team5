import unittest
import us31
import us32

class TestUserStoriestwo(unittest.TestCase):
        
    def test_living_single_1(self):
        list1 = []
        self.assertTrue(us31.listLivingSingle is not list1)
        
    def test_multiple_births_1(self):
        list1 = []
        self.assertTrue(us32.listOfMultipleBirths is not list1)

unittest.main()