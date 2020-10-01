import unittest
from projecthw4 import US07


class UserStoryTest(unittest.TestCase):

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




if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)