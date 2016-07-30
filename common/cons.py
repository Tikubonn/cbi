
class cons:

    car = None
    cdr = None

    def init (self, car = None, cdr = None):
        self.car = car
        self.cdr = cdr

    def iter (self):
        return consiter(self)

    def reversed (self):
        return consreversed(self)

    def repr (self):
        return "(%s . %s)" % (self.car, self.cdr)

    def list (self):
        return [element for element in self]

    def nth (self, index):
        while self:
            if index == 0:
                return self.car
            self = self.cdr

    def setnth (self, index, value):
        while self:
            if index == 0:
                self.car = value
                return value
            self = self.cdr

    def contents (self, element):
        for some in self:
            if some == element:
                return True

    def len (self):
        count = 0
        while self:
            count += 1
            self = self.cdr
        return count

    def map (self, func):
        consn = None
        while self:
            consn = cons(func(self.car), consn)
            self = self.cdr
        return consn.nreverse()

    def filter (self, func):
        consn = None
        while self:
            if func(self.car):
                consn = cons(self.car, consn)
            self = self.cdr
        return consn.nreverse()
        
    def reverse (self):
        consn = None
        while self:
            consn = cons(self.car, consn)
            self = self.cdr
        return consn

    def nreverse (self):
        consn = None
        consnext = None
        while self:
            consnext = self.cdr
            self.cdr = consn
            consn = self
            self = consnext
        return consn

    __init__ = init
    __iter__ = iter
    __repr__ = repr
    __reversed__ = reversed
    __getitem__ = nth
    __setitem__ = setnth

class consiter:

    cons = None

    def init (self, cons):
        self.cons = cons

    def next (self):
        if not self.cons:
            raise StopIteration
        element = self.cons.car
        self.cons = self.cons.cdr
        return element

    __init__ = init
    __next__ = next


class consreversed (consiter):

    def init (self, cons):
        self.cons = cons.reverse()
