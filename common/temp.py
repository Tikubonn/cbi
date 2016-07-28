
class temp:

    def init (self):
        self.source = ""
        self.result = ""

    def addtemp (self, source):
        self.source += source

    def add (self, source):
        self.result += source

    def gettemp (self):
        source = self.source
        self.source = ""
        return source

    def get (self):
        return self.result
        
    __init__ = init
