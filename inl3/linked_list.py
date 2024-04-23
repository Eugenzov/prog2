""" linked_list.py

Student:
Reviewed by:
Date reviewed:
"""


from os import remove
from platform import node
from queue import Empty
import re


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):       # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):      # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):             # Optional
        count = 0
        current = self.first
        while current != None:
            count += 1
            current = current.succ
        return count
            

    def mean(self):               # Optional
        pass

    def remove_last(self):        # Optional
        pass

    def remove(self, x):          # Compulsory
        current = self.first
        if current == None:
            return False
        if current.data == x:
            self.first = current.succ
            return True
        while current.succ:
            if current.succ.data == x:
                current.succ = current.succ.succ
                return True
            current = current.succ

    def count(self, x):           # Optional
        pass

    def to_list(self):            # Compulsory
        def _to_list(node):
            if node is None:
                return []
            return [node.data] + _to_list(node.succ)
        
        return _to_list(self.first)
    def remove_all(self, x):      # Compulsory
        def _remove_all(node):
            if node is None:
                return 0
            
            if node.data == x:
                self.first = node.succ
                if node.succ:
                    return 1 + _remove_all(node.succ)
                return 1
            
            if node.succ.succ is None:
                if node.succ.data == x:
                    node.succ = None
                    return 1
                return 0
            
            if node.succ.data == x:
                node.succ = node.succ.succ
                return 1 + _remove_all(node.succ)
            return _remove_all(node.succ)
            
        return _remove_all(self.first)
        

    def __str__(self):            # Compulsary
        pass

    def copy(self):               # Compulsary
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    ''' Complexity for this implementation: 

    '''

    def copy(self):               # Compulsary
        pass                      # Should be more efficient
    ''' Complexity for this implementation:

    '''

    def __getitem__(self, ind):   # Optional
        pass


class Person:                     # Compulsory
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"


def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    # Test code:


if __name__ == '__main__':
    main()
