import unittest
import user_story05, user_story06

check=( user_story06.deathDate is None) 

class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertNotEqual(user_story05.deathDate, 1)

    def test2(self):
        self.assertIsNot(user_story05.deathDate, False)
    
    def test3(self):
        self.assertIsNotNone(user_story06.deathDate, True)

    def test4(self):
        self.assertTrue(user_story06.deathDate)

    def test5(self):
        self.assertFalse(check)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
