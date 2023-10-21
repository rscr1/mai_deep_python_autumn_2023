import unittest

from hw3_class import CustomList


class Test(unittest.TestCase):
    def setUp(self):
        self.list_1 = CustomList([5, 1, 3, 7])
        self.list_2 = CustomList([1, 2, 7])
        self.list_3 = CustomList([6, 3, 10, 7])
        self.list_4 = CustomList([1])
        self.list_5 = [2, 5]
        self.list_6 = CustomList([3, 5])
        self.list_7 = CustomList([4, -1, -4, 7])
        self.list_8 = CustomList([-1, -5])
        self.list_9 = CustomList([1, 5])

    def test_sum_1(self):
        self.assertEqual(self.list_1 + self.list_2, self.list_3)

    def test_sum_2(self):
        self.assertEqual(self.list_4 + self.list_5, self.list_6)

    def test_sum_3(self):
        self.assertEqual(self.list_5 + self.list_4, self.list_6)

    def test_dif_1(self):
        self.assertEqual(self.list_1 - self.list_2, self.list_7)

    def test_dif_2(self):
        self.assertEqual(self.list_4 - self.list_5, self.list_8)

    def test_dif_3(self):
        self.assertEqual(self.list_5 - self.list_4, self.list_9)

    def test_equal_1(self):
        self.assertEqual(self.list_1 == self.list_2, False)

    def test_not_equal_1(self):
        self.assertEqual(self.list_2 != self.list_4, True)

    def test_more_1(self):
        self.assertEqual(self.list_1 <= self.list_3, True)

    def test_more_2(self):
        self.assertEqual(self.list_1 <= self.list_1, True)

    def test_less_1(self):
        self.assertEqual(self.list_1 >= self.list_3, False)

    def test_str_1(self):
        self.assertEqual(self.list_1.__str__(), '[5, 1, 3, 7] sum=16')

if __name__ == "main":
    unittest.main()
