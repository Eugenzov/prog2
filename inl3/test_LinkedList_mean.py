# https://docs.python.org/3/library/unittest.html
"""
Unittest for LinkedList's mean
"""

import unittest

from linked_list import *


class Test(unittest.TestCase):

    def test_mean(self):
        print("\nTests LinkedList's mean")
        lst = LinkedList()
        for x in [3, 1, 2, 6]:
            lst.insert(x)
        self.assertEqual(lst.mean(), 3)
        self.assertEqual(lst.mean(), 3, msg="mean modifies the list")


if __name__ == "__main__":
    unittest.main()
