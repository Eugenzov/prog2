"""
Unittests for the binary search tree methods
"""

import unittest

from bst import *
from linked_list import *


class Test(unittest.TestCase):

    def test_remove(self):
        lst = LinkedList()
        self.assertEqual(lst.remove(1), 0, msg="Cant't handle empty lists")
        lst.insert(3)
        self.assertEqual(lst.remove(3), 1)
        lst.insert(3)
        lst.insert(1)
        lst.insert(2)
        lst.insert(4)
        lst.remove(4)
        self.assertEqual(lst.length(), 3, msg='Destroys self')
        #lst.insert(2)


if __name__ == "__main__":
    unittest.main()
