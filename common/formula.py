
import read
import stream
import string

class oprand:

    order = 0

    def evaluate (self, sequence):
        pass

class oprandAdd (oprand):

    order = 3

    def evaluate (self, sequence):
        a = sequence.pop() if sequence else 0
        b = sequence.pop() if sequence else 0
        sequence.append(b + a)

class oprandMinus (oprand):

    order = 9

    def evaluate (self, sequence):
        a = sequence.pop()
        sequence.append(-a)

class oprandMul (oprand):

    order = 4

    def evaluate (self, sequence):
        a = sequence.pop()
        b = sequence.pop()
        sequence.append(b * a)

class oprandDiv (oprand):

    order = 4

    def evaluate (self, sequence):
        a = sequence.pop()
        b = sequence.pop()
        sequence.append(b / a)

class oprandMod (oprand):

    order = 4

    def evaluate (self, sequence):
        a = sequence.pop()
        b = sequence.pop()
        sequence.append(b % a)

class oprandEqual (oprand):

    order = 0

    def evaulate (self, sequence):
        a = sequence.pop()
        b = sequence.pop()
        sequence.append(1 if a == b else 0)

class oprandEqualNot (oprand):

    order = 0

    def evaluate (self, sequence):
        a = sequence.pop()
        b = sequence.pop()
        sequence.append(1 if a != b else 0)
        
class oprandNot (oprand):

    order = 0

    def evaulate (self, sequence):
        a = sequence.pop()
        sequence.append(1 if not a else 0)

class oprandOr (oprand):

    order = 0

    def evaluate (self, sequence):
        a = sequence.pop()
        b = sequence.pop()
        sequence.append(1 if a or b else 0)
        
class oprandAnd (oprand):

    order = 0

    def evaulate (self, sequence):
        a = sequence.pop()
        b = sequence.pop()
        sequence.append(1 if a and b else 0)

class oprandOpenBrace (oprand):
    
    pass

class oprandCloseBrace (oprand):
    
    pass


# oprands for parsing 

oprands = {}
oprands.setdefault("+", oprandAdd())
oprands.setdefault("*", oprandMul())
oprands.setdefault("/", oprandDiv())
oprands.setdefault("%", oprandMod())
oprands.setdefault("==", oprandEqual())
oprands.setdefault("!=", oprandEqualNot())
oprands.setdefault("&&", oprandAnd())
oprands.setdefault("||", oprandOr())
oprands.setdefault("!", oprandNot())

# parse methods

def parsetoken (sequence, streamin):
    read.readspace(streamin)
    if not streamin.look():
        return sequence
    elif streamin.look() in string.digits:
        sequence.append(int(read.readint(streamin)))
    elif streamin.look() == "-":
        streamin.get()
        parseminus(sequence, streamin)
    elif streamin.look() == "(":
        streamin.get()
        sequence.append(oprandOpenBrace())
        parsebrace(sequence, streamin)
    elif streamin.look() == ")":
        raise Exception("independent close brace.")
    else:
        oprand = read.readfornot(
            string.punctuation +
            string.ascii_letters,
            streamin)
        if not oprand in oprands:
            raise Exception("oprand '%s' was not found." % oprand)
        sequence.append(oprands.get(oprand))
    return sequence
        
def parseminus (sequence, streamin):
    read.readspace(streamin)
    should = (
        bool(sequence) and
        isinstance(sequence[-1], int) or
        isinstance(sequence[-1], oprandCloseBrace))
    if should: sequence.append(oprandAdd())
    sequence.append(oprandOpenBrace())
    sequence.append(oprandMinus())
    parsetoken(sequence, streamin)
    sequence.append(oprandCloseBrace())
    return sequence

def parsebrace (sequence, streamin):
    while streamin.look():
        read.readspace(streamin)
        if streamin.look() == ")":
            streamin.get()
            sequence.append(oprandCloseBrace())
            return sequence
        parsetoken(sequence, streamin)
    raise Exception("missing close brace.")

def parsetokens (streamin):
    sequence = []
    while streamin.look():
        parsetoken(sequence, streamin)
    return sequence

# parsing fomula

def parsefomula (tokens):
    stack = []
    result = []
    while tokens:
        token = tokens.pop(0)
        if isinstance(token, int):
            result.append(token)
        elif isinstance(token, oprandOpenBrace):
            result = parsefomula(tokens) + result
        elif isinstance(token, oprandCloseBrace):
            break
        else:
            stack.append(token)
            while len(stack) >= 2:
                if stack[-2].order > stack[-1].order:
                    result.append(stack.pop(-2))
                    continue
                break
    return result + stack

# evaluate fomula

def evaluatefomula (tokens):
    stack = []
    for token in tokens:
        if isinstance(token, int):
            stack.append(token)
        else: token.evaluate(stack)
    if len(stack) > 1:
        raise Exception("stack has many values in evalfomula().")
    return stack[0]

# alias of procedure

def evaluate (source):
    return evaluatefomula(parsefomula(parsetokens(stream.stream(source))))
