from rply import LexerGenerator


class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):    
        # Identifier
        self.lexer.add('ID', r'\w+')
        # Brackets
        self.lexer.add('O_BRACKET', r'\{')
        self.lexer.add('C_BRACKET', r'\}')
        # While
        self.lexer.add('WHILE', r'wahrend')
        # Print
        self.lexer.add('PRINT', r'schreibe')
        # Scanf
        self.lexer.add('SCANF', r'lehre')
        # If
        self.lexer.add('IF', r'ob')
        self.lexer.add('ELSE', r'sonst')
        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')
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

        # Number
        self.lexer.add('NUMBER', r'\d+')
        # Ignore spaces
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()