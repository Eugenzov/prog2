"""
Unittest for LinkedList's count
"""

import unittest

from linked_list import *


class Test(unittest.TestCase):

    def test_count(self):
        print("\nTests LinkedList's count")
        lst = LinkedList()
        self.assertEqual(lst.count(1), 0, msg='Wrong for empty lists')
        for x in [1, 1, 2, 6, 6]:
            lst.insert(x)
        self.assertEqual(lst.count(1), 2)
        self.assertEqual(lst.count(1), 2, msg='count modifies the list')
        self.assertEqual(lst.count(2), 1)
        self.assertEqual(lst.count(3), 0)
        self.assertEqual(lst.count(6), 2)
        self.assertEqual(lst.count(6), 2, msg='count modifies the list')
        self.assertEqual(lst.count(7), 0)


if __name__ == "__main__":
    unittest.main()
