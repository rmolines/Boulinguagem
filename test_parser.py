from rply import ParserGenerator
from ast import *

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER', 'PRINTF', 'SCANF', 'QUOTE',
             'SEMI_COLON', 'SUM', 'SUB', 'MULT', 'DIV',
             'MAIN', 'O_KEY', 'C_KEY', 'IF', 'WHILE', 'IDENTIFIER',
             'ELSE', 'EQUAL', 'IS_LESS', 'IS_GREATER', 'IS_EQUAL',
             'RETURN'
             ]
        )

    def parse(self):       
        @self.pg.production('test : MAIN QUOTE QUOTE commands MAIN QUOTE QUOTE SEMI_COLON')
        def test(p):
            return(p[3])

        @self.pg.production('commands : O_KEY command_list C_KEY')
        def commands(p):
            return Commands(p[1])

        @self.pg.production('command_list : command_list command SEMI_COLON')
        @self.pg.production('command_list : command SEMI_COLON')
        def command_list(p):
            if (len(p) > 1):
                p[0].add_child(p[1])
            else:
                return Command(p[0])

        @self.pg.production('command : IDENTIFIER EQUAL expression')
        def attr(p):
            return Equal(p[0].value, p[1])


        @self.pg.production('command : IF QUOTE bool_exp QUOTE commands')
        @self.pg.production('command : IF QUOTE bool_exp QUOTE commands ELSE commands')
        def if_st (p):
            if (len(p == 7)):
                return If_Else(p[2], p[4], p[6])
            else:
                return If_Else(p[2], p[4], None)
        

        @self.pg.production('command : WHILE QUOTE bool_exp QUOTE commands')
        def while_st(p):
            return While(p[2], p[4])

        @self.pg.production('command : SCANF QUOTE identifier QUOTE')
        def scanf_st(p):
            return Scanf(p[2])

        @self.pg.production('command : PRINTF QUOTE identifier QUOTE')
        def printf_st(p):
            return Prinft([2])


        @self.pg.production('bool_exp : expression bool_op expression')
        def bool_exp(p):
            pass

        @self.pg.production('command : RETURN QUOTE exp QUOTE')
        def return_st(p):
            pass

        @self.pg.production('expression : term SUM term')
        @self.pg.production('expression : term SUB term')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)

        @self.pg.production('expression : term')
        def expression_term(p):
            return (p[0])

        @self.pg.production('term : factor MULT factor')
        @self.pg.production('term : factor DIV factor')
        def term(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'MULT':
                return Mult(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)


        @self.pg.production('factor : QUOTE exp QUOTE')
        @self.pg.production('factor : MULT factor')
        @self.pg.production('factor : DIV factor')
        @self.pg.production('factor : MULT  factor')
        @self.pg.production('factor : NUMBER')
        def factor(p):
            if (len(p) == 1):
                return (int(p[0].getstr()))


        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()