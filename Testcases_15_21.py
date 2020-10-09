import unittest
import user_story15, user_story21

check=( user_story21.getGenderID is None) 

class TestStringMethods(unittest.TestCase):

    def test1(self):
        siblings = 15
        if (self.assertTrue(siblings)):
            print(True)
        else:
            print(False)

    def test2(self):
        siblings = 20
        if (self.assertEqual(siblings, 20)):
            print(True)
        else:
            print(False)
    
    def test3(self):
        self.assertIsNotNone(user_story21.getGenderID, True)

    def test4(self):
        self.assertTrue(user_story21.getGenderID)

    def test5(self):
        self.assertFalse(check)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
