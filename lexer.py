from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):    
        # Comma
        self.lexer.add('COMMA', r',')
        # Brackets
        self.lexer.add('O_KEY', r'\[')
        self.lexer.add('C_KEY', r'\]')
        # While
        self.lexer.add('WHILE', r'wahrend')
        # Print
        self.lexer.add('PRINTF', r'schreibe')
        # Scanf
        self.lexer.add('SCANF', r'lehre')
        # If
        self.lexer.add('IF', r'ob')
        self.lexer.add('ELSE', r'sonst')
        # Parenthesis
        self.lexer.add('QUOTE', r'\'')
        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')
        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('DIV', r'\\')
        self.lexer.add('EQUAL', r'\=')
        self.lexer.add('IS_LESS', r'\<')
        self.lexer.add('IS_GREATER', r'\>')
        self.lexer.add('IS_EQUAL', r'\=\=')
        # Return
        self.lexer.add('RETURN', r'gib')
        # Function
        self.lexer.add('FUNC', r'funk')
        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Identifier
        self.lexer.add('IDENTIFIER', r'\w+')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()