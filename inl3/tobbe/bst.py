""" bst.py

Student: Tobias Karlsson    
Mail: tobias.karlsson@student.uu.se
Reviewed by:Andreas Pihl 
Date reviewed:20230925
"""


from linked_list import LinkedList
import random
import math


class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Dicussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

    def height(self):                             # Compulsory
        def _height (n):
            if n:
                return 1 + max(_height(n.right), _height(n.left))
            else:
                return 0
            
        return _height(self.root)

    

    def __str__(self):                            # Compulsory
        string = "<"
        index = 0 
        for i in self:
            string += str(i)
            if index != self.size() - 1:
                string += ", " 
            index += 1
        return string + ">"

    def to_list(self):                            # Compulsory
        res = []
        for i in self.__iter__():
            res.append(i)
        return res


    def to_LinkedList(self):                      # Compulsory
        res = []
        for i in self.__iter__():
            res.append(i)
        
        LL = LinkedList()
        for x in res:
            LL.insert(x)
        return LL

    
    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      # Compulsory
        if r is None:
            return None
        elif k < r.key:
            r.left = self._remove(r.left, k)

        elif k > r.key:
            r.right = self._remove(r.right, k)
            # r.right =  right subtree with k removed
        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:  # This is the tricky case.

                min = r.right
                
                while min.left:
                    min = min.left
                r.key = min.key
                r.right = self._remove(r.right,min.key)
            
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
        return r  # Remember this! It applies to some of the cases above
    def ipl(self):
        return self._ipl(self.root)
    
    def _ipl(self,node, n = 1 ):
        if node is None:
            return 0
        else:
            left_ipl = self._ipl(node.left, n + 1)
            right_ipl = self._ipl(node.right, n + 1)
            return n + left_ipl + right_ipl


def random_tree(n):                               # Useful
    root = BST()
    for i in range(n):
        data = random.random()
        root.insert(data)
    return root
        
def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")

    print('\tSize', '\t Theory','\tObesrved height', '\t IPL',)
    size = 100
    for i in range(1,10):
        size = size * 2  # set steps
        rand_bst = random_tree(size)
        
        height = rand_bst.height()
        average_h = rand_bst.ipl()/size  
              
        print('\t', size, '\t', "{:.3f}".format(1.39*math.log2(size)),  '\t', height, '\t\t\t', "{:.3f}".format(average_h), )


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? Y
2. computing height? N
3. contains? Y
4. insert? N
5. remove? N



Results for ipl of random trees
===============================
Size     Theory         Obesrved height          IPL
200     10.625          20                      10.355
400     12.015          17                      9.820
800     13.405          18                      10.739
1600    14.795          22                      12.594
3200    16.185          24                      13.819
6400    17.575          28                      15.598
12800   18.965          37                      16.733
25600   20.355          33                      18.519
51200   21.745          38                      21.242





"""
