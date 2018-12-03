from symboltable import SymbolTable


class IntVal():
    def __init__(self, value):
        self.value = value
    
    def eval(self, st):
        return (self.value)

class FuncDec():
    def __init__(self, symbol, child, args):
        self.symbol = symbol
        self.child = child
        self.args = args
    
    def eval(self, st):
        st.setSymbol(self.symbol, self)

class IdVal():
    def __init__(self, symbol):
        self.symbol = symbol
    
    def eval(self, st):
        return (st.getSymbol(self.symbol))

class Return():
    def __init__(self, child):
        self.child = child
    
    def eval(self, st):
        return (self.child.eval(st))

class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self, st):
        return self.left.eval(st) + self.right.eval(st)

class Sub(BinaryOp):
    def eval(self, st):
        return self.left.eval(st) - self.right.eval(st)

class Div(BinaryOp):
    def eval(self, st):
        return self.left.eval(st) / self.right.eval(st)

class Mult(BinaryOp):
    def eval(self, st):
        return self.left.eval(st) * self.right.eval(st)

class Is_Less(BinaryOp):
    def eval(self, st):
        return self.left.eval(st) < self.right.eval(st)

class Is_Greater(BinaryOp):
    def eval(self, st):
        return self.left.eval(st) > self.right.eval(st)

class Is_Equal(BinaryOp):
    def eval(self, st):
        return self.left.eval(st) == self.right.eval(st)

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self, st):
        print(self.value.eval(st))

class While():
    def __init__(self, condition, child):
        self.condition = condition
        self.child = child

    def eval(self, st):
        while(self.condition.eval(st)):
            self.child.eval(st)

class If_Else():
    def __init__(self, condition, childTrue, childFalse):
        self.condition = condition
        self.childTrue = childTrue
        self.childFalse = childFalse

    def eval(self, st):
        if(self.condition.eval(st)):
            self.childTrue.eval(st)
        else:
            if (self.childFalse != None):
                self.childFalse.eval(st)

class Scanf():
    def __init__(self, id_):
        self.id_ = id_

    def eval(self, st):
        st.setSymbol(self.id_, int(input()))


class Equal(BinaryOp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self, st):
        st.setSymbol(self.left, self.right.eval(st))

class Commands():
    def __init__(self, children):
        self.children = children

    def eval(self, st):
        for i in self.children:
            if (isinstance(i, Return)):
                return i.eval(st)
            
            i.eval(st)

    def pushChild(self, child):
        self.children.append(child)
class Program():
    def __init__(self, children):
        self.children = children
    
    def eval(self, st):
        for i in self.children:
            i.eval(st)
    
    def pushChild(self, child):
        self.children.append(child)

class FuncCall():
    def __init__(self, symbol, args):
        self.symbol = symbol
        self.args = args

    def eval(self, st):
        new_st = SymbolTable(st)
        func = st.getSymbol(self.symbol)

        counter = 0

        if (func.args is not None):
            while (counter < len(func.args)):
                symbol = func.args[counter]
                new_st.setSymbol(symbol, self.args[counter].eval(st))
                counter += 1
        
        return func.child.eval(new_st)
        

class Main():
    def __init__(self, child):
        self.child = child
        self.main = FuncCall('main', [])
    
    def eval(self, st):
        self.child.eval(st)
        self.main.eval(st)



