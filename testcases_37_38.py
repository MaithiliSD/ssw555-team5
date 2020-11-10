mport unittest
from us37 import us37
from us38 import us38

class UserStoryTest(unittest.TestCase):
     def test_us37(self):
        f = open("test.txt", "a")
        value = us37(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

    def test_us38(self):
        f = open("test.txt", "a")
        value = us38(self.d[0], self.d[1], f)
        f.close()
        self.assertFalse(value)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)

