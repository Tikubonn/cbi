
class scopein (dict):

    def __init__ (self, isroot = False):
        self.isroot = isroot

class scope:

    def init (self):
        self.scopes = [scopein(True)]

    def push (self):
        self.scopes.append(scopein())

    def pop (self):
        self.scopes.pop()

    def add (self, name, value):
        self.scopes[-1][name] = value

    def get (self, name):
        if name in self.scopes[-1]:
            return self.scopes[-1].get(name)
        if name in self.scopes[0]:
            return self.scopes[0].get(name)

    def contains (self, name):
        return bool(self.get(name))

    def isroot (self):
        return self.scopes[-1].isroot

    __init__ = init
    __contains__ = contains

class pushscope:

    def init (self, scope):
        self.scope = scope

    def enter (self):
        self.scope.push()

    def exit (self, exception, exceptionvalue, trace):
        self.scope.pop()
        return False

    __init__ = init
    __enter__ = enter
    __exit__ = exit
