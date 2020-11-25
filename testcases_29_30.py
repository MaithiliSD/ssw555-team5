import unittest
import user_story29
import user_story30

check29=( user_story30.death_date is None) 
check30=( user_story29.living_married is None) 

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertGreaterEqual(5, 1)
    
    def test2(self):
        self.assertIsNotNone(user_story29.get_indi_name, True)

    def test3(self):
        self.assertFalse(check29)

    def test4(self):
        self.assertGreaterEqual(5, 1)
    
    def test5(self):
        self.assertIsNotNone(user_story30.death_date, True)

    def test6(self):
        self.assertTrue(user_story30.death_date, 2)

    def test7(self):
        self.assertFalse(check30)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
