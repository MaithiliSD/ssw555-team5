import unittest
from US17 import us17
from US22 import us22

class UserStoryTest(unittest.TestCase):
     def test_us17(self):
        f = open("test.txt", "a")
        value = us17(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us22(self):
        f = open("test.txt", "a")
        value = us22(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)



    
