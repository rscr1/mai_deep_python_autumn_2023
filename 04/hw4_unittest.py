import unittest

from hw4_metaclass import CustomClass


class Test(unittest.TestCase):
    def setUp(self):
        self.inst = CustomClass()

    def test_metaclass_1(self):
        self.assertEqual(CustomClass.custom_x, 50)
    
    def test_metaclass_2(self):
        self.assertFalse(CustomClass.x)
    
    def test_metaclass_4(self):
        self.assertEqual(self.inst.custom_x, 50)

    def test_metaclass_5(self):
        self.assertEqual(self.inst.custom_val, 99)

    def test_metaclass_6(self):
        self.assertEqual(self.inst.custom_line(), 100)

    def test_metaclass_7(self):
        self.assertEqual(str(self.inst), "Custom_by_metaclass")

    def test_metaclass_8(self):
        self.assertFalse(self.inst.x)

    def test_metaclass_9(self):
        self.assertFalse(self.inst.val)

    def test_metaclass_10(self):
        self.assertFalse(self.inst.line())

    def test_metaclass_11(self):
        self.assertFalse(self.inst.yyy)

if __name__ == "main":
    unittest.main()
