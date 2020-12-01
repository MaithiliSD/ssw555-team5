import unittest
from us33 import us33



class UserStoryTest(unittest.TestCase):
     def test_us33(self):
        f = open("test.txt", "a")
        value = us33(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
