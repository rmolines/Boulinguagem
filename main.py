from ast import *
from lexer import Lexer
from parser import Parser

text_input = """
funk main''[
    x = 6;
    y = 4;
    wahrend 'y<x'[
        y=y+1;
        lehre'z';
        ob 'y<z'[
            schreibe'z';
        ] sonst [
            schreibe'4';
        ]
    ]
]

main'';"""

text_input2 =  """
funk test''[
    x = 2;
    wahrend'x<5'[
        x=x+1;
    ]
    gib'x';
]

funk main''[
    a = funk test'';
    schreibe'x';
]

main'';"""

    
lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)


pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()