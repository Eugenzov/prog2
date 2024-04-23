""" linked_list.py

Student: Tobias Karlsson    
Mail: tobias.karlsson@student.uu.se
Reviewed by:Andreas Pihl 
Date reviewed:20230925
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
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
        len  = 0 
        f = self.first

        while f:
            len += 1
            f = f.succ
        return len

    def sum(self):
        sum = 0
        f = self.first
        while f:
            sum += f.data
            f = f.succ
        return sum

    def mean(self):               # Optional

        mean = self.sum()/self.length()
        return mean
        
    def remove_last(self):        # Optional

        f = self.first

        if f == None:
            raise ValueError("No value to return")

        if f.succ == None:
            self.first = None
            return f.data

        while f.succ.succ:
            f = f.succ
        result = f.succ.data
        f.succ = None
        return result

    def remove(self, x):          # Compulsory
        f = self.first

        if f == None: #checks if list is empty
            return False 
        
        if f.data == x:
            self.first = f.succ
            return True
            
        while f.succ:
            if f.succ.data == x:
                f.succ = f.succ.succ 
                return True
            f = f.succ
        return False

    def count(self, x):           # Optional
        def _count(f,x):
            if not f:
                return 0            
            if f.data == x:
                return 1 + _count(f.succ,x)
            return _count(f.succ,x)
        return _count(self.first,x)


    def to_list(self):            # Compulsory
        def _to_list(f):
            while f:
                return [f.data] + _to_list(f.succ)
            return []
        return _to_list(self.first)
        

    def remove_all(self, x):      # Compulsory
        def _remove_all(f,x):
            if not f:
                return 0

            if f.data == x: 

                self.first = f.succ
                if f.succ: 

                    return 1 + _remove_all(f.succ, x)
                return 1

            if not f.succ.succ: 

                if f.succ.data == x:

                    f.succ = None
                    return 1
                return 0           

            if f.succ.data == x: 

                f.succ = f.succ.succ
                return 1 + _remove_all(f, x)
            
            return _remove_all(f.succ, x) 
     
        return _remove_all(self.first,x)

    def __str__(self):            # Compulsary
        s = "("
        index = 0
        for i in self:

            s += str(i)
            if index < self.length() - 1:
                s += ", "
            index += 1
        return s + ")"

    def copy(self):               # Compulsary
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result

    
    def copy(self):               # Compulsary  # Should be more efficient
        
        copy = LinkedList() 
        lst = list(self)    
        t = None           
        
        lst.reverse()       
        for i in lst:               
            t = self.Node(i,t)

        copy.first = t        
        return copy     
          

    def __getitem__(self, ind):   # Compulsory
        for i,j in enumerate(self):
            if i == ind:
                return j
        raise IndexError("utanf;r listan")


class Person:                     # Compulsory to complete
    def __init__(self, name, pnr):
        self.name = name
        self.pnr = pnr

    def __str__(self):
        return f"{self.name}:{self.pnr}"
    
    def __it__(self, next):
        return self.pnr < next.pnr

    def __le__(self, next):
        return self.pnr <= next.pnr
    
    def __gt__(self, other):
        return self.pnr > other.pnr

    def __ge__(self, other):
        return self.prn >= other.pnr

    def __eq__(self, next):
        return self.pnr == next.pnr



def main():
    lst = LinkedList()
    for x in [1, 1, 1, 3, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()
    print(lst.remove_all(3))
    lst.print()
    # Test code:


if __name__ == '__main__':
    main()
