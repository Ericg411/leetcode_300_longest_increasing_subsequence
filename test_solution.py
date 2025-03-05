import unittest
from solution import Solution

class TestLengthOfLIS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_length_of_lis_1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)

    def test_length_of_lis_2(self):
        nums = [0, 1, 0, 3, 2, 3]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)

    def test_length_of_lis_3(self):
        nums = [7, 7, 7, 7, 7, 7, 7]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

    def test_length_of_lis_4(self):
        nums = [4, 10, 4, 3, 8, 9]
        self.assertEqual(self.solution.lengthOfLIS(nums), 3)

    def test_length_of_lis_5(self):
        nums = []
        self.assertEqual(self.solution.lengthOfLIS(nums), 0)

    def test_length_of_lis_6(self):
        nums = [2, 2, 2, 2, 2]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

    def test_length_of_lis_7(self):
        nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
        self.assertEqual(self.solution.lengthOfLIS(nums), 6)

if __name__ == '__main__':
    unittest.main()
