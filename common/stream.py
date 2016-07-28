
class streambase:

    def get (self):
        pass

    def look (self):
        pass

class stream (streambase):

    def init (self, source):
        self.source = list(source)

    def get (self):
        return self.source.pop(0) if self.source else None

    def look (self):
        return self.source[0] if self.source else None

    __init__ = init

class filestream (streambase):

    def init (self, fin, size = 1024):
        self.fin = fin
        self.size = size
        self.streamin = None

    def load (self):
        if not self.fin:
            return False
        source = self.fin.read()
        if not source:
            self.fin = None
            return False
        self.streamin = stream(source)
        return True

    def get (self):
        while True:
            element = self.streamin and self.streamin.get()
            if not element and self.load():
                continue
            break
        return element

    def look (self):
        while True:
            element = self.streamin and self.streamin.look()
            if not element and self.load():
                continue
            break
        return element

    __init__ = init
