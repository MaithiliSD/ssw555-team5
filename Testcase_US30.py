import unittest
import user_story30

check=( user_story30.death_date is None) 

class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertGreaterEqual(5, 1)
    
    def test2(self):
        self.assertIsNotNone(user_story30.death_date, True)

    def test3(self):
        self.assertTrue(user_story30.death_date, 2)

    def test4(self):
        self.assertFalse(check)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
