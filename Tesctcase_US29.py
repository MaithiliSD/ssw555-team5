import unittest
import user_story29

check=( user_story29.living_married is None) 

class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertGreaterEqual(5, 1)
    
    def test2(self):
        self.assertIsNotNone(user_story29.get_indi_name, True)

    def test4(self):
        self.assertFalse(check)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
