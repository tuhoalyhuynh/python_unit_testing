import unittest
import tripler

class TestTripler(unittest.TestCase):

    def test_tripler(self):
        self.assertEqual(tripler.tripler([1,2,3,4,5]), [3,6,9,12,15])
        self.assertEqual(tripler.tripler([101]), [303])
        self.assertEqual(tripler.tripler([-88]), [-264])
        self.assertEqual(tripler.tripler([2, 2]), [6,6])

if __name__ == '__main__':
    unittest.main()