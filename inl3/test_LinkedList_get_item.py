"""
Unittest for LinkedList's __getitem__ 
"""

import unittest

from linked_list import *


class Test(unittest.TestCase):
    def test___getitem__(self):
        print('\nTests __getitem__')
        lst = LinkedList()
        for x in [1, 2, 6]:
            lst.insert(x)
        self.assertEqual(lst[0], 1)
        self.assertEqual(lst[0], 1, msg='Destroys self')
        self.assertEqual(lst[1], 2)
        self.assertEqual(lst[2], 6)
        self.assertEqual(lst[2], 6, msg='Destroys self')
        with self.assertRaises(IndexError):
            print(lst[3], 'This should not be seen')


if __name__ == "__main__":
    unittest.main()
