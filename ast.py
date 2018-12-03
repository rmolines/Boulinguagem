from symboltable import SymbolTable


class IntVal():
    def __init__(self, value):
        self.value = value
    
    def eval(self):
        return (self.value)

class FuncDec():
    def __init__(self, symbol, child):
        self.symbol = symbol
        self.child = child
    
    def eval(self):
        SymbolTable.setSymbol(self.symbol, self.child)

class IdVal():
    def __init__(self, symbol):
        self.symbol = symbol
    
    def eval(self):
        return (SymbolTable.getSymbol(self.symbol))

class Return():
    def __init__(self, child):
        self.child = child
    
    def eval(self):
        return (self.child.eval())

class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Div(BinaryOp):
    def eval(self):
        return self.left.eval() / self.right.eval()

class Mult(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Is_Less(BinaryOp):
    def eval(self):
        return self.left.eval() < self.right.eval()

class Is_Greater(BinaryOp):
    def eval(self):
        return self.left.eval() > self.right.eval()

class Is_Equal(BinaryOp):
    def eval(self):
        return self.left.eval() == self.right.eval()

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print(self.value.eval())

class While():
    def __init__(self, condition, child):
        self.condition = condition
        self.child = child

    def eval(self):
        while(self.condition.eval()):
            self.child.eval()

class If_Else():
    def __init__(self, condition, childTrue, childFalse):
        self.condition = condition
        self.childTrue = childTrue
        self.childFalse = childFalse

    def eval(self):
        if(self.condition.eval()):
            self.childTrue.eval()
        else:
            if (self.childFalse != None):
                self.childFalse.eval()

class Scanf():
    def __init__(self, id_):
        self.id_ = id_

    def eval(self):
        SymbolTable.setSymbol(self.id_, int(input()))


class Equal(BinaryOp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        SymbolTable.setSymbol(self.left, self.right.eval())

class Commands():
    def __init__(self, children):
        self.children = children

    def eval(self):
        for i in self.children:
            if (isinstance(i, Return)):
                return i.eval()
            
            i.eval()

    def pushChild(self, child):
        self.children.append(child)
class Program():
    def __init__(self, children):
        self.children = children
    
    def eval(self):
        for i in self.children:
            i.eval()
    
    def pushChild(self, child):
        self.children.append(child)

class FuncCall():
    def __init__(self, symbol):
        self.symbol = symbol
    
    def eval(self):
        func = SymbolTable.getSymbol(self.symbol)
        
        return func.eval()

class Main():
    def __init__(self, child):
        self.child = child
        self.main = FuncCall('main')
    
    def eval(self):
        self.child.eval()
        self.main.eval()



