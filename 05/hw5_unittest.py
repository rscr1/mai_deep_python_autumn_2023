import unittest

from hw5_lru_cache import LRUCache


class Test(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)

    def test_1(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.assertIs(self.cache.get('k3'), None)

    def test_2(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.assertEqual(self.cache.get('k2'), 'val2')

    def test_3(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.assertEqual(self.cache.get('k1'), 'val1')

    def test_4(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k3", "val3")
        self.assertEqual(self.cache.get('k3'), 'val3')

    def test_5(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k3", "val3")
        self.assertIs(self.cache.get('k1'), None)

    def test_6(self):
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")
        self.cache.set("k3", "val3")
        self.assertEqual(self.cache.get('k2'), 'val2')

if __name__ == "__main__":
    unittest.main()
