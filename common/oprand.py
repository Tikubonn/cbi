
class oprand:

    def init (self):
        self.props = {}

    def add (self, name, value):
        return self.props.setdefault(name, value)

    def get (self, name):
        return self.props.get(name, "")

    def remove (self, name):
        return self.props.pop(name)

    def parse (self, stream):
        pass

    def run (self):
        pass

    def build (self):
        pass

    __init__ = init

