import unittest
from US import US07, US09


class UserStoryTest(unittest.TestCase):
# Test Cases for US07
    def test1(self):
        self.assertEqual(US07(), True)
    def test2(self):
        self.assertNotEqual(US07(), False)
    def test3(self):
        self.assertTrue(US07())
    def test4(self):
        self.assertIsNotNone(US07(), True)
    def test5(self):
        self.assertIsNot(US07(), False)

# Test Cases for US09
    def test6(self):
        self.assertEqual(US09(), True)
    def test7(self):
        self.assertNotEqual(US09(), False)
    def test8(self):
        self.assertTrue(US09())
    def test9(self):
        self.assertIsNotNone(US09(), True)
    def test10(self):
        self.assertIsNot(US09(), False)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
