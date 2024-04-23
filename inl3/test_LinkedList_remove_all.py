"""
Unittests LinkedList's remove_all
"""

import unittest

from linked_list import *


class Test(unittest.TestCase): 
 
    def test_remove_all(self):
        print("\nTests LinkedList's remove_all")
        lst = LinkedList()
        for x in [1, 1, 2, 6, 6, 8, 9, 9]:
            lst.insert(x)
        self.assertEqual(lst.remove_all(5),0)
        self.assertEqual(lst.remove_all(9),2)
        self.assertEqual(lst.remove_all(9),0)
        self.assertEqual(lst.remove_all(1),2)
        self.assertEqual(lst.remove_all(2),1)
        self.assertEqual(lst.remove_all(2),0)
        self.assertEqual(lst.remove_all(8),1)
        self.assertEqual(lst.remove_all(6),2)
        self.assertEqual(lst.remove_all(6),0)
        self.assertEqual(lst.first, None)

    
    

if __name__ == "__main__":
    unittest.main()
