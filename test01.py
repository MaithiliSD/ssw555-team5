import unittest
from US08 import us08,husbadage, wifeage
from US10 import us10



class UserStoryTest(unittest.TestCase):
# Test Cases for US08
    def test1(self):
        self.assertEqual(us08(), True)
    def test2(self):
        self.assertNotEqual(us08(), False)
    def test3(self):
        self.assertTrue(us08())
    def test4(self):
        self.assertIsNotNone(us08(), True)
    def test5(self):
        self.assertIsNot(us08(), False)

# Test Cases for US10
    def test6(self):
        self.assertEqualus10(), True)
    def test7(self):
        self.assertNotEqual(us10(), False)
    def test8(self):
        self.assertTrue(us10())
    def test9(self):
        self.assertIsNotNone(us10(), True)
    def test10(self):
        self.assertIsNot(us10(), False)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)