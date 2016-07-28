
class scope:

    def init (self):
        self.scopes = [{}]

    def push (self):
        self.scopes.append({})

    def pop (self):
        self.scopes.pop()

    def add (self, name, value):
        self.scopes[-1][name] = value

    def get (self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope.get(name, None)

    def contains (self, name):
        return bool(self.get(name))

    __init__ = init
    __contains__ = contains
