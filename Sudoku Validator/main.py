from math import sqrt,floor

class Sudoku(object):
    def __init__(self, data):
        self.data = data
    
    def is_valid(self):
        
        # Because python interprets bool as int(1) and int(0) but is distinguished by type()
        if not all(type(x)== int for l in self.data for x in l):
            return False
        
        # The size of rows must be equal to the size of columns
        if not all((len(x) == len(self.data) for x in self.data)):
            return False
        
        size = len(self.data) # Thanks to the last check
        
        correct_model = {i for i in range(1,size + 1)}
        
        # We check if every rows contain unique and valid numbers (through the set)
        if not all((correct_model == set(x) for x in self.data)):
            return False
        
        # We check if every columns contain unique and valid numbers (through the set)
        columns = ({v[i] for v in self.data} for i in range(size))
        if not all((correct_model == x for x in columns)):
            return False
        
        # At this point we only need to check every boxes
        # Since Sudoku is reprented in a square, the size of a little box is an integer == sqrt(size)
        # considering size >= 4
        
        size_box = floor(sqrt(size)) # size is obviously > 0
        boxes = []
        
        for i in range(size_box):
            curr = []
            for (c,v) in enumerate(self.data):
                if c % size_box==0:
                    boxes.append(curr)
                    curr.clear()
                for k in range(size_box):
                    curr.append(v[k+size_box*i])
        
        if not all((correct_model == set(x) for x in boxes)):
            return False
        
        # Else, everything is good
        return True
