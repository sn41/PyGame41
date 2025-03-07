import unittest

def sum(a, b):
    return a + b


class TestSum(unittest.TestCase):
    def test_sum(self):
        # self.assertEqual(sum(1, 2), 3)
        assert sum(1, 2) == 4, "The function should return 3"
