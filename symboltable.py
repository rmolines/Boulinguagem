class SymbolTable:

    def __init__(self, ancestor):
        self.valueTable = dict()
        self.ancestor = ancestor

    def setSymbol(self, symbol, value):
        self.valueTable[symbol] = value

    def getSymbol(self, symbol):
        st = self
        while (symbol not in st.valueTable):
            st = st.ancestor
            if (st is None):
                raise ValueError("id nao existe")

        return (st.valueTable[symbol])
    