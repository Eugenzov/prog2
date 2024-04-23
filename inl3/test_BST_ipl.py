# https://docs.python.org/3/library/unittest.html
"""
Unittests for the binary search tree methods

"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):

    def test_ipl(self):
        print('\nTests ipl')
        bst = BST()
        self.assertEqual(bst.ipl(), 0)
        bst.insert(5)
        self.assertEqual(bst.ipl(), 1)
        bst.insert(8)
        self.assertEqual(bst.ipl(), 3)
        bst.insert(9)
        self.assertEqual(bst.ipl(), 6)
        bst.insert(3)
        self.assertEqual(bst.ipl(), 8)
        bst.insert(1)
        self.assertEqual(bst.ipl(), 11)
        bst.insert(10)
        self.assertEqual(bst.ipl(), 15)
        bst.insert(2)
        self.assertEqual(bst.ipl(), 19)
        bst.insert(4)
        self.assertEqual(bst.ipl(), 22)


if __name__ == "__main__":
    unittest.main()
