
import os

class pathname:

    pathnames = None

    def init (self):
        self.pathnames = [set()]

    def push (self):
        self.pathnames.append(set())

    def pop (self):
        return self.pathnames.pop()

    def add (self, pathname):
        self.pathnames[-1].add(pathname)

    def get (self):
        pathnames = set()
        for pathname in self.pathnames:
            for path in pathname:
                pathnames.add(path)
        return pathnames

    def find (self, filename):
        if os.path.isabs(filename):
            return filename
        for pathname in self.get():
            pathname = os.path.join(pathname, filename)
            pathname = os.path.abspath(pathname)
            if os.path.exists(pathname):
                return pathname

    __init__ = init

class pushpathname:

    def init (self, pathname):
        self.pathname = pathname

    def enter (self):
        self.pathname.push()

    def exit (self, exception, exceptionvalue, trace):
        self.pathname.pop()
        return False

    __init__ = init
    __enter__ = enter
    __exit__ = exit
