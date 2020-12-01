import unittest
import user_story43

check=( user_story43.aunts_uncle is None) 

class TestStringMethods(unittest.TestCase):

    def test1(self):
        self.assertGreaterEqual(5, 1)
    
    def test2(self):
        self.assertIsNotNone(user_story43.get_indi_name, True)

    def test4(self):
        self.assertFalse(check)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
