import unittest
import user_stories12

check=( user_stories12.getDeathDate is " ") 

class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertNotEqual(user_stories12.getDeathDate, 1)

    def test2(self):
        self.assertIsNot(user_stories12.getDeathDate, False)
    
    def test3(self):
        self.assertIsNotNone(user_stories12.getDeathDate, True)

    def test4(self):
        self.assertTrue(user_stories12.getDeathDate)

    def test5(self):
        self.assertFalse(check)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
