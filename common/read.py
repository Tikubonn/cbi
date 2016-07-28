
import string
import stream
import oprand

wordable = string.ascii_letters + string.digits

def readif (func, streamin):
    content = ""
    while streamin.look() and func(streamin.look()):
        content += streamin.get()
    return content

def readfor (union, streamin):
    return readif((lambda char: not char in union), streamin)

def readfornot (union, streamin):
    return readif((lambda char: char in union), streamin)

def readrest (streamin):
    content = ""
    while streamin.look():
        content += streamin.get()
    return content

def readline (streamin):
    return readfor("\n", streamin)

def readat (streamin):
    return readfor("@", streamin)

def readconnector (streamin):
    return readfornot("#", streamin)

def readint (streamin):
    return readfornot(string.digits, streamin)

def readpunctuation (streamin):
    return readfornot(string.punctuation, streamin)

def readword (streamin):
    return readfornot(wordable, streamin)

def readunword (streamin):
    return readfor(wordable, streamin)

def readspace (streamin):
    return readfornot(string.whitespace, streamin)

def readunspace (streamin):
    return readfor(string.whitespace, streamin)

def readoprand (streamin):
    content = readat(streamin)
    streamin.get()
    oprand = readword(streamin)
    return content, oprand

# def readtooprands (union, streamin):
#     before = ""
#     while streamin.look():
#         content, oprand = readoprand(streamin)
#         if oprand in union:
#             return content, oprand
#         if oprand in oprands:
#             op = oprands.get(oprand)()
#             op.parse(streamin)
#             before += content
#             before += op.build()
#             continue
#         raise readerror('you tried undefined oprand of "%s" in readtooprands().' % oprand)

def readstring (streamin):
    if not streamin.look() in "\"'":
        raise readerror("it is not string in readstring().")
    quote = streamin.get()
    content = quote
    while streamin.look() and streamin.look() != quote:
        char = streamin.get()
        if char == "\\":
            content += escapechar(streamin.get())
            continue
        content += char
    content += streamin.get()
    return content

def readlist (streamin):
    if streamin.look() != "(":
        raise readerror("it is not tuple in readlist().")
    sequence = []
    streamin.get()
    while streamin.look():
        element = readlistelement(streamin)
        sequence.append(element)
        if streamin.get() == ")":
            break
    return sequence

def readlistelement (streamin):
    content = ""
    while streamin.look() and not streamin.look() in "),":
        if streamin.look() in "\"'":
            content += readstring(streamin)
            continue
        if streamin.look() in "(":
            content += "(%s)" % ",".join(readlist(streamin))
        content += streamin.get()
    return content.strip(string.whitespace)

class readerror (Exception):
    pass
