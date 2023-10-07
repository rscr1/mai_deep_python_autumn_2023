import unittest
from unittest.mock import Mock
from hw2_parser import parse_json

class Test(unittest.TestCase):
    def setUp(self):
        self.test_1 = '{"key1": "Word1 word2", "key2": "word2 word3"}'
        self.test_2 = '{}'
        self.test_3 = '{"key1": "", "key":""}'
        self.test_4 = '{"1": "Word1 word2"}'
        self.test_5 = '{"key1": "w", "key2": "w", "key3": "w", "key4": "w"}'
        self.mock = Mock()
        self.parse_json = parse_json

    def test_parsing_1(self):
        self.parse_json(self.test_1, ["key1", "key2"], ["word2"], self.mock)
        self.assertEqual(self.mock.call_count, 2)

    def test_parsing_2(self):
        self.parse_json(self.test_2, ["key1", "key2"], ["w1", "a1"], self.mock)
        self.assertEqual(self.mock.call_count, 0)

    def test_parsing_3(self):
        self.parse_json(self.test_3, ["key1","key2"], ["vk"], self.mock)
        self.assertEqual(self.mock.call_count, 0)

    def test_parsing_4(self):
        self.parse_json(self.test_4, ["1"], ["Word1"], self.mock)
        self.assertEqual(self.mock.call_count, 1)

    def test_parsing_5(self):
        self.parse_json(self.test_5, ["key1", "key2", "key3", "key4"], ["w"], self.mock)
        self.assertEqual(self.mock.call_count, 4)

unittest.main()