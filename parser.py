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
             'RETURN', 'FUNC', 'COMMA'
             ]
        )

    def parse(self):      


        @self.pg.production('main : program IDENTIFIER QUOTE QUOTE SEMI_COLON')
        def main_st(p):
            st = SymbolTable(None)
            return (Main(p[0]))

        @self.pg.production('program : func_dec ')
        @self.pg.production('program : program func_dec')
        def program(p):
            if (len(p) == 1):
                return (Program([p[0]]))
            else:
                p[0].pushChild(p[1])
                return (p[0])

        @self.pg.production('func_dec : FUNC IDENTIFIER QUOTE QUOTE commands')
        @self.pg.production('func_dec : FUNC IDENTIFIER QUOTE func_var QUOTE commands')
        def func_dec(p):
            if(len(p) == 5):
                return FuncDec(p[1].getstr(), p[4], [])
            else:
                return FuncDec(p[1].getstr(), p[5], p[3])

        @self.pg.production('func_var : IDENTIFIER')
        @self.pg.production('func_var : func_var COMMA IDENTIFIER')
        def func_var(p):
            if (len(p) == 1):
                return ([p[0].getstr()])
            else:
                p[0].append(p[2].getstr())
                return(p[0])

        @self.pg.production('commands : O_KEY command_list C_KEY')
        def commands(p):
            return (p[1])

        @self.pg.production('command_list : command')        
        @self.pg.production('command_list : command_list command')
        def command_list(p):
            if (len(p) > 1):
                p[0].pushChild(p[1])
                return (p[0])
            else:
                return Commands([p[0]])


        @self.pg.production('command : IF QUOTE bool_exp QUOTE commands')
        @self.pg.production('command : IF QUOTE bool_exp QUOTE commands ELSE commands')
        def if_st (p):
            if (len(p) == 7):
                return If_Else(p[2], p[4], p[6])
            else:
                return If_Else(p[2], p[4], None)
        

        @self.pg.production('command : WHILE QUOTE bool_exp QUOTE commands')
        def while_st(p):
            return While(p[2], p[4])

        @self.pg.production('command : RETURN QUOTE expression QUOTE SEMI_COLON')
        def return_st(p):
            return (Return(p[2]))

        @self.pg.production('command : SCANF QUOTE IDENTIFIER QUOTE SEMI_COLON')
        def scanf_st(p):
            return Scanf(p[2].getstr())

        @self.pg.production('command : PRINTF QUOTE expression QUOTE SEMI_COLON')
        def printf_st(p):
            return Print(p[2])


        @self.pg.production('command : IDENTIFIER EQUAL expression SEMI_COLON')
        def attr(p):
            return Equal(p[0].getstr(), p[2])


        @self.pg.production('expression : FUNC IDENTIFIER QUOTE QUOTE')
        def expression_func(p):
            return (FuncCall(p[1].getstr(), []))

        @self.pg.production('expression : FUNC IDENTIFIER QUOTE passing_args QUOTE')
        def expression_func_with_args(p):
            return (FuncCall(p[1].getstr(), p[3]))
        
        @self.pg.production('passing_args : expression')
        @self.pg.production('passing_args : passing_args COMMA expression')
        def passing_args(p):
            if (len(p) == 1):
                return ([p[0]])
            else:
                p[0].append(p[2])
                return (p[0])

        @self.pg.production('bool_exp : expression IS_LESS expression')
        @self.pg.production('bool_exp : expression IS_GREATER expression')
        @self.pg.production('bool_exp : expression IS_EQUAL expression')
        def bool_exp(p):
            token_type = p[1].gettokentype()
            if (token_type == 'IS_LESS'):
                return Is_Less(p[0], p[2])
            if (token_type == 'IS_GREATER'):
                return Is_Greater(p[0], p[2])
            if (token_type == 'IS_EQUAL'):
                return Is_Equal(p[0], p[2])

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
            

        @self.pg.production('term : factor')
        def single_term(p):
            return (p[0])

        @self.pg.production('expression : term')
        def single_expression(p):
            return (p[0])

        @self.pg.production('factor : NUMBER')
        def factor_num(p):
            return (IntVal(int(p[0].getstr())))

        @self.pg.production('factor : IDENTIFIER')
        def factor_id(p):
            return (IdVal((p[0].getstr())))

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()