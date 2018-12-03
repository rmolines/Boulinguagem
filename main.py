from ast import *
from lexer import Lexer
from parser import Parser

text_input = """

funk sum'x, y'[
    gib'x+y';
]

funk main''[
    x = 6;
    y = 4;
    o = funk sum'2, 2';
    schreibe'o';
    wahrend 'y<x'[
        y=y+1;
        z = 24;
        ob 'y<z'[
            schreibe'z';
        ] sonst [
            schreibe'4';
        ]
    ]
]

main'';"""

text_input =  """
funk mult'x,y'[
    gib'x*y';
]
funk test''[
    x = 2;
    wahrend'x<5'[
        x=x+1;
    ]
    gib'funk mult'x, 2'';
]

funk main''[
    a = funk test'';
    ob'a<11'[
        schreibe'24';
    ] sonst [
        schreibe'35';
    ]
]

main'';"""

    
lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)


pg = Parser()
pg.parse()
parser = pg.get_parser()
st = SymbolTable(None)
parser.parse(tokens).eval(st)